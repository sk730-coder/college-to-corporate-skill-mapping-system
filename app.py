import os
import json
import hmac
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.utils import secure_filename
from database import (
    init_db, search_companies, get_all_companies,
    get_roles_for_company, get_skills_for_role,
    get_company_by_id, get_role_by_id, estimate_hiring_expectation_months,
    clear_all_activities
)
from resume_parser import try_pdf_extract, extract_skills_from_text
from skill_analyzer import analyze_skills, score_label

# Load settings from a .env file if python-dotenv is installed (optional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")

# Admin password comes from the environment, never from the source code.
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

# Enhanced user tracking with detailed activity - GLOBAL VARIABLES
user_sessions = []
user_activities = []  

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ─── Routes ──────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/select-stream')
def select_stream():
    """Route for choosing between Engineering or Arts & Science."""
    return render_template('select_stream.html')


@app.route('/set-stream/<int:stream_id>')
def set_stream(stream_id):
    # 1: Engineering, 2: Arts & Science
    session['stream'] = int(stream_id)
    return redirect(url_for('search'))


@app.route('/search')
def search():
    stream = session.get('stream')
    if not stream:
        return redirect(url_for('select_stream'))
    companies = get_all_companies(stream=stream)
    return render_template('search.html', companies=companies, stream=stream)


@app.route('/api/companies')
def api_companies():
    q = request.args.get('q', '').strip()
    stream = session.get('stream', 1)  # Default to engineering stream
    if q:
        companies = search_companies(q, stream=stream)
    else:
        companies = get_all_companies(stream=stream)
    return jsonify(companies)


@app.route('/api/roles/<int(signed=True):company_id>')
def api_roles(company_id):
    stream = session.get('stream', 1)  # Default to engineering stream
    roles = get_roles_for_company(company_id, stream=stream)
    company = get_company_by_id(company_id)
    company_name = company["name"] if company else None
    normalized_stream = stream if stream in (1, 2) else 1

    # Defensive fallback so UI always receives month names.
    for role in roles:
        if not role.get("hiring_expectation_months"):
            role["hiring_expectation_months"] = estimate_hiring_expectation_months(
                role.get("role_name", ""),
                normalized_stream,
                company_name
            )
    return jsonify(roles)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    company_id = request.args.get('company_id') or request.form.get('company_id')
    role_id = request.args.get('role_id') or request.form.get('role_id')
    stream = session.get('stream')

    if not company_id or not role_id:
        return redirect(url_for('search'))

    try:
        company_id_int = int(company_id)
        role_id_int = int(role_id)
    except (TypeError, ValueError):
        return redirect(url_for('search'))

    company = get_company_by_id(company_id_int)
    role = get_role_by_id(role_id_int)

    if not company or not role:
        return redirect(url_for('search'))

    if request.method == 'POST':
        print(f"[DEBUG] Upload POST request received")
        student_skills = set()
        pdf_used = False

        # PDF-only resume parsing.
        saved_name = None
        if 'resume' in request.files:
            file = request.files['resume']
            if file and file.filename and allowed_file(file.filename):
                saved_name = f"{uuid.uuid4().hex[:8]}_{secure_filename(file.filename)}"
                filepath = os.path.join(UPLOAD_FOLDER, saved_name)
                file.save(filepath)
                parsed_skills, parse_success = try_pdf_extract(filepath)
                if parse_success and parsed_skills:
                    student_skills = parsed_skills
                    pdf_used = True

        if not student_skills:
            return render_template('upload.html', company=company, role=role,
                                   error="Please upload a readable PDF resume with your technical skills.")

        # Run analysis
        role_skills = get_skills_for_role(role_id_int)
        
        result = analyze_skills(student_skills, role_skills, role.get('role_name', ''))
        result['score_info'] = score_label(result['score'])
        result['pdf_used'] = pdf_used
        result['student_skills'] = sorted(list(student_skills))

        # Store in session for result page
        session['result'] = result
        session['company'] = company
        session['role'] = role
        
        print(f"[DEBUG] About to track admin data - Result keys: {result.keys()}")
        print(f"[DEBUG] Matched in result: {result.get('matched', 'NOT_FOUND')}")
        print(f"[DEBUG] Missing in result: {result.get('missing', 'NOT_FOUND')}")
        
        # Track resume upload for admin dashboard - PUT IT HERE AFTER SESSION IS SET
        user_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.environ.get('REMOTE_ADDR', 'unknown'))
        
        # Get detailed skill information from result
        matched_skills = result.get('matched', [])
        missing_skills = result.get('missing', {})
        
        print(f"[DEBUG] Raw matched skills: {matched_skills}")
        print(f"[DEBUG] Raw missing skills: {missing_skills}")
        
        # Flatten missing skills
        all_missing_skills = []
        for skill_category in ['core', 'good', 'bonus']:
            if skill_category in missing_skills:
                all_missing_skills.extend(missing_skills[skill_category])
        
        print(f"[DEBUG] Flattened missing skills: {all_missing_skills}")
        
        # Extract user name from resume content
        user_name = "Unknown User"
        if pdf_used and saved_name:
            try:
                # Read the PDF content to extract name
                from pypdf import PdfReader
                filepath = os.path.join(UPLOAD_FOLDER, saved_name)
                with open(filepath, 'rb') as f:
                    reader = PdfReader(f)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text() or ""
                    
                    # Simple name extraction (first line that looks like a name)
                    lines = text.split('\n')
                    for line in lines[:10]:  # Check first 10 lines
                        line_stripped = line.strip()
                        if (len(line_stripped) > 2 and len(line_stripped) < 50 and 
                            not any(char in line_stripped for char in ['@', '.', '(', ')', '/', '\\', '|', '-', '_']) and
                            not any(word in line_stripped.lower() for word in ['resume', 'curriculum', 'vitae', 'experience', 'education', 'skills', 'projects', 'contact', 'phone', 'email', 'address'])):
                            # Check if it looks like a name (has spaces and capital letters)
                            if ' ' in line_stripped and line_stripped.replace(' ', '').isalpha():
                                user_name = line_stripped.title()
                                break
            except Exception as e:
                print(f"[DEBUG] Name extraction error: {e}")
                user_name = "Unknown User"
        
        # Process skills - SIMPLE AND DIRECT
        processed_matched = [skill.title() if isinstance(skill, str) else str(skill).title() for skill in matched_skills]
        processed_missing = [skill.title() if isinstance(skill, str) else str(skill).title() for skill in all_missing_skills]
        
        print(f"[DEBUG] Final processed matched: {processed_matched}")
        print(f"[DEBUG] Final processed missing: {processed_missing}")
        
        # Calculate total missing skills properly
        total_missing = len(missing_skills.get('core', [])) + len(missing_skills.get('good', [])) + len(missing_skills.get('bonus', []))
        
        # Create and store activity - ENSURE ALL FIELDS ARE PRESENT
        activity = {
            'ip': user_ip,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'resume_upload',
            'company_name': company['name'],
            'role_name': role['role_name'],
            'company_id': company_id,
            'role_id': role_id,
            'academic_stream': 'Engineering' if stream == 1 else 'Arts & Science',
            'user_name': user_name,
            'skills_matched': result.get('total_matched', 0),
            'skills_missing': total_missing,
            'match_score': result.get('score', 0),
            'matched_skills_list': processed_matched,
            'missing_skills_list': processed_missing
        }
        
        print(f"[DEBUG] ACTIVITY BEING STORED:")
        for key, value in activity.items():
            print(f"  {key}: {value}")
        
        user_activities.append(activity)
        print(f"[DEBUG] ACTIVITY STORED SUCCESSFULLY")
        print(f"[DEBUG] Total activities in list: {len(user_activities)}")
        
        # Store resume content for later use in resume generation
        if pdf_used and saved_name:
            session['resume_filename'] = saved_name

        return redirect(url_for('result'))

    return render_template('upload.html', company=company, role=role, error=None)


@app.route('/result')
def result():
    result = session.get('result')
    company = session.get('company')
    role = session.get('role')

    if not result:
        return redirect(url_for('search'))

    return render_template('result.html', result=result, company=company, role=role)


@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    """Generate ATS-friendly resume based on job requirements and user's resume"""
    try:
        result = session.get('result')
        company = session.get('company')
        role = session.get('role')
        resume_filename = session.get('resume_filename')
        
        if not all([result, company, role]):
            return jsonify({'error': 'Missing session data'}), 400
        
        # Get the original resume content if available
        original_content = ""
        if resume_filename:
            resume_path = os.path.join(UPLOAD_FOLDER, resume_filename)
            if os.path.exists(resume_path):
                from pypdf import PdfReader
                try:
                    reader = PdfReader(resume_path)
                    content_chunks = []
                    for page in reader.pages:
                        page_text = page.extract_text() or ""
                        if page_text.strip():
                            content_chunks.append(page_text)
                    original_content = "\n".join(content_chunks)
                except Exception as e:
                    print(f"Error reading original resume: {e}")
        
        # Generate ATS-friendly resume
        ats_resume = generate_ats_resume(
            original_content=original_content,
            student_skills=result.get('student_skills', []),
            company=company,
            role=role,
            role_skills=get_skills_for_role(role['id']),
            analysis_result=result
        )
        
        return jsonify({
            'success': True,
            'resume_content': ats_resume
        })
        
    except Exception as e:
        print(f"Resume generation error: {e}")
        return jsonify({'error': 'Failed to generate resume'}), 500


def generate_ats_resume(original_content, student_skills, company, role, role_skills, analysis_result):
    """
    Generate ATS-friendly resume content with proper resume formatting
    """
    
    # Extract key information from original content
    lines = original_content.split('\n') if original_content else []
    name = ""
    email = ""
    phone = ""
    education = ""
    location = ""
    
    # Simple extraction of personal information
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        line_lower = line_stripped.lower()
        
        # Try to extract name (usually first line with no special characters)
        if not name and i < 3 and len(line_stripped) > 2 and len(line_stripped) < 50:
            if not any(char in line_stripped for char in ['@', '.', '(', ')', '/', '\\', '|']) and not any(word in line_lower for word in ['resume', 'curriculum', 'vitae']):
                name = line_stripped.upper()
        
        if '@' in line_stripped and '.' in line_stripped and not email:
            email = line_stripped
        elif any(char.isdigit() for char in line_stripped) and len(line_stripped) >= 10 and not phone:
            # Check if it looks like a phone number
            digits = ''.join(filter(str.isdigit, line_stripped))
            if len(digits) >= 10:
                phone = line_stripped
        elif any(word in line_lower for word in ['b.tech', 'b.e', 'bachelor', 'university', 'college']) and not education:
            education = line_stripped
        elif any(word in line_lower for word in ['chennai', 'bangalore', 'mumbai', 'delhi', 'hyderabad', 'pune', 'india']) and not location:
            location = line_stripped
    
    # Prioritize skills based on job requirements
    matched_skills = analysis_result.get('matched', [])
    missing_core = analysis_result.get('missing', {}).get('core', [])
    missing_good = analysis_result.get('missing', {}).get('good', [])
    
    # Categorize skills
    technical_skills = []
    soft_skills = []
    
    for skill in student_skills:
        skill_lower = skill.lower()
        if any(soft in skill_lower for soft in ['communication', 'leadership', 'teamwork', 'problem solving', 'project management', 'analytical thinking']):
            soft_skills.append(skill.title())
        else:
            technical_skills.append(skill.title())
    
    # Add missing core skills as "learning/familiar with"
    learning_skills = [skill.title() for skill in missing_core]
    
    # Build properly formatted resume
    resume_lines = []
    
    # Header with name and contact info
    if name:
        resume_lines.append(name)
        resume_lines.append("=" * len(name))
        resume_lines.append("")
    
    # Contact information
    contact_info = []
    if email:
        contact_info.append(f"Email: {email}")
    if phone:
        contact_info.append(f"Phone: {phone}")
    if location:
        contact_info.append(f"Location: {location}")
    
    if contact_info:
        resume_lines.append(" | ".join(contact_info))
        resume_lines.append("")
    
    # Professional Summary
    resume_lines.append("PROFESSIONAL SUMMARY")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    summary_lines = [
        f"Results-driven {role['role_name'].upper()} with expertise in {', '.join(technical_skills[:5])}.",
        f"Passionate about leveraging technical skills to deliver innovative solutions for {company['name'].upper()}.",
        f"Strong foundation in {', '.join(soft_skills[:3])} with a commitment to continuous learning and professional growth.",
        f"Successfully matched {len(matched_skills)} out of {len(matched_skills) + len(missing_core) + len(missing_good)} required skills for this position."
    ]
    
    for summary_line in summary_lines:
        resume_lines.append(f"- {summary_line}")
    resume_lines.append("")
    
    # Technical Skills Section
    resume_lines.append("TECHNICAL SKILLS")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    if technical_skills:
        # Group skills by category for better organization
        programming_langs = [skill for skill in technical_skills if skill.lower() in ['python', 'java', 'javascript', 'c++', 'c#', 'go', 'rust', 'typescript']]
        web_techs = [skill for skill in technical_skills if any(tech.lower() in skill.lower() for tech in ['react', 'angular', 'vue', 'node', 'html', 'css', 'django', 'flask'])]
        databases = [skill for skill in technical_skills if any(db.lower() in skill.lower() for db in ['sql', 'mysql', 'postgresql', 'mongodb', 'redis'])]
        cloud_devops = [skill for skill in technical_skills if any(cloud.lower() in skill.lower() for cloud in ['aws', 'azure', 'docker', 'kubernetes', 'ci/cd', 'devops'])]
        other_techs = [skill for skill in technical_skills if skill not in programming_langs + web_techs + databases + cloud_devops]
        
        if programming_langs:
            resume_lines.append(f"Programming Languages: {', '.join(programming_langs)}")
        if web_techs:
            resume_lines.append(f"Web Technologies: {', '.join(web_techs)}")
        if databases:
            resume_lines.append(f"Databases: {', '.join(databases)}")
        if cloud_devops:
            resume_lines.append(f"Cloud & DevOps: {', '.join(cloud_devops)}")
        if other_techs:
            resume_lines.append(f"Other Technologies: {', '.join(other_techs)}")
        
        resume_lines.append("")
    
    if learning_skills:
        resume_lines.append("Currently Learning:")
        for skill in learning_skills:
            resume_lines.append(f"  → {skill}")
        resume_lines.append("")
    
    # Soft Skills Section
    if soft_skills:
        resume_lines.append("SOFT SKILLS")
        resume_lines.append("-" * 20)
        resume_lines.append("")
        resume_lines.append(f"- {', '.join(soft_skills)}")
        resume_lines.append("")
    
    # Professional Experience Section
    resume_lines.append("PROFESSIONAL EXPERIENCE")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    # Create experience based on user's skills
    exp_techs = [s for s in technical_skills if s in ['JavaScript', 'Python', 'Java', 'React', 'Node.js', 'Django', 'Flask', 'Spring']][:4]
    exp_tools = [s for s in technical_skills if s in ['Git', 'Docker', 'AWS', 'Azure', 'MongoDB', 'PostgreSQL', 'MySQL']][:3]
    
    resume_lines.append("SOFTWARE ENGINEER INTERN")
    resume_lines.append("Tech Solutions Inc. | Chennai, India")
    resume_lines.append("Jan 2024 - Present")
    resume_lines.append("")
    
    experience_points = [
        f"Developed and maintained web applications using {', '.join(exp_techs)}",
        f"Implemented {', '.join(exp_tools)} for version control, deployment, and data management",
        "Collaborated with cross-functional teams to deliver high-quality software solutions",
        "Participated in code reviews, testing, and agile development methodologies",
        f"Contributed to {len(matched_skills)} successful project deployments using modern development practices"
    ]
    
    for point in experience_points:
        resume_lines.append(f"- {point}")
    resume_lines.append("")
    
    # Academic Projects Section
    resume_lines.append("ACADEMIC PROJECTS")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    # Create project based on user's skills
    project_techs = [s for s in technical_skills if s in ['React', 'Node.js', 'Python', 'Django', 'Flask', 'Spring', 'Angular']][:3]
    project_dbs = [s for s in technical_skills if s in ['MongoDB', 'PostgreSQL', 'MySQL', 'Redis']][:2]
    project_concepts = [s for s in technical_skills if s in ['Data Structures', 'Algorithms', 'REST API', 'System Design']][:2]
    
    resume_lines.append("FULL-STACK WEB APPLICATION")
    resume_lines.append("Final Year Project | Computer Engineering")
    resume_lines.append("")
    
    project_points = [
        f"Architected and developed a comprehensive web application using {', '.join(project_techs)}",
        f"Implemented {', '.join(project_dbs)} for efficient data storage and retrieval",
        f"Applied knowledge of {', '.join(project_concepts)} to optimize system performance",
        "Designed responsive user interface with modern CSS frameworks",
        "Deployed application on cloud platform with CI/CD pipeline"
    ]
    
    for point in project_points:
        resume_lines.append(f"- {point}")
    resume_lines.append("")
    
    # Education Section
    resume_lines.append("EDUCATION")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    if education:
        resume_lines.append(education)
    else:
        resume_lines.append("BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE ENGINEERING")
        resume_lines.append("Anna University | Chennai, India")
        resume_lines.append("2020 - 2024 | CGPA: 8.5/10")
    resume_lines.append("")
    
    # Key Achievements Section
    resume_lines.append("KEY ACHIEVEMENTS")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    achievements = [
        f"Skill Match Score: {analysis_result.get('score', 0)}% for {role['role_name']} position at {company['name']}",
        f"Proficient in {len(technical_skills)} technical technologies and {len(soft_skills)} soft skills",
        "Successfully completed multiple full-stack development projects",
        "Active contributor to open-source projects and technical communities"
    ]
    
    for achievement in achievements:
        resume_lines.append(f"- {achievement}")
    resume_lines.append("")
    
    # ATS Keywords Section (for optimization, but hide in display)
    resume_lines.append("ATS KEYWORDS")
    resume_lines.append("-" * 20)
    resume_lines.append("")
    
    all_keywords = []
    all_keywords.extend(technical_skills)
    all_keywords.extend(soft_skills)
    all_keywords.extend([company['name'], role['role_name']])
    all_keywords.extend([skill.title() for skill in role_skills.get('core', [])])
    all_keywords.extend([skill.title() for skill in role_skills.get('good', [])])
    
    resume_lines.append(", ".join(list(set(all_keywords))))
    resume_lines.append("")
    
    # Footer
    resume_lines.append("=" * 50)
    resume_lines.append(f"SAMPLE UPDATED RESUME - Optimized for {company['name'].upper()} {role['role_name'].upper()} Position")
    resume_lines.append("=" * 50)
    
    return "\n".join(resume_lines)


@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))


@app.route('/admin')
def admin_entry():
    return render_template('admin_login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    print(f"[DEBUG] Admin dashboard accessed!")
    # Simple session-based admin authentication (set after a successful login)
    if not session.get('admin_authenticated'):
        return redirect(url_for('admin_entry'))
    
    try:
        # Calculate user analytics
        unique_users = len(set(session['ip'] for session in user_sessions))
        total_sessions = len(user_sessions)
        today_users = len(set(session['ip'] for session in user_sessions 
                             if session['timestamp'].startswith(datetime.now().strftime('%Y-%m-%d'))))
        
        # Resume upload statistics
        resume_uploads = [activity for activity in user_activities if activity['type'] == 'resume_upload']
        total_resume_uploads = len(resume_uploads)
        today_resume_uploads = len([activity for activity in resume_uploads 
                                   if activity['timestamp'].startswith(datetime.now().strftime('%Y-%m-%d'))])
        
        # Popular companies and roles
        popular_companies = {}
        popular_roles = {}
        for activity in resume_uploads:
            company = activity['company_name']
            role = activity['role_name']
            popular_companies[company] = popular_companies.get(company, 0) + 1
            popular_roles[role] = popular_roles.get(role, 0) + 1
        
        # Get recent detailed activities
        recent_activities = []
        print(f"[DEBUG] Admin: Processing {len(user_activities)} total activities")
        
        # Just get the last 10 activities directly without any processing
        recent_activities = user_activities[-10:] if user_activities else []
        
        print(f"[DEBUG] Admin: Recent activities count: {len(recent_activities)}")
        if recent_activities:
            latest = recent_activities[-1]
            print(f"[DEBUG] Admin: Latest activity keys: {latest.keys()}")
            print(f"[DEBUG] Admin: Latest user: {latest.get('user_name', 'NOT_FOUND')}")
            print(f"[DEBUG] Admin: Latest stream: {latest.get('academic_stream', 'NOT_FOUND')}")
            print(f"[DEBUG] Admin: Latest matched skills: {latest.get('matched_skills_list', 'NOT_FOUND')}")
            print(f"[DEBUG] Admin: Latest missing skills: {latest.get('missing_skills_list', 'NOT_FOUND')}")
        
        print(f"[DEBUG] Admin Dashboard Data:")
        print(f"  - Total resume uploads: {total_resume_uploads}")
        print(f"  - Recent activities count: {len(recent_activities)}")
        if recent_activities:
            latest = recent_activities[-1]
            print(f"  - Latest activity: {latest.get('company_name', 'N/A')} - {latest.get('role_name', 'N/A')}")
            print(f"  - Latest user: {latest.get('user_name', 'N/A')}")
            print(f"  - Latest matched skills: {len(latest.get('matched_skills_list', []))}")
            print(f"  - Latest missing skills: {len(latest.get('missing_skills_list', []))}")
        else:
            print(f"  - No recent activities found")
        
        return render_template('admin.html', 
                             unique_users=unique_users,
                             total_sessions=total_sessions,
                             today_users=today_users,
                             total_resume_uploads=total_resume_uploads,
                             today_resume_uploads=today_resume_uploads,
                             popular_companies=sorted(popular_companies.items(), key=lambda x: x[1], reverse=True)[:5],
                             popular_roles=sorted(popular_roles.items(), key=lambda x: x[1], reverse=True)[:5],
                             recent_activities=recent_activities)
    
    except Exception as e:
        print(f"[ERROR] Admin dashboard error: {e}")
        import traceback
        traceback.print_exc()
        return render_template('admin.html', 
                             unique_users=0,
                             total_sessions=0,
                             today_users=0,
                             total_resume_uploads=0,
                             today_resume_uploads=0,
                             popular_companies=[],
                             popular_roles=[],
                             recent_activities=[])


@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    if not ADMIN_PASSWORD:
        return render_template('admin_login.html',
                               error='Admin login is disabled: set the ADMIN_PASSWORD environment variable.')
    if hmac.compare_digest(password.encode(), ADMIN_PASSWORD.encode()):
        session['admin_authenticated'] = True
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html', error='Invalid password')


@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_authenticated', None)
    return redirect(url_for('admin_entry'))


@app.route('/admin/clear', methods=['POST'])
def admin_clear():
    if not session.get('admin_authenticated'):
        return redirect(url_for('admin_entry'))
    clear_all_activities()
    user_activities.clear()
    user_sessions.clear()
    return redirect(url_for('admin_dashboard'))


@app.before_request
def track_user():
    if request.endpoint and request.endpoint not in ['admin_entry', 'admin_dashboard', 'admin_login', 'static']:
        user_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.environ.get('REMOTE_ADDR', 'unknown'))
        session_data = {
            'ip': user_ip,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'path': request.path,
            'user_agent': request.headers.get('User-Agent', 'Unknown')[:100]
        }
        user_sessions.append(session_data)
        
        # Keep only last 1000 records
        if len(user_sessions) > 1000:
            user_sessions.pop(0)
        if len(user_activities) > 1000:
            user_activities.pop(0)

if __name__ == '__main__':
    print("[*] Initializing database...")
    init_db()
    print("[*] Starting College to Corporate Skill Mapper...")
    print("    Open: http://127.0.0.1:5000")
    # Set FLASK_DEBUG=1 in .env only while developing; debug mode exposes a code console.
    app.run(debug=os.environ.get('FLASK_DEBUG') == '1', use_reloader=False)

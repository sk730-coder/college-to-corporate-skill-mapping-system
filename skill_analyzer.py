from roadmap_data import get_skill_info

PRIORITY_ORDER = {"core": 1, "good": 2, "bonus": 3}
SOFT_SKILLS = {
    "communication", "problem solving", "teamwork", "interpersonal skills",
    "stakeholder management", "presentation skills", "analytical thinking"
}


def is_soft_skill_role(role_name: str) -> bool:
    role = (role_name or "").lower()
    soft_role_keywords = (
        "hr", "customer", "sales", "marketing", "bpo", "support", "relationship",
        "content", "business analyst", "process associate", "customer success"
    )
    return any(k in role for k in soft_role_keywords)


def analyze_skills(student_skills: set, role_skills: dict, role_name: str = "") -> dict:
    """
    Enhanced skill comparison with perfect matching and comprehensive analysis.

    Args:
        student_skills: Set of lowercase skill strings from the student.
        role_skills: Dict with keys 'core', 'good', 'bonus' each being a list.
        role_name: Name of the role for context-aware analysis.

    Returns:
        A result dict with matched, missing (by priority), score, and roadmap.
    """
    all_required = {}
    include_soft_skills = is_soft_skill_role(role_name)
    
    # Build comprehensive skill mapping with variations
    skill_variations = {
        'javascript': ['javascript', 'js'],
        'typescript': ['typescript', 'ts'],
        'python': ['python', 'py'],
        'java': ['java'],
        'react': ['react', 'reactjs', 'react.js'],
        'node.js': ['node.js', 'nodejs', 'node'],
        'machine learning': ['machine learning', 'ml'],
        'artificial intelligence': ['artificial intelligence', 'ai'],
        'deep learning': ['deep learning', 'dl'],
        'natural language processing': ['natural language processing', 'nlp'],
        'computer vision': ['computer vision', 'cv'],
        'data structures': ['data structures', 'dsa'],
        'algorithms': ['algorithms', 'algo'],
        'ui design': ['ui design', 'ui'],
        'ux design': ['ux design', 'ux'],
        'testing': ['testing', 'qa'],
        'ci/cd': ['ci/cd', 'ci', 'cd'],
        'sql': ['sql', 'rdbms'],
        'nosql': ['nosql'],
        'rest api': ['rest api', 'restful', 'rest'],
        'graphql': ['graphql', 'gql'],
        'html': ['html', 'html5'],
        'css': ['css', 'css3'],
        'devops': ['devops'],
        'docker': ['docker'],
        'kubernetes': ['kubernetes', 'k8s'],
        'aws': ['aws', 'amazon web services'],
        'azure': ['azure', 'microsoft azure'],
        'gcp': ['gcp', 'google cloud'],
        'git': ['git', 'github', 'gitlab'],
        'linux': ['linux', 'ubuntu', 'centos'],
        'excel': ['excel', 'microsoft excel'],
        'power bi': ['power bi', 'powerbi'],
        'tableau': ['tableau'],
        'figma': ['figma'],
        'selenium': ['selenium'],
        'jira': ['jira'],
        'communication': ['communication', 'comm'],
        'problem solving': ['problem solving', 'problem-solving'],
        'teamwork': ['teamwork', 'team work'],
        'leadership': ['leadership', 'lead'],
        'project management': ['project management', 'pm'],
        'agile': ['agile'],
        'scrum': ['scrum'],
        'microservices': ['microservices', 'micro service'],
        'system design': ['system design', 'system architecture'],
        'data analysis': ['data analysis', 'analytics'],
        'data science': ['data science', 'ds']
    }
    
    # Create reverse mapping for student skills
    student_skill_map = {}
    for skill in student_skills:
        skill_lower = skill.lower().strip()
        student_skill_map[skill_lower] = skill_lower
        
        # Map variations to canonical form
        for canonical, variations in skill_variations.items():
            if skill_lower in variations:
                student_skill_map[canonical] = skill_lower
                break
    
    # Process required skills
    for priority, skills in role_skills.items():
        for skill in skills:
            skill_key = skill.lower().strip()
            
            # Skip soft skills for technical roles
            if not include_soft_skills and skill_key in SOFT_SKILLS:
                continue
                
            all_required[skill_key] = priority

    # Enhanced matching with variations
    matched = []
    missing = {"core": [], "good": [], "bonus": []}
    matched_details = []

    for skill, priority in all_required.items():
        found_match = False
        matched_skill = None
        
        # Check direct match first
        if skill in student_skill_map:
            found_match = True
            matched_skill = student_skill_map[skill]
        
        # Check variations if no direct match
        if not found_match and skill in skill_variations:
            for variation in skill_variations[skill]:
                if variation in student_skill_map:
                    found_match = True
                    matched_skill = student_skill_map[variation]
                    break
        
        # Check partial matches for multi-word skills
        if not found_match and ' ' in skill:
            skill_words = skill.split()
            if len(skill_words) >= 2:
                # Check if most words are present
                matching_words = sum(1 for word in skill_words if any(word in student_skill for student_skill in student_skill_map))
                if matching_words >= len(skill_words) - 1:  # Allow 1 word mismatch
                    found_match = True
                    matched_skill = skill
        
        if found_match:
            matched.append(skill)
            matched_details.append({
                'required': skill,
                'found': matched_skill,
                'priority': priority
            })
        else:
            missing[priority].append(skill)

    # Enhanced scoring with detailed breakdown
    total_weight = sum(
        len([s for s, p in all_required.items() if p == priority]) * weight
        for priority, weight in [("core", 3), ("good", 2), ("bonus", 1)]
    )
    
    earned_weight = sum(
        3 if priority == "core" else 2 if priority == "good" else 1
        for skill, priority in all_required.items()
        if skill in [m['required'] for m in matched_details]
    )
    
    score = round((earned_weight / total_weight * 100) if total_weight else 0)

    # Build comprehensive roadmap
    roadmap = {}
    for priority in ("core", "good", "bonus"):
        roadmap[priority] = []
        for skill in missing[priority]:
            info = get_skill_info(skill)
            roadmap[priority].append({
                "skill": skill,
                "label": info.get("label", skill.title()),
                "resources": info.get("resources", []),
                "fast": info.get("fast", "Varies"),
                "moderate": info.get("moderate", "Varies"),
                "slow": info.get("slow", "Varies"),
                "category": info.get("category", "General")
            })

    return {
        "matched": matched,
        "matched_details": matched_details,  # Detailed matching info
        "missing": missing,
        "score": score,
        "roadmap": roadmap,
        "total_required": len(all_required),
        "total_matched": len(matched),
        "student_skills_found": list(student_skills),  # All skills found in resume
        "skill_coverage": {
            "core": {
                "required": len([s for s, p in all_required.items() if p == "core"]),
                "matched": len([s for s, p in all_required.items() if p == "core" and s in matched])
            },
            "good": {
                "required": len([s for s, p in all_required.items() if p == "good"]),
                "matched": len([s for s, p in all_required.items() if p == "good" and s in matched])
            },
            "bonus": {
                "required": len([s for s, p in all_required.items() if p == "bonus"]),
                "matched": len([s for s, p in all_required.items() if p == "bonus" and s in matched])
            }
        }
    }


def score_label(score: int) -> dict:
    """Return a label and color class for a given score."""
    if score >= 80:
        return {"label": "Excellent Match! 🎉", "cls": "excellent"}
    elif score >= 60:
        return {"label": "Good Match 👍", "cls": "good"}
    elif score >= 40:
        return {"label": "Fair Match — Keep Learning 📚", "cls": "fair"}
    else:
        return {"label": "Needs Work — Big Opportunity Ahead 💪", "cls": "poor"}

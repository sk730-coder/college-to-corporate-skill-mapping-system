import re

# Master list of recognizable skills (lowercase keys) - Enhanced for comprehensive coverage
SKILL_KEYWORDS = {
    # Programming Languages
    "python", "java", "javascript", "c++", "c#", "go", "ruby", "php", "swift", "kotlin",
    "rust", "scala", "perl", "r", "matlab", "shell script", "powershell", "bash",
    
    # Web Technologies
    "html", "html5", "css", "css3", "sass", "scss", "less", "react", "angular", "vue", "next.js",
    "node.js", "express", "django", "flask", "spring", "spring boot", "laravel", "rails",
    
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "sqlite", "redis", "oracle", "cassandra", "elasticsearch",
    "firebase", "supabase", "dynamodb", "neo4j", "influxdb",
    
    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "terraform", "ansible", "puppet",
    "jenkins", "gitlab ci", "github actions", "ci/cd", "linux", "ubuntu", "centos", "debian",
    "nginx", "apache", "microservices", "serverless", "lambda", "cloud functions",
    
    # Data Science & ML
    "machine learning", "deep learning", "tensorflow", "pytorch", "keras", "scikit-learn", "nlp",
    "computer vision", "data analysis", "data science", "pandas", "numpy", "matplotlib", "seaborn",
    "plotly", "spark", "hadoop", "kafka", "airflow", "etl", "data warehouse", "big data",
    
    # Testing & QA
    "testing", "unit testing", "integration testing", "e2e testing", "manual testing", "automation testing",
    "selenium", "cypress", "playwright", "jest", "mocha", "jasmine", "junit", "testng", "postman",
    "api testing", "performance testing", "load testing", "jira", "confluence",
    
    # Core CS
    "data structures", "algorithms", "system design", "os concepts", "operating systems", "networking",
    "computer networks", "tcp/ip", "http", "https", "rest api", "restful", "graphql", "websockets",
    "api", "microservices", "design patterns", "oop", "functional programming",
    
    # Tools & Technologies
    "git", "github", "gitlab", "bitbucket", "svn", "mercurial", "vim", "vs code", "intellij", "eclipse",
    "maven", "gradle", "npm", "yarn", "pip", "conda", "docker compose", "kubernetes",
    
    # Business & Analytics
    "excel", "power bi", "tableau", "looker", "google analytics", "salesforce", "sap", "salesforce crm",
    "financial analysis", "business intelligence", "data visualization", "reporting", "dashboards",
    
    # Design & UX
    "figma", "sketch", "adobe xd", "photoshop", "illustrator", "ui design", "ux design", "wireframing",
    "prototyping", "responsive design", "mobile design", "web design",
    
    # Soft Skills & Business
    "communication", "problem solving", "teamwork", "leadership", "project management", "agile", "scrum",
    "kanban", "stakeholder management", "presentation skills", "public speaking", "negotiation",
    "time management", "critical thinking", "analytical thinking", "decision making",
    
    # Marketing & Content
    "content writing", "copywriting", "seo", "sem", "social media marketing", "email marketing",
    "content strategy", "branding", "growth hacking", "digital marketing", "market research",
    
    # HR & Operations
    "recruitment", "talent acquisition", "employee relations", "hr management", "payroll", "hris",
    "performance management", "training", "onboarding", "compensation", "benefits",
    
    # Security
    "cybersecurity", "information security", "network security", "application security", "ethical hacking",
    "penetration testing", "security audit", "compliance", "risk management", "firewall",
    
    # Additional Technical Skills
    "typescript", "redux", "webpack", "babel", "eslint", "prettier", "jquery", "bootstrap", "tailwind",
    "material ui", "ant design", "chakra ui", "nextauth", "passport", "jwt", "oauth", "authentication",
    "authorization", "encryption", "hashing", "ssl", "tls", "caching", "cdn", "cloudflare",
    
    # Emerging Technologies
    "blockchain", "web3", "solidity", "smart contracts", "ar", "vr", "iot", "edge computing",
    "quantum computing", "robotics", "automation", "rpa", "chatbot", "ai", "artificial intelligence"
}


def extract_skills_from_text(text: str) -> set:
    """
    Extract skill keywords from free text (resume, comma-separated input, etc.)
    Enhanced to be more comprehensive and accurate.
    Returns a set of lowercase skill strings.
    """
    if not text:
        return set()

    text_lower = text.lower()
    found = set()

    # Normalize text for better matching
    # Replace common separators and normalize whitespace
    normalized_text = re.sub(r'[,\.;:()\[\]{}"\'/\\]', ' ', text_lower)
    normalized_text = re.sub(r'\s+', ' ', normalized_text).strip()

    # Multi-word skills first (order matters — longer phrases before substrings)
    for skill in sorted(SKILL_KEYWORDS, key=len, reverse=True):
        # Enhanced pattern matching for better accuracy
        skill_words = skill.split()
        if len(skill_words) > 1:
            # For multi-word skills, check if all words appear in sequence
            pattern = r'\b' + r'\s+'.join(map(re.escape, skill_words)) + r'\b'
            if re.search(pattern, normalized_text):
                found.add(skill)
        else:
            # For single-word skills, use word boundary
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, normalized_text):
                found.add(skill)

    # Skills containing symbols (c++, c#, node.js, next.js, tcp/ip, ci/cd) are
    # destroyed by the normalisation above, so match them on the original text.
    for skill in SKILL_KEYWORDS:
        if re.search(r'[+#./]', skill):
            pattern = r'(?<![\w+#.])' + re.escape(skill) + r'(?![\w+#])'
            if re.search(pattern, text_lower):
                found.add(skill)

    # Additional extraction for common abbreviations and variations
    abbreviations = {
        'js': 'javascript',
        'ts': 'typescript', 
        'py': 'python',
        'ml': 'machine learning',
        'ai': 'artificial intelligence',
        'dl': 'deep learning',
        'nlp': 'natural language processing',
        'cv': 'computer vision',
        'ui': 'ui design',
        'ux': 'ux design',
        'qa': 'testing',
        'devops': 'devops',
        'ci': 'ci/cd',
        'cd': 'ci/cd',
        'rdbms': 'sql',
        'nosql': 'nosql',
        'saas': 'saas',
        'paas': 'paas',
        'iaas': 'iaas'
    }
    
    # Check for abbreviations
    for abbrev, full_skill in abbreviations.items():
        if re.search(r'\b' + re.escape(abbrev) + r'\b', normalized_text):
            if full_skill in SKILL_KEYWORDS:
                found.add(full_skill)

    return found


def parse_manual_input(raw: str) -> set:
    """
    Parse comma/newline-separated skill list typed by the user.
    Returns a set of normalized, matched skill strings.
    """
    if not raw:
        return set()

    # Split by commas, newlines, semicolons
    parts = re.split(r'[,\n;]+', raw)
    entered = {p.strip().lower() for p in parts if p.strip()}

    # Fuzzy-match against known skills
    matched = set()
    for entry in entered:
        if entry in SKILL_KEYWORDS:
            matched.add(entry)
        else:
            # Try partial match
            for skill in SKILL_KEYWORDS:
                if entry in skill or skill in entry:
                    matched.add(skill)
                    break
            else:
                # Accept as-is if not matched (user may have niche skills)
                matched.add(entry)

    return matched


def try_ocr_extract(image_path: str) -> tuple[set, bool]:
    """
    Try to extract skills from a resume image using pytesseract OCR.
    Returns (skills_set, ocr_success).
    If OCR fails, returns (empty_set, False).
    """
    try:
        import pytesseract
        from PIL import Image
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        skills = extract_skills_from_text(text)
        return skills, True
    except Exception:
        return set(), False


def try_pdf_extract(pdf_path: str) -> tuple[set, bool]:
    """
    Extract skills from a PDF resume using enhanced text extraction.
    Returns (skills_set, parse_success).
    """
    try:
        from pypdf import PdfReader

        reader = PdfReader(pdf_path)
        text_chunks = []
        
        # Extract text from all pages with better error handling
        for page_num, page in enumerate(reader.pages):
            try:
                page_text = page.extract_text() or ""
                if page_text.strip():
                    text_chunks.append(page_text)
            except Exception as e:
                print(f"Warning: Could not extract text from page {page_num}: {e}")
                continue
        
        full_text = "\n".join(text_chunks).strip()
        
        if not full_text:
            return set(), False
            
        # Additional text cleaning and normalization
        # Remove common PDF artifacts
        cleaned_text = re.sub(r'\f', '\n', full_text)  # Form feed to newline
        cleaned_text = re.sub(r'\x00', '', cleaned_text)  # Null bytes
        cleaned_text = re.sub(r'[^\w\s\-\.\,\;\:\!\?\(\)\[\]\{\}\"\'\/\\]', ' ', cleaned_text)
        
        # Extract skills using the enhanced function
        skills = extract_skills_from_text(cleaned_text)
        
        # Log extraction results for debugging
        print(f"PDF extraction successful. Found {len(skills)} skills from {len(text_chunks)} pages")
        if skills:
            print(f"Skills found: {', '.join(sorted(skills))}")
        
        return skills, True
        
    except Exception as e:
        print(f"PDF extraction failed: {e}")
        return set(), False

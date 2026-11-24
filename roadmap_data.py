# roadmap_data.py — Learning resources for every skill

ROADMAP = {
    # Programming Languages
    "python": {
        "label": "Python",
        "resources": [
            {"title": "Python Official Docs", "url": "https://docs.python.org/3/tutorial/"},
            {"title": "CS50P – Harvard Python Course", "url": "https://cs50.harvard.edu/python/"},
            {"title": "Automate the Boring Stuff", "url": "https://automatetheboringstuff.com/"},
        ],
        "certifications": [
            {"title": "Google Python Certificate", "url": "https://www.coursera.org/professional-certificates/google-automation", "provider": "Google", "duration": "6 months"},
            {"title": "Python for Everybody (Free)", "url": "https://www.coursera.org/specializations/python", "provider": "University of Michigan", "duration": "3 months"},
            {"title": "IBM Python Certification", "url": "https://www.coursera.org/professional-certificates/ibm-data-science", "provider": "IBM", "duration": "6 months"}
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Programming Language"
    },
    "java": {
        "label": "Java",
        "resources": [
            {"title": "Java Tutorial – W3Schools", "url": "https://www.w3schools.com/java/"},
            {"title": "Java Programming – MOOC.fi", "url": "https://java-programming.mooc.fi/"},
        ],
        "certifications": [
            {"title": "Oracle Java Certification", "url": "https://education.oracle.com/java-se-11-developer", "provider": "Oracle", "duration": "2-3 months"},
            {"title": "Java Programming (Free)", "url": "https://www.edx.org/learn/java", "provider": "edX", "duration": "4 months"},
            {"title": "Core Java (Free)", "url": "https://www.udemy.com/course/core-java/", "provider": "Udemy", "duration": "6 weeks"}
        ],
        "fast": "3 weeks", "moderate": "6 weeks", "slow": "3 months",
        "category": "Programming Language"
    },
    "javascript": {
        "label": "JavaScript",
        "resources": [
            {"title": "JavaScript.info", "url": "https://javascript.info/"},
            {"title": "freeCodeCamp JS", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"},
        ],
        "certifications": [
            {"title": "freeCodeCamp JavaScript Certification", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "provider": "freeCodeCamp", "duration": "300 hours"},
            {"title": "JavaScript Algorithms (Free)", "url": "https://www.udemy.com/course/javascript-algorithms-and-data-structures/", "provider": "Udemy", "duration": "9 hours"},
            {"title": "Meta Front-End Developer", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer", "provider": "Meta", "duration": "7 months"}
        ],
        "fast": "3 weeks", "moderate": "6 weeks", "slow": "3 months",
        "category": "Programming Language"
    },
    "c++": {
        "label": "C++",
        "resources": [
            {"title": "LearnCpp.com", "url": "https://www.learncpp.com/"},
            {"title": "C++ Reference", "url": "https://cppreference.com/"},
        ],
        "fast": "3 weeks", "moderate": "6 weeks", "slow": "2 months",
        "category": "Programming Language"
    },
    "go": {
        "label": "Go (Golang)",
        "resources": [
            {"title": "Tour of Go", "url": "https://go.dev/tour/"},
            {"title": "Go by Example", "url": "https://gobyexample.com/"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Programming Language"
    },

    # Web Development
    "html": {
        "label": "HTML",
        "resources": [
            {"title": "MDN HTML Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML"},
            {"title": "W3Schools HTML", "url": "https://www.w3schools.com/html/"},
        ],
        "certifications": [
            {"title": "HTML Responsive Web Design (Free)", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "provider": "freeCodeCamp", "duration": "300 hours"},
            {"title": "HTML5 & CSS3 (Free)", "url": "https://www.udemy.com/course/html-css-javascript/", "provider": "Udemy", "duration": "15 hours"},
            {"title": "Front-End Web Development", "url": "https://www.edx.org/learn/front-end-web-development", "provider": "edX", "duration": "5 months"}
        ],
        "fast": "3 days", "moderate": "1 week", "slow": "2 weeks",
        "category": "Web Development"
    },
    "css": {
        "label": "CSS",
        "resources": [
            {"title": "MDN CSS Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS"},
            {"title": "CSS-Tricks", "url": "https://css-tricks.com/"},
        ],
        "certifications": [
            {"title": "CSS Certification (Free)", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "provider": "freeCodeCamp", "duration": "300 hours"},
            {"title": "Advanced CSS (Free)", "url": "https://www.udemy.com/course/advanced-css-and-sass/", "provider": "Udemy", "duration": "13 hours"},
            {"title": "Web Design for Everybody", "url": "https://www.coursera.org/specializations/web-design", "provider": "University of Michigan", "duration": "5 months"}
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Web Development"
    },
    "react": {
        "label": "React",
        "resources": [
            {"title": "React Official Tutorial", "url": "https://reactjs.org/tutorial/tutorial.html"},
            {"title": "React Docs", "url": "https://reactjs.org/docs/getting-started.html"},
        ],
        "certifications": [
            {"title": "Meta React Certification", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer", "provider": "Meta", "duration": "7 months"},
            {"title": "React - The Complete Guide", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "provider": "Udemy", "duration": "48 hours"},
            {"title": "React JS (Free)", "url": "https://www.edx.org/learn/react", "provider": "edX", "duration": "4 months"}
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Web Development"
    },
    "node.js": {
        "label": "Node.js",
        "resources": [
            {"title": "Node.js Official Docs", "url": "https://nodejs.org/en/docs/"},
            {"title": "The Odin Project – Node", "url": "https://www.theodinproject.com/paths/full-stack-javascript/courses/nodejs"},
        ],
        "certifications": [
            {"title": "Node.js Certification (Free)", "url": "https://www.freecodecamp.org/learn/back-end-development-and-apis/", "provider": "freeCodeCamp", "duration": "300 hours"},
            {"title": "Node.js - The Complete Guide", "url": "https://www.udemy.com/course/nodejs-the-complete-guide/", "provider": "Udemy", "duration": "27 hours"},
            {"title": "IBM Full Stack Developer", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer", "provider": "IBM", "duration": "12 months"}
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Web Development"
    },
    "flask": {
        "label": "Flask",
        "resources": [
            {"title": "Flask Official Docs", "url": "https://flask.palletsprojects.com/"},
            {"title": "Corey Schafer Flask Tutorial", "url": "https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH"},
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Web Development"
    },
    "django": {
        "label": "Django",
        "resources": [
            {"title": "Django Official Docs", "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/"},
            {"title": "Django for Beginners", "url": "https://djangoforbeginners.com/"},
        ],
        "fast": "3 weeks", "moderate": "2 months", "slow": "3 months",
        "category": "Web Development"
    },
    "rest api": {
        "label": "REST API Design",
        "resources": [
            {"title": "REST API Tutorial", "url": "https://restfulapi.net/"},
            {"title": "Postman Learning Center", "url": "https://learning.postman.com/"},
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Web Development"
    },

    # Databases
    "sql": {
        "label": "SQL",
        "resources": [
            {"title": "SQLZoo", "url": "https://sqlzoo.net/"},
            {"title": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "1 month",
        "category": "Database"
    },
    "mysql": {
        "label": "MySQL",
        "resources": [
            {"title": "MySQL Official Tutorial", "url": "https://dev.mysql.com/doc/refman/8.0/en/tutorial.html"},
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Database"
    },
    "mongodb": {
        "label": "MongoDB",
        "resources": [
            {"title": "MongoDB University", "url": "https://learn.mongodb.com/"},
            {"title": "MongoDB Docs", "url": "https://www.mongodb.com/docs/manual/tutorial/"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "2 months",
        "category": "Database"
    },
    "postgresql": {
        "label": "PostgreSQL",
        "resources": [
            {"title": "PostgreSQL Tutorial", "url": "https://www.postgresqltutorial.com/"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "2 months",
        "category": "Database"
    },

    # Cloud & DevOps
    "aws": {
        "label": "AWS",
        "resources": [
            {"title": "AWS Free Tier + Tutorials", "url": "https://aws.amazon.com/getting-started/"},
            {"title": "AWS Skill Builder", "url": "https://skillbuilder.aws/"},
        ],
        "certifications": [
            {"title": "AWS Cloud Practitioner (Free)", "url": "https://aws.amazon.com/certification/certified-cloud-practitioner/", "provider": "Amazon Web Services", "duration": "1-2 months"},
            {"title": "AWS Solutions Architect", "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/", "provider": "Amazon Web Services", "duration": "3-4 months"},
            {"title": "AWS Developer Associate", "url": "https://aws.amazon.com/certification/certified-developer-associate/", "provider": "Amazon Web Services", "duration": "2-3 months"}
        ],
        "fast": "1 month", "moderate": "3 months", "slow": "6 months",
        "category": "Cloud / DevOps"
    },
    "azure": {
        "label": "Microsoft Azure",
        "resources": [
            {"title": "Microsoft Learn – Azure", "url": "https://learn.microsoft.com/en-us/training/azure/"},
        ],
        "certifications": [
            {"title": "Azure Fundamentals (Free)", "url": "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/", "provider": "Microsoft", "duration": "1 month"},
            {"title": "Azure Developer Associate", "url": "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-204/", "provider": "Microsoft", "duration": "2-3 months"},
            {"title": "Azure Solutions Architect", "url": "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-305/", "provider": "Microsoft", "duration": "3-4 months"}
        ],
        "fast": "1 month", "moderate": "3 months", "slow": "6 months",
        "category": "Cloud / DevOps"
    },
    "gcp": {
        "label": "Google Cloud Platform",
        "resources": [
            {"title": "Google Cloud Skills Boost", "url": "https://cloudskillsboost.google/"},
        ],
        "fast": "1 month", "moderate": "3 months", "slow": "6 months",
        "category": "Cloud / DevOps"
    },
    "docker": {
        "label": "Docker",
        "resources": [
            {"title": "Docker Getting Started", "url": "https://docs.docker.com/get-started/"},
            {"title": "Play With Docker", "url": "https://labs.play-with-docker.com/"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "1 month",
        "category": "Cloud / DevOps"
    },
    "kubernetes": {
        "label": "Kubernetes",
        "resources": [
            {"title": "Kubernetes Official Docs", "url": "https://kubernetes.io/docs/tutorials/"},
            {"title": "Kubernetes by Example", "url": "https://kubernetesbyexample.com/"},
        ],
        "fast": "1 month", "moderate": "2 months", "slow": "4 months",
        "category": "Cloud / DevOps"
    },
    "ci/cd": {
        "label": "CI/CD Pipelines",
        "resources": [
            {"title": "GitHub Actions Docs", "url": "https://docs.github.com/en/actions"},
            {"title": "Jenkins Tutorial", "url": "https://www.jenkins.io/doc/tutorials/"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "1 month",
        "category": "Cloud / DevOps"
    },
    "linux": {
        "label": "Linux / Shell Scripting",
        "resources": [
            {"title": "Linux Journey", "url": "https://linuxjourney.com/"},
            {"title": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "2 months",
        "category": "Cloud / DevOps"
    },

    # Data Science & ML
    "machine learning": {
        "label": "Machine Learning",
        "resources": [
            {"title": "Andrew Ng – ML Specialization", "url": "https://www.coursera.org/specializations/machine-learning-introduction"},
            {"title": "fast.ai", "url": "https://www.fast.ai/"},
        ],
        "fast": "2 months", "moderate": "4 months", "slow": "6 months",
        "category": "Data Science / ML"
    },
    "deep learning": {
        "label": "Deep Learning",
        "resources": [
            {"title": "Deep Learning Specialization – Coursera", "url": "https://www.coursera.org/specializations/deep-learning"},
            {"title": "fast.ai DL", "url": "https://course.fast.ai/"},
        ],
        "fast": "2 months", "moderate": "4 months", "slow": "6 months",
        "category": "Data Science / ML"
    },
    "data analysis": {
        "label": "Data Analysis",
        "resources": [
            {"title": "Kaggle – Data Analysis", "url": "https://www.kaggle.com/learn/pandas"},
            {"title": "Pandas Docs", "url": "https://pandas.pydata.org/docs/getting_started/index.html"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Data Science / ML"
    },
    "pandas": {
        "label": "Pandas",
        "resources": [
            {"title": "Pandas Getting Started", "url": "https://pandas.pydata.org/docs/getting_started/"},
            {"title": "Kaggle Pandas Course", "url": "https://www.kaggle.com/learn/pandas"},
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Data Science / ML"
    },
    "numpy": {
        "label": "NumPy",
        "resources": [
            {"title": "NumPy Official Docs", "url": "https://numpy.org/doc/stable/user/quickstart.html"},
        ],
        "fast": "3 days", "moderate": "1 week", "slow": "2 weeks",
        "category": "Data Science / ML"
    },
    "tensorflow": {
        "label": "TensorFlow",
        "resources": [
            {"title": "TensorFlow Official Tutorials", "url": "https://www.tensorflow.org/tutorials"},
        ],
        "fast": "1 month", "moderate": "2 months", "slow": "4 months",
        "category": "Data Science / ML"
    },
    "nlp": {
        "label": "Natural Language Processing",
        "resources": [
            {"title": "HuggingFace NLP Course", "url": "https://huggingface.co/learn/nlp-course/"},
            {"title": "Stanford NLP", "url": "https://web.stanford.edu/class/cs224n/"},
        ],
        "fast": "1 month", "moderate": "3 months", "slow": "6 months",
        "category": "Data Science / ML"
    },

    # Core CS
    "data structures": {
        "label": "Data Structures & Algorithms",
        "resources": [
            {"title": "LeetCode – DSA", "url": "https://leetcode.com/explore/"},
            {"title": "Neetcode.io", "url": "https://neetcode.io/roadmap"},
            {"title": "GeeksForGeeks DSA", "url": "https://www.geeksforgeeks.org/data-structures/"},
        ],
        "fast": "1 month", "moderate": "2 months", "slow": "4 months",
        "category": "Core CS"
    },
    "algorithms": {
        "label": "Algorithms",
        "resources": [
            {"title": "Algorithms – Princeton (Coursera)", "url": "https://www.coursera.org/learn/algorithms-part1"},
            {"title": "VisuAlgo", "url": "https://visualgo.net/"},
        ],
        "fast": "1 month", "moderate": "2 months", "slow": "4 months",
        "category": "Core CS"
    },
    "system design": {
        "label": "System Design",
        "resources": [
            {"title": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer"},
            {"title": "Grokking System Design", "url": "https://www.educative.io/courses/grokking-modern-system-design-interview"},
        ],
        "fast": "1 month", "moderate": "2 months", "slow": "6 months",
        "category": "Core CS"
    },
    "os concepts": {
        "label": "Operating Systems",
        "resources": [
            {"title": "OS Concepts – Studytonight", "url": "https://www.studytonight.com/operating-system/"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Core CS"
    },
    "networking": {
        "label": "Computer Networking",
        "resources": [
            {"title": "Computer Networking – Khan Academy", "url": "https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Core CS"
    },

    # Tools & Practices
    "git": {
        "label": "Git & GitHub",
        "resources": [
            {"title": "Git Official Book", "url": "https://git-scm.com/book/en/v2"},
            {"title": "Learn Git Branching", "url": "https://learngitbranching.js.org/"},
        ],
        "fast": "3 days", "moderate": "1 week", "slow": "2 weeks",
        "category": "Tools"
    },
    "agile": {
        "label": "Agile / Scrum",
        "resources": [
            {"title": "Scrum Guide", "url": "https://scrumguides.org/"},
        ],
        "fast": "2 days", "moderate": "1 week", "slow": "2 weeks",
        "category": "Tools"
    },
    "testing": {
        "label": "Software Testing",
        "resources": [
            {"title": "Testing Python – Real Python", "url": "https://realpython.com/python-testing/"},
            {"title": "ISTQB Foundation", "url": "https://www.istqb.org/certifications/certified-tester-foundation-level"},
        ],
        "fast": "1 week", "moderate": "3 weeks", "slow": "1 month",
        "category": "Tools"
    },
    "excel": {
        "label": "Microsoft Excel",
        "resources": [
            {"title": "Excel – GCFGlobal", "url": "https://edu.gcfglobal.org/en/excel2016/"},
        ],
        "fast": "1 week", "moderate": "2 weeks", "slow": "1 month",
        "category": "Tools"
    },
    "power bi": {
        "label": "Power BI",
        "resources": [
            {"title": "Microsoft Power BI Learning", "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Tools"
    },
    "tableau": {
        "label": "Tableau",
        "resources": [
            {"title": "Tableau Free Training", "url": "https://www.tableau.com/learn/training"},
        ],
        "fast": "2 weeks", "moderate": "1 month", "slow": "2 months",
        "category": "Tools"
    },
    "cybersecurity": {
        "label": "Cybersecurity Fundamentals",
        "resources": [
            {"title": "TryHackMe", "url": "https://tryhackme.com/"},
            {"title": "Google Cybersecurity Certificate", "url": "https://www.coursera.org/professional-certificates/google-cybersecurity"},
        ],
        "fast": "1 month", "moderate": "3 months", "slow": "6 months",
        "category": "Security"
    },
    "ethical hacking": {
        "label": "Ethical Hacking",
        "resources": [
            {"title": "Hack The Box", "url": "https://www.hackthebox.com/"},
            {"title": "CEH Course – EC-Council", "url": "https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/"},
        ],
        "fast": "2 months", "moderate": "4 months", "slow": "6 months",
        "category": "Security"
    },
    "communication": {
        "label": "Communication Skills",
        "resources": [
            {"title": "Coursera – Communication Skills", "url": "https://www.coursera.org/courses?query=communication+skills"},
        ],
        "fast": "Ongoing", "moderate": "Ongoing", "slow": "Ongoing",
        "category": "Soft Skills"
    },
    "problem solving": {
        "label": "Problem Solving",
        "resources": [
            {"title": "HackerRank – Problem Solving", "url": "https://www.hackerrank.com/domains/tutorials/10-days-of-javascript"},
            {"title": "LeetCode", "url": "https://leetcode.com/"},
        ],
        "fast": "Ongoing", "moderate": "Ongoing", "slow": "Ongoing",
        "category": "Soft Skills"
    },
}

def get_skill_info(skill_key):
    """Return roadmap info for a skill key (case-insensitive)."""
    return ROADMAP.get(skill_key.lower(), {
        "label": skill_key.title(),
        "resources": [
            {"title": f"Search on Google", "url": f"https://www.google.com/search?q=learn+{skill_key}"},
            {"title": f"YouTube Tutorial", "url": f"https://www.youtube.com/results?search_query=learn+{skill_key}+tutorial"},
        ],
        "fast": "Varies", "moderate": "Varies", "slow": "Varies",
        "category": "General"
    })

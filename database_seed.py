# database_seed.py — Company and role data for seeding the database

COMPANIES_DATA = {
    "TCS": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Tata_Consultancy_Services_Logo.svg/2560px-Tata_Consultancy_Services_Logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["python", "java", "javascript"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Systems Engineer", "skills": {"core": ["java", "c++", "data structures"], "good": ["linux", "sql"], "bonus": ["cloud", "devops"]}},
                {"role_name": "Graduate Engineer Trainee", "skills": {"core": ["python", "java", "data structures"], "good": ["sql", "git"], "bonus": ["communication", "teamwork"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "hadoop"], "bonus": ["aws", "etl"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "linux", "networking"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["linux", "docker", "jenkins"], "good": ["kubernetes", "terraform"], "bonus": ["aws", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Executive", "skills": {"core": ["communication", "english"], "good": ["ms office", "typing"], "bonus": ["customer service", "problem solving"]}},
                {"role_name": "Content Writer", "skills": {"core": ["writing", "english", "creativity"], "good": ["seo", "social media"], "bonus": ["research", "editing"]}},
                {"role_name": "Digital Marketing Executive", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}}
            ]
        }
    },
    "Infosys": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Infosys_logo.svg/2560px-Infosys_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Systems Engineer", "skills": {"core": ["c++", "java", "data structures"], "good": ["linux", "networking"], "bonus": ["cloud", "security"]}},
                {"role_name": "Programmer Analyst", "skills": {"core": ["python", "sql", "data analysis"], "good": ["excel", "visualization"], "bonus": ["machine learning", "statistics"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Test Engineer", "skills": {"core": ["testing", "automation", "java"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "UI/UX Designer", "skills": {"core": ["design", "figma", "prototyping"], "good": ["user research", "wireframing"], "bonus": ["css", "javascript"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "swift"], "good": ["react native", "flutter"], "bonus": ["android", "ios"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Executive", "skills": {"core": ["communication", "english"], "good": ["computer skills", "typing"], "bonus": ["customer service", "multitasking"]}},
                {"role_name": "Content Developer", "skills": {"core": ["writing", "content strategy", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Marketing Associate", "skills": {"core": ["marketing", "communication", "analytics"], "good": ["social media", "content"], "bonus": ["design", "research"]}}
            ]
        }
    },
    "Wipro": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Wipro_logo_2023.svg/2560px-Wipro_logo_2023.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Project Engineer", "skills": {"core": ["c++", "java", "data structures"], "good": ["project management", "testing"], "bonus": ["agile", "scrum"]}},
                {"role_name": "Systems Engineer", "skills": {"core": ["linux", "networking", "security"], "good": ["cloud", "devops"], "bonus": ["python", "automation"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Cloud Architect", "skills": {"core": ["aws", "azure", "architecture"], "good": ["devops", "security"], "bonus": ["kubernetes", "microservices"]}},
                {"role_name": "Automation Engineer", "skills": {"core": ["python", "automation", "testing"], "good": ["selenium", "jenkins"], "bonus": ["ci/cd", "docker"]}},
                {"role_name": "Embedded Systems Engineer", "skills": {"core": ["c", "c++", "embedded"], "good": ["microcontrollers", "iot"], "bonus": ["arduino", "raspberry pi"]}},
                {"role_name": "Network Engineer", "skills": {"core": ["networking", "security", "tcp/ip"], "good": ["firewall", "vpn"], "bonus": ["cisco", "routing"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Associate", "skills": {"core": ["process management", "communication"], "good": ["ms office", "data entry"], "bonus": ["quality control", "auditing"]}},
                {"role_name": "Technical Writer", "skills": {"core": ["technical writing", "documentation"], "good": ["api documentation", "user guides"], "bonus": ["markdown", "diagramming"]}},
                {"role_name": "Training Coordinator", "skills": {"core": ["training", "coordination", "communication"], "good": ["curriculum development", "presentation"], "bonus": ["e-learning", "lms"]}}
            ]
        }
    },
    "HCLTech": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HCLTech_logo.svg/2560px-HCLTech_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "azure"]}},
                {"role_name": "Systems Engineer", "skills": {"core": ["c++", "linux", "networking"], "good": ["cloud", "devops"], "bonus": ["security", "automation"]}},
                {"role_name": "Graduate Engineer Trainee", "skills": {"core": ["python", "java", "data structures"], "good": ["git", "testing"], "bonus": ["communication", "teamwork"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Security Engineer", "skills": {"core": ["cybersecurity", "networking", "linux"], "good": ["penetration testing", "firewall"], "bonus": ["ethical hacking", "compliance"]}},
                {"role_name": "Infrastructure Engineer", "skills": {"core": ["linux", "networking", "infrastructure"], "good": ["vmware", "storage"], "bonus": ["cloud", "automation"]}},
                {"role_name": "Test Automation Engineer", "skills": {"core": ["automation", "python", "testing"], "good": ["selenium", "jenkins"], "bonus": ["performance testing", "api testing"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Specialist", "skills": {"core": ["process management", "analysis"], "good": ["documentation", "quality"], "bonus": ["six sigma", "lean"]}},
                {"role_name": "HR Coordinator", "skills": {"core": ["hr coordination", "communication"], "good": ["recruitment", "onboarding"], "bonus": ["employee relations", "training"]}},
                {"role_name": "Content Specialist", "skills": {"core": ["content creation", "writing"], "good": ["seo", "social media"], "bonus": ["analytics", "design"]}}
            ]
        }
    },
    "Zoho": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Zoho_logo.svg/2560px-Zoho_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Developer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["node.js", "mongodb"]}},
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "react"], "good": ["node.js", "express"], "bonus": ["aws", "docker"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "swift"], "good": ["react native", "flutter"], "bonus": ["android", "ios"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["linux", "docker", "jenkins"], "good": ["kubernetes", "terraform"], "bonus": ["aws", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Writer", "skills": {"core": ["writing", "english", "creativity"], "good": ["seo", "social media"], "bonus": ["research", "editing"]}},
                {"role_name": "Digital Marketing Executive", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "strategy"], "good": ["user research", "analytics"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Freshworks": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Freshworks_logo.svg/2560px-Freshworks_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "react"], "good": ["node.js", "express"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["linux", "docker", "jenkins"], "good": ["kubernetes", "terraform"], "bonus": ["aws", "ci/cd"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Security Engineer", "skills": {"core": ["cybersecurity", "networking", "linux"], "good": ["penetration testing", "firewall"], "bonus": ["ethical hacking", "compliance"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Technical Writer", "skills": {"core": ["technical writing", "documentation"], "good": ["api documentation", "user guides"], "bonus": ["markdown", "diagramming"]}},
                {"role_name": "Content Strategist", "skills": {"core": ["content strategy", "writing"], "good": ["seo", "analytics"], "bonus": ["social media", "marketing"]}},
                {"role_name": "Marketing Associate", "skills": {"core": ["marketing", "communication", "analytics"], "good": ["social media", "content"], "bonus": ["design", "research"]}}
            ]
        }
    },
    "Flipkart": {
        "logo": "https://cdn-icons-png.flaticon.com/512/3177.png",
        "roles": {
            1: [
                {"role_name": "SDE 1 - Software Development Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "SDE 1 - Frontend", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "SDE 1 - Mobile", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "e-commerce"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["e-commerce", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Category Manager", "skills": {"core": ["category management", "e-commerce", "analytics"], "good": ["inventory management", "vendor relations"], "bonus": ["merchandising", "sales"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Supply Chain Analyst", "skills": {"core": ["supply chain", "logistics", "analytics"], "good": ["inventory planning", "demand forecasting"], "bonus": ["data analysis", "optimization"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "e-commerce", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Operations Manager", "skills": {"core": ["operations", "logistics", "management"], "good": ["supply chain", "coordination"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}}
            ]
        }
    },
    "Swiggy": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Swiggy_logo.svg/1200px-Swiggy_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "SDE 1 - Software Development Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "SDE 1 - Frontend", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "SDE 1 - Mobile", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "food-tech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["food-tech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Operations Manager", "skills": {"core": ["operations", "logistics", "management"], "good": ["supply chain", "coordination"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "City Manager", "skills": {"core": ["operations", "management", "coordination"], "good": ["logistics", "vendor management"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "food-tech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}}
            ]
        }
    },
    "Ola": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Ola_logo.svg/1200px-Ola_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Development Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Assurance Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "mobility-tech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "User Experience Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["mobility-tech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Operations Manager", "skills": {"core": ["operations", "logistics", "management"], "good": ["supply chain", "coordination"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "City General Manager", "skills": {"core": ["operations", "management", "coordination"], "good": ["logistics", "vendor management"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "mobility-tech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}}
            ]
        }
    },
    "Paytm": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Paytm_logo.svg/1200px-Paytm_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "SDE 1 - Software Development Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "SDE 1 - Frontend", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "SDE 1 - Mobile", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Backend Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["redis", "kafka"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Security Engineer", "skills": {"core": ["cybersecurity", "networking", "linux"], "good": ["penetration testing", "firewall"], "bonus": ["ethical hacking", "compliance"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "fintech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["fintech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Risk Analyst", "skills": {"core": ["risk management", "compliance", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "fintech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}},
                {"role_name": "Compliance Officer", "skills": {"core": ["compliance", "regulation", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "risk management"]}}
            ]
        }
    },
    "PhonePe": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/PhonePe_logo.svg/1200px-PhonePe_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "SDE 1 - Software Development Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "SDE 1 - Frontend", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "SDE 1 - Mobile", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Backend Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["redis", "kafka"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "QA Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Security Engineer", "skills": {"core": ["cybersecurity", "networking", "linux"], "good": ["penetration testing", "firewall"], "bonus": ["ethical hacking", "compliance"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "fintech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["fintech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Risk Analyst", "skills": {"core": ["risk management", "compliance", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "fintech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}},
                {"role_name": "Compliance Officer", "skills": {"core": ["compliance", "regulation", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "risk management"]}}
            ]
        }
    },
    "Byju's": {
        "logo": "https://byjus.com/wp-content/themes/byjus-2023/assets/images/byjus-logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Unacademy": {
        "logo": "https://static.uacdn.net/prod/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Vedantu": {
        "logo": "https://www.vedantu.com/cdn/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "WhiteHat Jr": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/WhiteHat_Jr_logo.svg/2560px-WhiteHat_Jr_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Toppr": {
        "logo": "https://www.toppr.com/assets/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Eruditus": {
        "logo": "https://www.eruditus.com/assets/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "UpGrad": {
        "logo": "https://www.upgrad.com/assets/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Simplilearn": {
        "logo": "https://www.simplilearn.com/assets/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "html", "css"], "good": ["react", "vue"], "bonus": ["typescript", "sass"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "QA Tester", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Business Analyst Trainee", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Content Developer", "skills": {"core": ["content development", "education", "writing"], "good": ["curriculum design", "research"], "bonus": ["e-learning", "video production"]}},
                {"role_name": "Educational Consultant", "skills": {"core": ["education", "consulting", "communication"], "good": ["curriculum development", "training"], "bonus": ["e-learning", "pedagogy"]}},
                {"role_name": "Product Manager", "skills": {"core": ["product management", "edtech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}}
            ]
        }
    },
    "Guvi": {
        "logo": "https://www.guvi.in/assets/images/logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Developer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Full Stack Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "kafka"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Frontend Developer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Backend Developer", "skills": {"core": ["python", "java", "sql"], "good": ["node.js", "express"], "bonus": ["redis", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Machine Learning Engineer", "skills": {"core": ["python", "machine learning", "sql"], "good": ["tensorflow", "spark"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Mobile Developer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}}
            ],
            2: [
                {"role_name": "Content Writer", "skills": {"core": ["writing", "english", "creativity"], "good": ["seo", "social media"], "bonus": ["research", "editing"]}},
                {"role_name": "Digital Marketing Executive", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "E-Learning Specialist", "skills": {"core": ["e-learning", "education", "content"], "good": ["curriculum development", "instructional design"], "bonus": ["lms", "video production"]}},
                {"role_name": "Technical Writer", "skills": {"core": ["technical writing", "documentation"], "good": ["api documentation", "user guides"], "bonus": ["markdown", "diagramming"]}}
            ]
        }
    },
    "Cognizant": {
        "logo": "https://www.cognizant.com/content/dam/cognizant-website/global/en/brand-logos/cognizant-logo.svg",
        "roles": {
            1: [
                {"role_name": "Associate Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Programmer Analyst Trainee", "skills": {"core": ["python", "sql", "data analysis"], "good": ["excel", "visualization"], "bonus": ["machine learning", "statistics"]}},
                {"role_name": "Systems Engineer", "skills": {"core": ["c++", "java", "data structures"], "good": ["linux", "networking"], "bonus": ["cloud", "security"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Automation Engineer", "skills": {"core": ["testing", "automation", "java"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "Full Stack Engineer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}}
            ],
            2: [
                {"role_name": "Associate Engineer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Business Analyst Associate", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Executive", "skills": {"core": ["communication", "english"], "good": ["computer skills", "typing"], "bonus": ["customer service", "multitasking"]}},
                {"role_name": "Content Writer", "skills": {"core": ["writing", "english", "creativity"], "good": ["seo", "social media"], "bonus": ["research", "editing"]}},
                {"role_name": "Digital Marketing Associate", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "Trainee Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Associate Software Engineer", "skills": {"core": ["python", "java", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Quality Analyst", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}}
            ]
        }
    },
    "Capgemini": {
        "logo": "https://www.capgemini.com/sites/default/files/2023-04/capgemini-logo.svg",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "data analysis", "sql"], "good": ["excel", "visualization"], "bonus": ["statistics", "reporting"]}},
                {"role_name": "Cloud Architect", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Test Analyst", "skills": {"core": ["testing", "automation", "java"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "SAP Consultant", "skills": {"core": ["sap", "abap", "sql"], "good": ["sap hana", "business processes"], "bonus": ["sap bw", "sap fi"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}}
            ],
            2: [
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Process Analyst", "skills": {"core": ["business analysis", "process mapping"], "good": ["documentation", "stakeholder management"], "bonus": ["six sigma", "lean"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "analytics", "social media"], "good": ["seo", "content strategy"], "bonus": ["design", "communication"]}},
                {"role_name": "Content Strategist", "skills": {"core": ["content strategy", "writing", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "HR Associate", "skills": {"core": ["hr coordination", "communication"], "good": ["recruitment", "onboarding"], "bonus": ["employee relations", "training"]}},
                {"role_name": "Trainee Software Engineer", "skills": {"core": ["python", "java", "sql"], "good": ["javascript", "react"], "bonus": ["aws", "docker"]}},
                {"role_name": "Quality Analyst", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Technical Writer", "skills": {"core": ["technical writing", "documentation"], "good": ["api documentation", "user guides"], "bonus": ["markdown", "diagramming"]}}
            ]
        }
    },
    "Tech Mahindra": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Tech_Mahindra_logo.svg/2560px-Tech_Mahindra_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Network Engineer", "skills": {"core": ["networking", "security", "tcp/ip"], "good": ["firewall", "vpn"], "bonus": ["cisco", "routing"]}},
                {"role_name": "Telecom Engineer", "skills": {"core": ["telecom", "5g", "network protocols"], "good": ["oss", "bss"], "bonus": ["lte", "voip"]}},
                {"role_name": "Data Engineer", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Test Engineer", "skills": {"core": ["testing", "automation", "java"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "System Administrator", "skills": {"core": ["linux", "windows", "networking"], "good": ["virtualization", "backup"], "bonus": ["security", "monitoring"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}}
            ],
            2: [
                {"role_name": "Associate Software Engineer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Associate", "skills": {"core": ["process management", "communication"], "good": ["ms office", "data entry"], "bonus": ["quality control", "auditing"]}},
                {"role_name": "Content Developer", "skills": {"core": ["writing", "content strategy", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Digital Marketing Associate", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "Network Associate", "skills": {"core": ["networking", "security", "tcp/ip"], "good": ["firewall", "vpn"], "bonus": ["cisco", "routing"]}},
                {"role_name": "Quality Analyst", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "HR Coordinator", "skills": {"core": ["hr coordination", "communication"], "good": ["recruitment", "onboarding"], "bonus": ["employee relations", "training"]}}
            ]
        }
    },
    "Accenture": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Accenture_logo.svg/2560px-Accenture_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineering Analyst", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Application Development Analyst", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Technology Consultant", "skills": {"core": ["consulting", "technology", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Data Engineering Analyst", "skills": {"core": ["python", "sql", "data structures"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}},
                {"role_name": "Cloud Engineering Analyst", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Test Analyst", "skills": {"core": ["testing", "automation", "java"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "SAP Consultant", "skills": {"core": ["sap", "abap", "sql"], "good": ["sap hana", "business processes"], "bonus": ["sap bw", "sap fi"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}}
            ],
            2: [
                {"role_name": "Associate Software Engineer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Process Executive", "skills": {"core": ["communication", "english"], "good": ["computer skills", "typing"], "bonus": ["customer service", "multitasking"]}},
                {"role_name": "Content Developer", "skills": {"core": ["writing", "content strategy", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Quality Analyst", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "HR Associate", "skills": {"core": ["hr coordination", "communication"], "good": ["recruitment", "onboarding"], "bonus": ["employee relations", "training"]}}
            ]
        }
    },
    "IBM": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/2560px-IBM_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Developer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Systems Administrator", "skills": {"core": ["linux", "unix", "networking"], "good": ["virtualization", "backup"], "bonus": ["security", "monitoring"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Cloud Engineer", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Mainframe Developer", "skills": {"core": ["cobol", "jcl", "db2"], "good": ["zos", "cics"], "bonus": ["pl/i", "assembly"]}},
                {"role_name": "AI Engineer", "skills": {"core": ["python", "machine learning", "ai"], "good": ["tensorflow", "pytorch"], "bonus": ["deep learning", "nlp"]}},
                {"role_name": "Quantum Computing Researcher", "skills": {"core": ["quantum computing", "python", "linear algebra"], "good": ["qiskit", "algorithms"], "bonus": ["physics", "mathematics"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}}
            ],
            2: [
                {"role_name": "Associate Software Developer", "skills": {"core": ["javascript", "python", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "mongodb"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Technical Support Engineer", "skills": {"core": ["technical support", "troubleshooting"], "good": ["customer service", "documentation"], "bonus": ["networking", "hardware"]}},
                {"role_name": "Content Developer", "skills": {"core": ["writing", "content strategy", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content writing"], "bonus": ["design", "communication"]}},
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Quality Analyst", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "HR Associate", "skills": {"core": ["hr coordination", "communication"], "good": ["recruitment", "onboarding"], "bonus": ["employee relations", "training"]}}
            ]
        }
    },
    "Deloitte": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Deloitte_logo.svg/2560px-Deloitte_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Technology Consultant", "skills": {"core": ["consulting", "technology", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Technology Analyst", "skills": {"core": ["business analysis", "technology", "consulting"], "good": ["requirements gathering", "documentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Data Analyst", "skills": {"core": ["data analysis", "sql", "excel"], "good": ["visualization", "statistics"], "bonus": ["python", "tableau"]}},
                {"role_name": "Cybersecurity Consultant", "skills": {"core": ["cybersecurity", "networking", "risk management"], "good": ["penetration testing", "compliance"], "bonus": ["security audit", "firewall"]}},
                {"role_name": "Cloud Consultant", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "ERP Consultant", "skills": {"core": ["sap", "oracle", "business processes"], "good": ["implementation", "configuration"], "bonus": ["project management", "training"]}},
                {"role_name": "Automation Engineer", "skills": {"core": ["automation", "python", "testing"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}}
            ],
            2: [
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Risk Advisory Associate", "skills": {"core": ["risk management", "compliance", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "reporting"]}},
                {"role_name": "Tax Technology Analyst", "skills": {"core": ["tax", "technology", "data analysis"], "good": ["excel", "automation"], "bonus": ["tax software", "compliance"]}},
                {"role_name": "Audit Associate", "skills": {"core": ["auditing", "accounting", "compliance"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "reporting"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content strategy"], "bonus": ["design", "communication"]}},
                {"role_name": "HR Analyst", "skills": {"core": ["hr analysis", "data", "communication"], "good": ["hr systems", "reporting"], "bonus": ["recruitment", "training"]}},
                {"role_name": "Financial Analyst", "skills": {"core": ["financial analysis", "excel", "accounting"], "good": ["modeling", "reporting"], "bonus": ["data visualization", "statistics"]}}
            ]
        }
    },
    "KPMG": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/KPMG_logo.svg/2560px-KPMG_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Technology Consultant", "skills": {"core": ["consulting", "technology", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Data Analyst", "skills": {"core": ["data analysis", "sql", "excel"], "good": ["visualization", "statistics"], "bonus": ["python", "tableau"]}},
                {"role_name": "Cybersecurity Analyst", "skills": {"core": ["cybersecurity", "risk management", "compliance"], "good": ["penetration testing", "audit"], "bonus": ["security audit", "firewall"]}},
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Cloud Consultant", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Risk Advisory Consultant", "skills": {"core": ["risk management", "compliance", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "reporting"]}},
                {"role_name": "Automation Engineer", "skills": {"core": ["automation", "python", "testing"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "nlp"]}}
            ],
            2: [
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Audit Associate", "skills": {"core": ["auditing", "accounting", "compliance"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "reporting"]}},
                {"role_name": "Tax Associate", "skills": {"core": ["tax", "accounting", "compliance"], "good": ["tax software", "documentation"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Advisory Associate", "skills": {"core": ["business advisory", "analysis", "communication"], "good": ["presentation", "documentation"], "bonus": ["project management", "consulting"]}},
                {"role_name": "Financial Analyst", "skills": {"core": ["financial analysis", "excel", "accounting"], "good": ["modeling", "reporting"], "bonus": ["data visualization", "statistics"]}},
                {"role_name": "Risk Analyst", "skills": {"core": ["risk analysis", "compliance", "audit"], "good": ["documentation", "reporting"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content strategy"], "bonus": ["design", "communication"]}}
            ]
        }
    },
    "EY": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/EY_logo_2019.svg/2560px-EY_logo_2019.svg.png",
        "roles": {
            1: [
                {"role_name": "Technology Consultant", "skills": {"core": ["consulting", "technology", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Data Analyst", "skills": {"core": ["data analysis", "sql", "excel"], "good": ["visualization", "statistics"], "bonus": ["python", "tableau"]}},
                {"role_name": "Cybersecurity Consultant", "skills": {"core": ["cybersecurity", "risk management", "compliance"], "good": ["penetration testing", "audit"], "bonus": ["security audit", "firewall"]}},
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["javascript", "spring"], "bonus": ["aws", "devops"]}},
                {"role_name": "Cloud Consultant", "skills": {"core": ["aws", "azure", "python"], "good": ["devops", "docker"], "bonus": ["kubernetes", "terraform"]}},
                {"role_name": "Blockchain Consultant", "skills": {"core": ["blockchain", "smart contracts", "cryptography"], "good": ["solidity", "web3"], "bonus": ["ethereum", "defi"]}},
                {"role_name": "Automation Engineer", "skills": {"core": ["automation", "python", "testing"], "good": ["selenium", "junit"], "bonus": ["performance testing", "api testing"]}},
                {"role_name": "AI Consultant", "skills": {"core": ["ai", "machine learning", "python"], "good": ["tensorflow", "pytorch"], "bonus": ["deep learning", "nlp"]}}
            ],
            2: [
                {"role_name": "Associate Consultant", "skills": {"core": ["consulting", "communication", "problem solving"], "good": ["business analysis", "presentation"], "bonus": ["project management", "agile"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Audit Associate", "skills": {"core": ["auditing", "accounting", "compliance"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "reporting"]}},
                {"role_name": "Tax Consultant", "skills": {"core": ["tax", "accounting", "compliance"], "good": ["tax software", "documentation"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Advisory Associate", "skills": {"core": ["business advisory", "analysis", "communication"], "good": ["presentation", "documentation"], "bonus": ["project management", "consulting"]}},
                {"role_name": "Financial Analyst", "skills": {"core": ["financial analysis", "excel", "accounting"], "good": ["modeling", "reporting"], "bonus": ["data visualization", "statistics"]}},
                {"role_name": "Risk Analyst", "skills": {"core": ["risk analysis", "compliance", "audit"], "good": ["documentation", "reporting"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Digital Marketing Analyst", "skills": {"core": ["marketing", "social media", "analytics"], "good": ["seo", "content strategy"], "bonus": ["design", "communication"]}}
            ]
        }
    },
    "Myntra": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Myntra_logo.svg/2560px-Myntra_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}},
                {"role_name": "Analytics Engineer", "skills": {"core": ["python", "sql", "data analysis"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "e-commerce"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["e-commerce", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "e-commerce", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Category Manager", "skills": {"core": ["category management", "e-commerce", "analytics"], "good": ["inventory management", "vendor relations"], "bonus": ["merchandising", "sales"]}},
                {"role_name": "Fashion Merchandiser", "skills": {"core": ["fashion", "merchandising", "trends"], "good": ["inventory planning", "visual merchandising"], "bonus": ["analytics", "marketing"]}},
                {"role_name": "Content Creator", "skills": {"core": ["content creation", "writing", "photography"], "good": ["social media", "video editing"], "bonus": ["fashion", "styling"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}}
            ]
        }
    },
    "Nykaa": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Nykaa_logo.svg/2560px-Nykaa_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}},
                {"role_name": "Analytics Engineer", "skills": {"core": ["python", "sql", "data analysis"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "e-commerce"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["e-commerce", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "e-commerce", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Category Manager", "skills": {"core": ["category management", "e-commerce", "analytics"], "good": ["inventory management", "vendor relations"], "bonus": ["merchandising", "sales"]}},
                {"role_name": "Beauty Merchandiser", "skills": {"core": ["beauty", "merchandising", "trends"], "good": ["inventory planning", "visual merchandising"], "bonus": ["analytics", "marketing"]}},
                {"role_name": "Content Creator", "skills": {"core": ["content creation", "writing", "photography"], "good": ["social media", "video editing"], "bonus": ["beauty", "styling"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}}
            ]
        }
    },
    "BigBasket": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/BigBasket_logo.svg/2560px-BigBasket_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}},
                {"role_name": "Analytics Engineer", "skills": {"core": ["python", "sql", "data analysis"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "e-commerce"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["e-commerce", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "e-commerce", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Category Manager", "skills": {"core": ["category management", "e-commerce", "analytics"], "good": ["inventory management", "vendor relations"], "bonus": ["merchandising", "sales"]}},
                {"role_name": "Supply Chain Analyst", "skills": {"core": ["supply chain", "logistics", "analytics"], "good": ["inventory planning", "demand forecasting"], "bonus": ["data analysis", "optimization"]}},
                {"role_name": "Operations Manager", "skills": {"core": ["operations", "logistics", "management"], "good": ["supply chain", "coordination"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Customer Experience Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}}
            ]
        }
    },
    "Zomato": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Zomato_logo.svg/2560px-Zomato_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Product Engineer", "skills": {"core": ["python", "javascript", "sql"], "good": ["react", "node.js"], "bonus": ["aws", "docker"]}},
                {"role_name": "Data Scientist", "skills": {"core": ["python", "machine learning", "statistics"], "good": ["tensorflow", "pandas"], "bonus": ["deep learning", "recommendation systems"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}},
                {"role_name": "Analytics Engineer", "skills": {"core": ["python", "sql", "data analysis"], "good": ["spark", "aws"], "bonus": ["airflow", "etl"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "food-tech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["food-tech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "food-tech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Operations Manager", "skills": {"core": ["operations", "logistics", "management"], "good": ["supply chain", "coordination"], "bonus": ["analytics", "problem solving"]}},
                {"role_name": "Customer Success Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Content Manager", "skills": {"core": ["content management", "writing", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}}
            ]
        }
    },
    "Razorpay": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Razorpay_logo.svg/2560px-Razorpay_logo.svg.png",
        "roles": {
            1: [
                {"role_name": "Software Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["aws", "redis"]}},
                {"role_name": "Backend Engineer", "skills": {"core": ["java", "python", "sql"], "good": ["spring", "microservices"], "bonus": ["redis", "kafka"]}},
                {"role_name": "Frontend Engineer", "skills": {"core": ["javascript", "react", "html"], "good": ["css", "typescript"], "bonus": ["performance", "optimization"]}},
                {"role_name": "Mobile Engineer", "skills": {"core": ["java", "kotlin", "android"], "good": ["react native", "flutter"], "bonus": ["performance", "security"]}},
                {"role_name": "DevOps Engineer", "skills": {"core": ["aws", "linux", "devops"], "good": ["kubernetes", "docker"], "bonus": ["monitoring", "ci/cd"]}},
                {"role_name": "Quality Engineer", "skills": {"core": ["testing", "automation", "python"], "good": ["selenium", "junit"], "bonus": ["performance testing", "security"]}},
                {"role_name": "Platform Engineer", "skills": {"core": ["python", "java", "microservices"], "good": ["spring", "kafka"], "bonus": ["aws", "redis"]}},
                {"role_name": "Security Engineer", "skills": {"core": ["cybersecurity", "networking", "linux"], "good": ["penetration testing", "firewall"], "bonus": ["ethical hacking", "compliance"]}}
            ],
            2: [
                {"role_name": "Product Manager", "skills": {"core": ["product management", "fintech"], "good": ["analytics", "user research"], "bonus": ["agile", "scrum"]}},
                {"role_name": "UX Designer", "skills": {"core": ["design", "user research", "prototyping"], "good": ["fintech", "wireframing"], "bonus": ["usability testing", "interaction design"]}},
                {"role_name": "Marketing Manager", "skills": {"core": ["marketing", "fintech", "analytics"], "good": ["digital marketing", "branding"], "bonus": ["social media", "content"]}},
                {"role_name": "Business Analyst", "skills": {"core": ["business analysis", "communication"], "good": ["requirements gathering", "documentation"], "bonus": ["sql", "data analysis"]}},
                {"role_name": "Risk Analyst", "skills": {"core": ["risk management", "compliance", "audit"], "good": ["documentation", "analysis"], "bonus": ["financial analysis", "regulation"]}},
                {"role_name": "Customer Success Manager", "skills": {"core": ["customer service", "communication"], "good": ["relationship management", "problem solving"], "bonus": ["product knowledge", "sales"]}},
                {"role_name": "Content Manager", "skills": {"core": ["content management", "writing", "seo"], "good": ["social media", "analytics"], "bonus": ["design", "video editing"]}},
                {"role_name": "Sales Associate", "skills": {"core": ["sales", "communication", "negotiation"], "good": ["customer service", "relationship building"], "bonus": ["product knowledge", "analytics"]}}
            ]
        }
    },
}

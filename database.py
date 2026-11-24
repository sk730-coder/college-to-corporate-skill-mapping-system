import pymysql
import pymysql.cursors
import os
import calendar
import copy
import re

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ─── MySQL connection settings ───────────────────────────────────────────────
# Override with environment variables (or a .env file loaded by your shell).
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "skills_db"),
    "charset": "utf8mb4",
}

# ─── Skill sets per role ─────────────────────────────────────────────────────

# ─── Updated Skill sets per role with Stream Logic ─────────────────────────

# STREAMS: 1 = Engineering, 2 = Arts & Science

COMPANIES_DATA = {
    "TCS": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Tata_Consultancy_Services_Logo.svg/2000px-Tata_Consultancy_Services_Logo.svg.png",
        "roles": [
            {
                "name": "Assistant System Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Digital Engineer Trainee",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            },
            {
                "name": "BPO Associate",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Infosys": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Infosys_logo.svg/2000px-Infosys_logo.svg.png",
        "roles": [
            {
                "name": "Systems Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Specialist Programmer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            },
            {
                "name": "BPO Process Executive",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Cognizant": {
        "logo": "https://www.cognizant.com/content/dam/cognizant_dotcom/en_us/dotcom/logos/cognizant-logo.svg",
        "roles": [
            {
                "name": "Programmer Analyst",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "GenC Next Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            },
            {
                "name": "Digital Marketing Executive",
                "stream": 2,
                "skills": {
                    "core": [
                        "seo",
                        "content writing",
                        "social media strategy",
                        "google ads"
                    ],
                    "good": [
                        "analytics",
                        "market research",
                        "communication"
                    ],
                    "bonus": [
                        "email marketing",
                        "branding",
                        "growth hacking"
                    ]
                }
            }
        ]
    },
    "HCLTech": {
        "logo": "https://www.hcltech.com/themes/custom/hcltech/logo.svg",
        "roles": [
            {
                "name": "Graduate Engineer Trainee",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Network Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            },
            {
                "name": "Process Associate",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Zoho": {
        "logo": "https://www.zoho.com/sites/default/files/zoho-logo-500px.png",
        "roles": [
            {
                "name": "Software Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "UI/UX Designer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            },
            {
                "name": "Content Writer",
                "stream": 2,
                "skills": {
                    "core": [
                        "seo",
                        "content writing",
                        "social media strategy",
                        "google ads"
                    ],
                    "good": [
                        "analytics",
                        "market research",
                        "communication"
                    ],
                    "bonus": [
                        "email marketing",
                        "branding",
                        "growth hacking"
                    ]
                }
            },
            {
                "name": "HR Generalist",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Freshworks": {
        "logo": "https://www.freshworks.com/static/freshworks/images/general/logos/freshworks-logo.png",
        "roles": [
            {
                "name": "Product Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Sales Development Rep",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Chargebee": {
        "logo": "https://avatars.githubusercontent.com/u/1523420?s=200&v=4",
        "roles": [
            {
                "name": "SaaS Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Billing Analyst",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Guvi": {
        "logo": "https://www.guvi.in/blog/wp-content/uploads/2022/10/Guvi-logo.png",
        "roles": [
            {
                "name": "Full Stack Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            },
            {
                "name": "E-Learning Specialist",
                "stream": 2,
                "skills": {
                    "core": [
                        "seo",
                        "content writing",
                        "social media strategy",
                        "google ads"
                    ],
                    "good": [
                        "analytics",
                        "market research",
                        "communication"
                    ],
                    "bonus": [
                        "email marketing",
                        "branding",
                        "growth hacking"
                    ]
                }
            }
        ]
    },
    "CONTUS Tech": {
        "logo": "https://www.contus.com/img/contus-logo.svg",
        "roles": [
            {
                "name": "Frontend Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            },
            {
                "name": "DevOps Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            }
        ]
    },
    "Aspire Systems": {
        "logo": "https://www.aspiresys.com/wp-content/uploads/2021/01/aspire-logo.png",
        "roles": [
            {
                "name": "Trainee Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "QA Automation Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "selenium",
                        "java",
                        "manual testing",
                        "test planning",
                        "git"
                    ],
                    "good": [
                        "testng",
                        "cucumber",
                        "sql",
                        "api testing"
                    ],
                    "bonus": [
                        "appium",
                        "performance testing",
                        "jmeter"
                    ]
                }
            }
        ]
    },
    "Ramco Systems": {
        "logo": "https://www.ramco.com/hubfs/Ramco_Logo_New.png",
        "roles": [
            {
                "name": "ERP Consultant",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Product Implementation Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            }
        ]
    },
    "Google": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/2000px-Google_2015_logo.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Site Reliability Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            },
            {
                "name": "Product Manager Trainee",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Microsoft": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/2000px-Microsoft_logo.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Cloud Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            }
        ]
    },
    "Amazon": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/2000px-Amazon_logo.svg.png",
        "roles": [
            {
                "name": "SDE-1",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Data Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "python",
                        "sql",
                        "pandas",
                        "statistics",
                        "git",
                        "data modeling"
                    ],
                    "good": [
                        "spark",
                        "airflow",
                        "tableau",
                        "power bi"
                    ],
                    "bonus": [
                        "machine learning",
                        "deep learning",
                        "redshift"
                    ]
                }
            }
        ]
    },
    "Flipkart": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/8/89/Flipkart_logo.svg/1200px-Flipkart_logo.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Supply Chain Analyst",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "PhonePe": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/PhonePe_Logo.svg/1200px-PhonePe_Logo.svg.png",
        "roles": [
            {
                "name": "SDE-1",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Security Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            }
        ]
    },
    "Razorpay": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/8/89/Razorpay_logo.svg/1200px-Razorpay_logo.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Product Analyst",
                "stream": 2,
                "skills": {
                    "core": [
                        "seo",
                        "content writing",
                        "social media strategy",
                        "google ads"
                    ],
                    "good": [
                        "analytics",
                        "market research",
                        "communication"
                    ],
                    "bonus": [
                        "email marketing",
                        "branding",
                        "growth hacking"
                    ]
                }
            }
        ]
    },
    "Cisco": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Cisco_logo_blue_2016.svg/1200px-Cisco_logo_blue_2016.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Network Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "linux",
                        "bash",
                        "aws",
                        "docker",
                        "git",
                        "ci/cd"
                    ],
                    "good": [
                        "terraform",
                        "kubernetes",
                        "ansible",
                        "monitoring"
                    ],
                    "bonus": [
                        "python",
                        "security compliance",
                        "helm"
                    ]
                }
            }
        ]
    },
    "Intel": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Intel_logo_%282006-2020%29.svg/1200px-Intel_logo_%282006-2020%29.svg.png",
        "roles": [
            {
                "name": "Validation Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            },
            {
                "name": "Firmware Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Samsung R&D": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Samsung_Logo.svg/2000px-Samsung_Logo.svg.png",
        "roles": [
            {
                "name": "R&D Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "AI/ML Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "python",
                        "sql",
                        "pandas",
                        "statistics",
                        "git",
                        "data modeling"
                    ],
                    "good": [
                        "spark",
                        "airflow",
                        "tableau",
                        "power bi"
                    ],
                    "bonus": [
                        "machine learning",
                        "deep learning",
                        "redshift"
                    ]
                }
            }
        ]
    },
    "Ather Energy": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/Ather_Logo.svg/1200px-Ather_Logo.svg.png",
        "roles": [
            {
                "name": "Embedded Systems Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            },
            {
                "name": "Battery Tech Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Darwinbox": {
        "logo": "https://www.darwinbox.com/img/common/logo.svg",
        "roles": [
            {
                "name": "Backend Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "HR Technology Intern",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Keka HR": {
        "logo": "https://www.keka.com/wp-content/uploads/2021/01/keka-logo-blue.svg",
        "roles": [
            {
                "name": "SaaS Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Customer Success Associate",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Qualcomm": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Qualcomm_Logo_2023.svg/1200px-Qualcomm_Logo_2023.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            },
            {
                "name": "Modem Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "ValueLabs": {
        "logo": "https://www.valuelabs.com/wp-content/themes/valuelabs/images/logo.png",
        "roles": [
            {
                "name": "Associate Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Data Scientist",
                "stream": 1,
                "skills": {
                    "core": [
                        "python",
                        "sql",
                        "pandas",
                        "statistics",
                        "git",
                        "data modeling"
                    ],
                    "good": [
                        "spark",
                        "airflow",
                        "tableau",
                        "power bi"
                    ],
                    "bonus": [
                        "machine learning",
                        "deep learning",
                        "redshift"
                    ]
                }
            }
        ]
    },
    "IBS Software": {
        "logo": "https://www.ibsplc.com/sites/default/files/logo.svg",
        "roles": [
            {
                "name": "Trainee Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Travel Tech Analyst",
                "stream": 1,
                "skills": {
                    "core": [
                        "python",
                        "sql",
                        "pandas",
                        "statistics",
                        "git",
                        "data modeling"
                    ],
                    "good": [
                        "spark",
                        "airflow",
                        "tableau",
                        "power bi"
                    ],
                    "bonus": [
                        "machine learning",
                        "deep learning",
                        "redshift"
                    ]
                }
            }
        ]
    },
    "UST Global": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/UST_Global_Logo.svg/1200px-UST_Global_Logo.svg.png",
        "roles": [
            {
                "name": "Associate Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Quality Assurance Intern",
                "stream": 1,
                "skills": {
                    "core": [
                        "selenium",
                        "java",
                        "manual testing",
                        "test planning",
                        "git"
                    ],
                    "good": [
                        "testng",
                        "cucumber",
                        "sql",
                        "api testing"
                    ],
                    "bonus": [
                        "appium",
                        "performance testing",
                        "jmeter"
                    ]
                }
            }
        ]
    },
    "QBurst": {
        "logo": "https://www.qburst.com/img/common/logo.svg",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Mobile App Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            }
        ]
    },
    "Kissflow": {
        "logo": "https://kissflow.com/hubfs/Kissflow_Logo.svg",
        "roles": [
            {
                "name": "SaaS Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Facilio": {
        "logo": "https://facilio.com/images/facilio-logo.svg",
        "roles": [
            {
                "name": "IoT Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Animaker": {
        "logo": "https://www.animaker.com/business/img/logo.svg",
        "roles": [
            {
                "name": "Frontend Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            }
        ]
    },
    "Hippo Video": {
        "logo": "https://www.hippovideo.io/img/hv-logo.svg",
        "roles": [
            {
                "name": "Video Tech Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Postman": {
        "logo": "https://www.postman.com/img/logos/postman-logo.svg",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Zerodha": {
        "logo": "https://zerodha.com/static/images/logo.svg",
        "roles": [
            {
                "name": "Frontend Developer",
                "stream": 1,
                "skills": {
                    "core": [
                        "javascript",
                        "react",
                        "html",
                        "css",
                        "git",
                        "typescript"
                    ],
                    "good": [
                        "redux",
                        "tailwind",
                        "figma",
                        "testing-library"
                    ],
                    "bonus": [
                        "next.js",
                        "three.js",
                        "web performance"
                    ]
                }
            }
        ]
    },
    "Mindtree": {
        "logo": "https://www.mindtree.com/themes/custom/mindtree/logo.svg",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Virtusa": {
        "logo": "https://www.virtusa.com/content/dam/virtusa/logos/virtusa-logo.svg",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Hexaware": {
        "logo": "https://hexaware.com/wp-content/themes/hexaware-main/images/logo.svg",
        "roles": [
            {
                "name": "GET",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Sutherland": {
        "logo": "https://www.sutherlandglobal.com/img/footer-logo.svg",
        "roles": [
            {
                "name": "Technical Support",
                "stream": 1,
                "skills": {
                    "core": [
                        "selenium",
                        "java",
                        "manual testing",
                        "test planning",
                        "git"
                    ],
                    "good": [
                        "testng",
                        "cucumber",
                        "sql",
                        "api testing"
                    ],
                    "bonus": [
                        "appium",
                        "performance testing",
                        "jmeter"
                    ]
                }
            },
            {
                "name": "Customer Service",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Mphasis": {
        "logo": "https://www.mphasis.com/content/dam/mphasis-com/global/logos/mphasis-logo.svg",
        "roles": [
            {
                "name": "Trainee Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Ramco": {
        "logo": "https://www.ramco.com/hubfs/Ramco_Logo_New.png",
        "roles": [
            {
                "name": "ERP Consultant",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "Hyundai": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Hyundai_Motor_Company_logo.svg/1200px-Hyundai_Motor_Company_logo.svg.png",
        "roles": [
            {
                "name": "Production Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "TVS Motors": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/TVS_Motor_Company_logo.svg/1200px-TVS_Motor_Company_logo.svg.png",
        "roles": [
            {
                "name": "R&D Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Ashok Leyland": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Ashok_Leyland_logo.svg/1200px-Ashok_Leyland_logo.svg.png",
        "roles": [
            {
                "name": "Service Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Royal Enfield": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Royal_Enfield_logo.svg/1200px-Royal_Enfield_logo.svg.png",
        "roles": [
            {
                "name": "Design Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Ford India": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ford_Motor_Company_Logo.svg/1200px-Ford_Motor_Company_Logo.svg.png",
        "roles": [
            {
                "name": "Embedded Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Reynolds": {
        "logo": "https://reynolds-india.com/wp-content/uploads/2019/11/logo.png",
        "roles": [
            {
                "name": "Manufacturing Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Caterpillar": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Caterpillar_logo.svg/1200px-Caterpillar_logo.svg.png",
        "roles": [
            {
                "name": "Mechanical Design Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "c",
                        "c++",
                        "microcontrollers",
                        "embedded systems",
                        "rtos",
                        "git"
                    ],
                    "good": [
                        "python",
                        "linux kernel",
                        "i2c/spi",
                        "debugging"
                    ],
                    "bonus": [
                        "autosar",
                        "fpga",
                        "iot protocols"
                    ]
                }
            }
        ]
    },
    "Standard Chartered": {
        "logo": "https://av.sc.com/corp-en/content/images/Sc-logo-social.png",
        "roles": [
            {
                "name": "Technology Associate",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Banking Trainee",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Goldman Sachs": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Goldman_Sachs_logo.svg/2000px-Goldman_Sachs_logo.svg.png",
        "roles": [
            {
                "name": "Technology Analyst",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            },
            {
                "name": "Finance Analyst",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "PayPal": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/PayPal.svg/2000px-PayPal.svg.png",
        "roles": [
            {
                "name": "Software Engineer",
                "stream": 1,
                "skills": {
                    "core": [
                        "data structures",
                        "algorithms",
                        "java",
                        "python",
                        "git",
                        "sql"
                    ],
                    "good": [
                        "rest api",
                        "docker",
                        "unit testing",
                        "linux"
                    ],
                    "bonus": [
                        "kubernetes",
                        "system design",
                        "microservices",
                        "cloud"
                    ]
                }
            }
        ]
    },
    "HDFC Bank": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/HDFC_Bank_Logo.svg/1200px-HDFC_Bank_Logo.svg.png",
        "roles": [
            {
                "name": "Relationship Manager",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    },
    "Federal Bank": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Federal_Bank_Logo.svg/1200px-Federal_Bank_Logo.svg.png",
        "roles": [
            {
                "name": "Clerk/PO",
                "stream": 2,
                "skills": {
                    "core": [
                        "communication",
                        "recruitment",
                        "employee relations",
                        "problem solving"
                    ],
                    "good": [
                        "talent management",
                        "excel",
                        "interpersonal skills"
                    ],
                    "bonus": [
                        "payroll",
                        "hris",
                        "conflict resolution"
                    ]
                }
            }
        ]
    }
}

PRIORITY_LABEL = {"core": "Must Know", "good": "Good to Have", "bonus": "Bonus / Advanced"}


def clean_role_name(role_name):
    """Normalize overly generic trainee/intern suffixes for cleaner role titles."""
    name = (role_name or "").strip()
    if not name:
        return name

    # Keep specific known titles as-is.
    keep_exact = {"Graduate Engineer Trainee", "Management Trainee (Marketing)"}
    if name in keep_exact:
        return name

    # Remove trailing trainee/intern markers while preserving core role meaning.
    name = re.sub(r"\s*\(?\b(Trainee|Intern)\b\)?\s*$", "", name, flags=re.IGNORECASE).strip()
    name = re.sub(r"\s{2,}", " ", name)
    return name

ARTS_IT_ROLE_TEMPLATES = [
    {
        "name": "Frontend Developer Trainee",
        "stream": 2,
        "skills": {
            "core": ["html", "css", "javascript", "communication", "git", "problem solving"],
            "good": ["react", "figma", "responsive design", "debugging"],
            "bonus": ["typescript", "ui testing", "web accessibility"]
        }
    },
    {
        "name": "QA Testing Trainee",
        "stream": 2,
        "skills": {
            "core": ["manual testing", "test case design", "bug reporting", "communication", "excel"],
            "good": ["api testing", "sql basics", "jira", "regression testing"],
            "bonus": ["selenium", "python basics", "automation testing"]
        }
    },
    {
        "name": "Business Analyst Trainee",
        "stream": 2,
        "skills": {
            "core": ["analytical thinking", "communication", "excel", "documentation", "problem solving"],
            "good": ["power bi", "sql basics", "stakeholder management", "presentation skills"],
            "bonus": ["tableau", "agile", "financial modeling"]
        }
    },
    {
        "name": "Backend Developer Trainee",
        "stream": 2,
        "skills": {
            "core": ["python", "sql", "api fundamentals", "communication", "problem solving", "git"],
            "good": ["flask", "node.js basics", "database design", "debugging"],
            "bonus": ["docker", "cloud basics", "system design basics"]
        }
    },
    {
        "name": "Full Stack Developer Trainee",
        "stream": 2,
        "skills": {
            "core": ["html", "css", "javascript", "python", "sql", "git"],
            "good": ["react", "flask", "api integration", "debugging"],
            "bonus": ["typescript", "docker", "cloud basics"]
        }
    }
]

ENGINEERING_ROLE_PACKS = [
    [
        {
            "name": "Backend Developer",
            "stream": 1,
            "skills": {
                "core": ["python", "java", "sql", "rest api", "data structures", "git"],
                "good": ["system design", "docker", "unit testing", "linux"],
                "bonus": ["microservices", "kubernetes", "cloud"]
            }
        },
        {
            "name": "Full Stack Developer",
            "stream": 1,
            "skills": {
                "core": ["javascript", "react", "python", "sql", "html", "css"],
                "good": ["typescript", "node.js", "api integration", "git"],
                "bonus": ["docker", "cloud", "performance optimization"]
            }
        },
        {
            "name": "QA Engineer",
            "stream": 1,
            "skills": {
                "core": ["manual testing", "test case design", "bug tracking", "sql", "api testing"],
                "good": ["selenium", "python", "regression testing", "jira"],
                "bonus": ["automation frameworks", "performance testing", "ci/cd"]
            }
        }
    ],
    [
        {
            "name": "Frontend Developer",
            "stream": 1,
            "skills": {
                "core": ["html", "css", "javascript", "react", "git", "responsive design"],
                "good": ["typescript", "redux", "ui testing", "accessibility"],
                "bonus": ["next.js", "web performance", "figma"]
            }
        },
        {
            "name": "Data Analyst",
            "stream": 1,
            "skills": {
                "core": ["sql", "excel", "python", "statistics", "problem solving"],
                "good": ["power bi", "tableau", "data cleaning", "data visualization"],
                "bonus": ["machine learning", "airflow", "big data tools"]
            }
        },
        {
            "name": "DevOps Engineer",
            "stream": 1,
            "skills": {
                "core": ["linux", "docker", "ci/cd", "git", "cloud basics"],
                "good": ["kubernetes", "terraform", "monitoring", "scripting"],
                "bonus": ["security", "helm", "cost optimization"]
            }
        }
    ],
    [
        {
            "name": "Software Testing Engineer",
            "stream": 1,
            "skills": {
                "core": ["manual testing", "api testing", "test planning", "bug tracking", "sql"],
                "good": ["selenium", "pytest", "jira", "automation basics"],
                "bonus": ["performance testing", "security testing", "ci/cd"]
            }
        },
        {
            "name": "Associate Product Analyst",
            "stream": 1,
            "skills": {
                "core": ["analytics", "excel", "sql", "communication", "problem solving"],
                "good": ["power bi", "ab testing", "market research", "documentation"],
                "bonus": ["tableau", "python", "product metrics"]
            }
        },
        {
            "name": "Cloud Support Engineer",
            "stream": 1,
            "skills": {
                "core": ["linux", "cloud basics", "networking basics", "scripting", "troubleshooting"],
                "good": ["docker", "monitoring", "incident management", "git"],
                "bonus": ["kubernetes", "terraform", "security basics"]
            }
        }
    ]
]

# Core fresher IT roles commonly seen across large MNC hiring drives.
MANDATORY_ENGINEERING_ROLES = [
    {
        "name": "Backend Developer",
        "stream": 1,
        "skills": {
            "core": ["python", "java", "sql", "rest api", "data structures", "git"],
            "good": ["system design", "docker", "unit testing", "linux"],
            "bonus": ["microservices", "kubernetes", "cloud"]
        }
    },
    {
        "name": "Frontend Developer",
        "stream": 1,
        "skills": {
            "core": ["html", "css", "javascript", "react", "git", "responsive design"],
            "good": ["typescript", "redux", "ui testing", "accessibility"],
            "bonus": ["next.js", "web performance", "figma"]
        }
    },
    {
        "name": "Full Stack Developer",
        "stream": 1,
        "skills": {
            "core": ["javascript", "react", "python", "sql", "html", "css"],
            "good": ["typescript", "node.js", "api integration", "git"],
            "bonus": ["docker", "cloud", "performance optimization"]
        }
    },
    {
        "name": "QA Engineer",
        "stream": 1,
        "skills": {
            "core": ["manual testing", "test case design", "bug tracking", "sql", "api testing"],
            "good": ["selenium", "python", "regression testing", "jira"],
            "bonus": ["automation frameworks", "performance testing", "ci/cd"]
        }
    },
    {
        "name": "Data Analyst",
        "stream": 1,
        "skills": {
            "core": ["sql", "excel", "python", "statistics", "problem solving"],
            "good": ["power bi", "tableau", "data cleaning", "data visualization"],
            "bonus": ["machine learning", "airflow", "big data tools"]
        }
    },
    {
        "name": "DevOps Engineer",
        "stream": 1,
        "skills": {
            "core": ["linux", "docker", "ci/cd", "git", "cloud basics"],
            "good": ["kubernetes", "terraform", "monitoring", "scripting"],
            "bonus": ["security", "helm", "cost optimization"]
        }
    }
]

EXPANDED_ARTS_COMPANIES = [
    "TCS", "Infosys", "Cognizant", "HCLTech", "Zoho", "Freshworks", "Chargebee", "Darwinbox",
    "Google", "Microsoft", "Amazon", "Flipkart", "PhonePe", "Razorpay", "Cisco", "Intel",
    "Samsung R&D", "Qualcomm", "ValueLabs", "UST Global", "QBurst", "Kissflow", "Postman",
    "Mindtree", "Virtusa", "Hexaware", "Mphasis", "Goldman Sachs", "PayPal"
]

EXPANDED_ENGINEERING_COMPANIES = [
    "TCS", "Infosys", "Cognizant", "HCLTech", "Zoho", "Freshworks", "Chargebee", "Darwinbox",
    "Google", "Microsoft", "Amazon", "Flipkart", "PhonePe", "Razorpay", "Cisco", "Intel",
    "Samsung R&D", "Qualcomm", "ValueLabs", "UST Global", "QBurst", "Kissflow", "Postman",
    "Mindtree", "Virtusa", "Hexaware", "Mphasis", "PayPal", "Accenture", "Capgemini",
    "IBM", "Tech Mahindra", "LTIMindtree", "Wipro", "Oracle", "JPMorgan Chase", "Tata Elxsi",
    "Bosch", "Siemens", "Nokia", "Atos", "CGI", "NTT DATA", "Coforge", "Persistent Systems"
]

ADDITIONAL_COMPANIES_DATA = {
    "Accenture": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Accenture.svg",
        "roles": [
            {"name": "Associate Software Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "data structures", "git"], "good": ["rest api", "linux", "unit testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "bug reporting", "communication", "excel"], "good": ["jira", "sql basics", "api testing"], "bonus": ["selenium", "automation testing"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["analytical thinking", "excel", "communication", "documentation"], "good": ["power bi", "sql basics", "presentation skills"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Capgemini": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Capgemini_201x_logo.svg",
        "roles": [
            {"name": "Software Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "data structures", "git"], "good": ["rest api", "linux", "testing"], "bonus": ["docker", "cloud", "devops"]}},
            {"name": "Frontend Developer Trainee", "stream": 2, "skills": {"core": ["html", "css", "javascript", "communication", "git"], "good": ["react", "responsive design", "figma"], "bonus": ["typescript", "ui testing"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "analytical thinking", "problem solving"], "good": ["power bi", "sql basics", "documentation"], "bonus": ["tableau", "presentation skills"]}}
        ]
    },
    "IBM": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg",
        "roles": [
            {"name": "Application Developer", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "unit testing", "linux"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "test case design", "communication", "bug reporting"], "good": ["api testing", "jira", "excel"], "bonus": ["selenium", "automation testing"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["analytical thinking", "communication", "excel", "documentation"], "good": ["power bi", "sql basics", "stakeholder management"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Deloitte": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/56/Deloitte.svg",
        "roles": [
            {"name": "Technology Analyst", "stream": 1, "skills": {"core": ["python", "sql", "excel", "problem solving", "communication"], "good": ["power bi", "data modeling", "linux"], "bonus": ["cloud", "automation"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "presentation skills"], "bonus": ["tableau", "agile"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "bug reporting", "communication", "test case design"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}}
        ]
    },
    "EY": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/0/0b/EY_logo_2019.svg",
        "roles": [
            {"name": "Technology Consultant Analyst", "stream": 1, "skills": {"core": ["python", "sql", "excel", "problem solving", "communication"], "good": ["power bi", "data analysis", "documentation"], "bonus": ["cloud", "automation"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["analytical thinking", "excel", "communication", "documentation"], "good": ["power bi", "sql basics", "stakeholder management"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "KPMG": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9d/KPMG_logo.svg",
        "roles": [
            {"name": "Data Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "problem solving"], "good": ["power bi", "sql basics", "statistics"], "bonus": ["tableau", "python basics"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "documentation", "analytical thinking"], "good": ["power bi", "stakeholder management", "presentation"], "bonus": ["agile", "tableau"]}}
        ]
    },
    "Tech Mahindra": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/84/Tech_Mahindra_New_Logo.svg",
        "roles": [
            {"name": "Associate Software Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "data structures"], "good": ["rest api", "linux", "testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "Frontend Developer Trainee", "stream": 2, "skills": {"core": ["html", "css", "javascript", "communication", "git"], "good": ["react", "figma", "responsive design"], "bonus": ["typescript", "ui testing"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "test case design", "bug reporting", "communication"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}}
        ]
    },
    "LTIMindtree": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/c7/LTIMindtree_logo.svg",
        "roles": [
            {"name": "Graduate Engineer Trainee", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "linux", "testing"], "bonus": ["docker", "cloud", "microservices"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "analytical thinking", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Wipro": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Wipro_Primary_Logo_Color_RGB.svg",
        "roles": [
            {"name": "Project Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "data structures", "git"], "good": ["linux", "rest api", "testing"], "bonus": ["cloud", "docker", "devops"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "bug reporting", "communication", "excel"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "stakeholder management"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Oracle": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg",
        "roles": [
            {"name": "Application Developer", "stream": 1, "skills": {"core": ["java", "sql", "data structures", "git", "problem solving"], "good": ["rest api", "testing", "linux"], "bonus": ["cloud", "microservices", "docker"]}},
            {"name": "Frontend Developer Trainee", "stream": 2, "skills": {"core": ["html", "css", "javascript", "communication", "git"], "good": ["react", "responsive design", "figma"], "bonus": ["typescript", "ui testing"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "analytical thinking", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Citi": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Citi.svg",
        "roles": [
            {"name": "Technology Analyst", "stream": 1, "skills": {"core": ["python", "sql", "problem solving", "git", "data structures"], "good": ["linux", "rest api", "testing"], "bonus": ["cloud", "automation", "docker"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "presentation skills"], "bonus": ["tableau", "financial analysis"]}}
        ]
    },
    "HSBC": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/a/aa/HSBC_logo_%282018%29.svg",
        "roles": [
            {"name": "Technology Trainee", "stream": 1, "skills": {"core": ["java", "python", "sql", "problem solving", "git"], "good": ["rest api", "linux", "testing"], "bonus": ["cloud", "automation", "docker"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "documentation", "analytical thinking"], "good": ["power bi", "sql basics", "stakeholder management"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "JPMorgan Chase": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a1/JPMorgan_Chase_logo_2008.svg",
        "roles": [
            {"name": "Software Engineer Analyst", "stream": 1, "skills": {"core": ["java", "python", "sql", "data structures", "git"], "good": ["rest api", "linux", "unit testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "test case design", "bug reporting", "communication"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation testing"]}}
        ]
    },
    "Tata Elxsi": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/0/08/Tata_Elxsi_logo.svg",
        "roles": [
            {"name": "Software Engineer", "stream": 1, "skills": {"core": ["c++", "python", "git", "problem solving", "data structures"], "good": ["linux", "testing", "sql"], "bonus": ["embedded systems", "automation", "cloud"]}},
            {"name": "Frontend Developer Trainee", "stream": 2, "skills": {"core": ["html", "css", "javascript", "communication", "git"], "good": ["react", "responsive design", "figma"], "bonus": ["typescript", "ui testing"]}}
        ]
    },
    "Bosch": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Bosch-logo.svg",
        "roles": [
            {"name": "Graduate Trainee Engineer", "stream": 1, "skills": {"core": ["c", "c++", "python", "git", "problem solving"], "good": ["linux", "testing", "microcontrollers"], "bonus": ["embedded", "automation", "iot"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "statistics"]}}
        ]
    },
    "Siemens": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Siemens-logo.svg",
        "roles": [
            {"name": "Software Developer", "stream": 1, "skills": {"core": ["c++", "python", "sql", "git", "problem solving"], "good": ["testing", "linux", "rest api"], "bonus": ["cloud", "docker", "devops"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "test case design", "bug reporting", "communication"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}}
        ]
    },
    "Nokia": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/0/02/Nokia_wordmark.svg",
        "roles": [
            {"name": "Software Engineer Trainee", "stream": 1, "skills": {"core": ["c", "c++", "python", "git", "problem solving"], "good": ["linux", "testing", "sql"], "bonus": ["networking", "cloud", "automation"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "analytical thinking", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Atos": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Atos.svg",
        "roles": [
            {"name": "Associate Consultant", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "testing", "linux"], "bonus": ["cloud", "automation", "docker"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "bug reporting", "communication", "test case design"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}}
        ]
    },
    "CGI": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9f/CGI_logo.svg",
        "roles": [
            {"name": "Software Developer", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "testing", "linux"], "bonus": ["cloud", "docker", "devops"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "analytical thinking", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "NTT DATA": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/NTT_DATA_logo.svg",
        "roles": [
            {"name": "Graduate Engineer Trainee", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "linux", "testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "stakeholder management"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Coforge": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Coforge_logo.svg",
        "roles": [
            {"name": "Software Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "linux", "testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "Frontend Developer Trainee", "stream": 2, "skills": {"core": ["html", "css", "javascript", "communication", "git"], "good": ["react", "figma", "responsive design"], "bonus": ["typescript", "ui testing"]}}
        ]
    },
    "Persistent Systems": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/80/Persistent_Systems_logo.svg",
        "roles": [
            {"name": "Associate Software Engineer", "stream": 1, "skills": {"core": ["java", "python", "sql", "data structures", "git"], "good": ["rest api", "linux", "unit testing"], "bonus": ["cloud", "docker", "microservices"]}},
            {"name": "QA Testing Trainee", "stream": 2, "skills": {"core": ["manual testing", "test case design", "bug reporting", "communication"], "good": ["jira", "api testing", "sql basics"], "bonus": ["selenium", "automation"]}}
        ]
    },
    "Yash Technologies": {
        "logo": "https://www.yash.com/wp-content/themes/yash/images/yash-logo.svg",
        "roles": [
            {"name": "Developer Trainee", "stream": 1, "skills": {"core": ["java", "python", "sql", "git", "problem solving"], "good": ["rest api", "linux", "testing"], "bonus": ["cloud", "docker", "devops"]}},
            {"name": "Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "analytical thinking", "communication", "documentation"], "good": ["power bi", "sql basics", "presentation"], "bonus": ["tableau", "agile"]}}
        ]
    },
    "Fractal Analytics": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Fractal_Analytics_logo.svg",
        "roles": [
            {"name": "Data Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "statistics", "sql basics", "analytical thinking", "communication"], "good": ["power bi", "python basics", "data visualization"], "bonus": ["tableau", "machine learning"]}},
            {"name": "Business Analyst Trainee", "stream": 2, "skills": {"core": ["excel", "communication", "documentation", "problem solving"], "good": ["power bi", "stakeholder management", "sql basics"], "bonus": ["tableau", "agile"]}}
        ]
    }
}


def _expanded_seed_data():
    """Build expanded seed with more companies and Arts/IT fresher roles."""
    seed = copy.deepcopy(COMPANIES_DATA)

    def append_unique_roles(company_name, role_templates):
        existing = {clean_role_name(r["name"]) for r in seed[company_name]["roles"]}
        for role in role_templates:
            cleaned = clean_role_name(role["name"])
            if cleaned not in existing:
                role_copy = copy.deepcopy(role)
                role_copy["name"] = cleaned
                seed[company_name]["roles"].append(role_copy)
                existing.add(cleaned)

    for company_name, company_info in ADDITIONAL_COMPANIES_DATA.items():
        seed[company_name] = company_info

    for company_name in EXPANDED_ARTS_COMPANIES:
        if company_name not in seed:
            continue
        append_unique_roles(company_name, ARTS_IT_ROLE_TEMPLATES)

    # Add varied engineering role packs so companies don't show the same repeated roles.
    for idx, company_name in enumerate(EXPANDED_ENGINEERING_COMPANIES):
        if company_name not in seed:
            continue
        append_unique_roles(company_name, MANDATORY_ENGINEERING_ROLES)
        pack = ENGINEERING_ROLE_PACKS[idx % len(ENGINEERING_ROLE_PACKS)]
        append_unique_roles(company_name, pack)

    return seed


class _Connection:
    """Thin wrapper so the rest of the code can keep using conn.execute(...)
    like it did with sqlite3. Rows come back as dicts."""

    def __init__(self, raw):
        self._raw = raw

    def cursor(self):
        return self._raw.cursor()

    def execute(self, sql, params=None):
        cur = self._raw.cursor()
        cur.execute(sql, params)
        return cur

    def commit(self):
        self._raw.commit()

    def rollback(self):
        self._raw.rollback()

    def close(self):
        self._raw.close()


def get_db():
    raw = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **DB_CONFIG)
    return _Connection(raw)


# roles.stream: 1 = Engineering, 2 = Arts
_SCHEMA = [
    "DROP TABLE IF EXISTS role_skills",
    "DROP TABLE IF EXISTS roles",
    "DROP TABLE IF EXISTS companies",
    """CREATE TABLE IF NOT EXISTS companies (
        id   INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE,
        logo TEXT
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS roles (
        id         INT AUTO_INCREMENT PRIMARY KEY,
        company_id INT NOT NULL,
        role_name  VARCHAR(255) NOT NULL,
        stream     INT NOT NULL DEFAULT 1, 
        FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS role_skills (
        id         INT AUTO_INCREMENT PRIMARY KEY,
        role_id    INT NOT NULL,
        skill_name VARCHAR(255) NOT NULL,
        priority   VARCHAR(20) NOT NULL,
        FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS activity_log (
        id INT AUTO_INCREMENT PRIMARY KEY,
        `type` VARCHAR(50),
        `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
        user_name VARCHAR(255),
        company_name VARCHAR(255),
        role_name VARCHAR(255),
        academic_stream VARCHAR(100),
        match_score INT,
        matched_skills TEXT,
        missing_skills TEXT,
        ip VARCHAR(64)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
]


def init_db():
    conn = get_db()
    c = conn.cursor()

    for statement in _SCHEMA:
        c.execute(statement)

    # Seed data
    seed_data = _expanded_seed_data()
    for company_name, company_info in seed_data.items():
        c.execute("INSERT IGNORE INTO companies (name, logo) VALUES (%s, %s)",
                  (company_name, company_info["logo"]))
        c.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
        company_id = c.fetchone()["id"]

        for role_data in company_info["roles"]:
            role_name = clean_role_name(role_data["name"])
            stream = role_data["stream"]
            skill_groups = role_data["skills"]

            c.execute("DELETE FROM roles WHERE company_id = %s AND role_name = %s",
                      (company_id, role_name))
            c.execute("INSERT INTO roles (company_id, role_name, stream) VALUES (%s, %s, %s)",
                      (company_id, role_name, stream))
            role_id = c.lastrowid

            for priority, skills in skill_groups.items():
                for skill in skills:
                    c.execute("INSERT INTO role_skills (role_id, skill_name, priority) VALUES (%s, %s, %s)",
                              (role_id, skill, priority))

    conn.commit()
    conn.close()
    print("[OK] Database initialized and seeded successfully!")


def get_all_companies(stream=None):
    conn = get_db()
    if stream:
        rows = conn.execute(
            "SELECT DISTINCT c.id, c.name, c.logo FROM companies c "
            "JOIN roles r ON c.id = r.company_id WHERE r.stream = %s ORDER BY c.name",
            (stream,)
        ).fetchall()
    else:
        rows = conn.execute("SELECT id, name, logo FROM companies ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def search_companies(query, stream=None):
    conn = get_db()
    if stream:
        rows = conn.execute(
            "SELECT DISTINCT c.id, c.name, c.logo FROM companies c "
            "JOIN roles r ON c.id = r.company_id "
            "WHERE LOWER(c.name) LIKE %s AND r.stream = %s ORDER BY c.name",
            (f"%{query.lower()}%", stream)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, name, logo FROM companies WHERE LOWER(name) LIKE %s ORDER BY name",
            (f"%{query.lower()}%",)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_roles_for_company(company_id, stream=None):
    conn = get_db()
    company_row = conn.execute("SELECT name FROM companies WHERE id = %s", (company_id,)).fetchone()
    company_name = company_row["name"] if company_row else None
    if stream:
        rows = conn.execute(
            "SELECT id, role_name FROM roles WHERE company_id = %s AND stream = %s ORDER BY role_name",
            (company_id, stream)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, role_name FROM roles WHERE company_id = %s ORDER BY role_name",
            (company_id,)
        ).fetchall()
    conn.close()
    roles = [dict(r) for r in rows]

    inferred_stream = stream if stream in (1, 2) else 1
    for role in roles:
        role["role_name"] = clean_role_name(role.get("role_name", ""))
        role["hiring_expectation_months"] = estimate_hiring_expectation_months(
            role.get("role_name", ""),
            inferred_stream,
            company_name
        )
    return roles


def get_skills_for_role(role_id):
    """Returns {'core': [...], 'good': [...], 'bonus': [...]}"""
    conn = get_db()
    rows = conn.execute(
        "SELECT skill_name, priority FROM role_skills WHERE role_id = %s",
        (role_id,)
    ).fetchall()
    conn.close()
    result = {"core": [], "good": [], "bonus": []}
    for r in rows:
        result[r["priority"]].append(r["skill_name"])
    return result


def get_company_by_id(company_id):
    conn = get_db()
    row = conn.execute("SELECT id, name, logo FROM companies WHERE id = %s", (company_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_role_by_id(role_id):
    conn = get_db()
    row = conn.execute(
        "SELECT r.id, r.role_name, c.name as company_name, c.logo as company_logo "
        "FROM roles r JOIN companies c ON r.company_id = c.id WHERE r.id = %s",
        (role_id,)
    ).fetchone()
    conn.close()
    if not row:
        return None
    role = dict(row)
    role["role_name"] = clean_role_name(role.get("role_name", ""))
    return role



# ─── Universal Fallback (Dynamic Search) ──────────────────────────────────

GENERIC_ROLES = {
    1: ["Software Development Engineer", "Data Analyst", "DevOps Engineer", "Cloud Architect", "QA Automation Engineer"],
    2: ["HR Associate", "Marketing Executive", "Business Process Lead", "Financial Analyst", "Content Specialist"]
}

def _format_month_window(start_month, end_month):
    """Return month-name window like 'February - August'."""
    start_name = calendar.month_name[start_month]
    end_name = calendar.month_name[end_month]
    if start_name == end_name:
        return start_name
    return f"{start_name} - {end_name}"


def estimate_hiring_expectation_months(role_name, stream, company_name=None):
    """
    Return hiring expectation as month names based on actual company hiring cycles.
    Honest hiring periods based on real campus recruitment patterns.
    """
    role = (role_name or "").lower()
    company = (company_name or "").lower()

    # Actual hiring periods based on company recruitment cycles
    company_hiring_periods = {
        # Service-based companies - typically Aug-Oct for campus hiring
        "tcs": "August - October",
        "infosys": "August - October", 
        "cognizant": "August - October",
        "hcltech": "August - October",
        
        # Product companies - typically Sep-Nov
        "google": "September - November",
        "microsoft": "September - November",
        "amazon": "September - November",
        "flipkart": "September - November",
        
        # Startups and mid-size companies - more varied
        "zoho": "July - December",
        "freshworks": "July - December",
        "chargebee": "July - December",
        "guvi": "July - December",
        "contus tech": "July - December",
        "aspire systems": "July - December",
        "ramco systems": "July - December",
    }

    # Role-specific hiring periods for companies without specific data
    role_hiring_periods = {
        # Engineering roles typically Aug-Nov
        "engineer": "August - November",
        "developer": "August - November",
        "software engineer": "August - November",
        "sde": "August - November",
        
        # Non-technical roles often have different timelines
        "content writer": "July - December",
        "digital marketing": "July - December", 
        "hr": "July - December",
        "bpo": "July - December",
        "process associate": "July - December",
        
        # QA and testing roles
        "qa": "August - November",
        "tester": "August - November",
        
        # Data roles
        "data engineer": "September - November",
        "data analyst": "September - November",
    }

    # Check company-specific first
    if company in company_hiring_periods:
        return company_hiring_periods[company]

    # Then check role-specific
    for role_key, period in role_hiring_periods.items():
        if role_key in role:
            return period

    # Default based on stream
    if stream == 2:  # Arts & Science - often more flexible
        return "July - December"
    else:  # Engineering - typical campus season
        return "August - November"

def get_generic_roles_list(stream):
    """Returns a list of roles for the dynamic fallback."""
    roles = GENERIC_ROLES.get(stream, GENERIC_ROLES[1])
    return [
        {
            "id": -100 - i,
            "role_name": name,
            "is_generic": True,
            "hiring_expectation_months": estimate_hiring_expectation_months(name, stream, None)
        }
        for i, name in enumerate(roles)
    ]

def log_activity(activity_data):
    """Log a user activity or resume upload to the database"""
    conn = get_db()
    try:
        conn.execute("""
            INSERT INTO activity_log 
            (`type`, user_name, company_name, role_name, academic_stream, match_score, matched_skills, missing_skills, ip)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            activity_data.get('type'),
            activity_data.get('user_name'),
            activity_data.get('company_name'),
            activity_data.get('role_name'),
            activity_data.get('academic_stream'),
            activity_data.get('match_score'),
            ", ".join(activity_data.get('matched_skills_list', [])),
            ", ".join(activity_data.get('missing_skills_list', [])),
            activity_data.get('ip')
        ))
        conn.commit()
    except Exception as e:
        print(f"[ERROR] Database logging failed: {e}")
    finally:
        conn.close()

def get_activities(limit=100):
    """Retrieve recent activities from the database"""
    conn = get_db()
    try:
        rows = conn.execute("SELECT * FROM activity_log ORDER BY `timestamp` DESC LIMIT %s", (limit,)).fetchall()
        activities = []
        for row in rows:
            d = dict(row)
            # Convert comma-separated strings back to lists for the template
            d['matched_skills_list'] = [s.strip() for s in d['matched_skills'].split(',')] if d['matched_skills'] else []
            d['missing_skills_list'] = [s.strip() for s in d['missing_skills'].split(',')] if d['missing_skills'] else []
            activities.append(d)
        return activities
    finally:
        conn.close()

def clear_all_activities():
    """Wipe all activity data from the database"""
    conn = get_db()
    try:
        conn.execute("DELETE FROM activity_log")
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()

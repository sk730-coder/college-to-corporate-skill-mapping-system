# College to Corporate Skill Mapping System

A Flask-based web application that helps students identify the skill gaps between their existing skills and industry job requirements.

## Features
- Search companies and job roles.
- Upload resumes for skill analysis.
- Identify missing skills.
- View skill priorities.
- Generate personalized learning roadmaps.
- Store company, role and skill data using MySQL.

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- Bootstrap
- JavaScript

## Requirements
- Python 3.10 or later
- MySQL Server
- Tesseract OCR (if using resume image OCR)

## Installation

1. Clone or download this repository.
2. Install the required Python packages:

   `pip install -r requirements.txt`
                or
   `python -m pip install -r requirements.txt`

4. Create a MySQL user and configure database credentials.

5. Copy `.env.example` and rename the copy to `.env`.

6. Update the `.env` file with your MySQL credentials.

7. Run the application:

   `python app.py`

8. Open the local URL displayed in your terminal.

## Database
The application automatically creates the `skills_db` database and initializes its tables when the MySQL user has the necessary permissions.

## Security
Never upload your actual `.env` file or database credentials to GitHub.

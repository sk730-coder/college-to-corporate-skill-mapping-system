import os
import re
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------------------------------------------------- #
#                                    MODELS                                    #
# ---------------------------------------------------------------------------- #

db = SQLAlchemy()
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    logo = db.Column(db.String(255))
    roles = db.relationship('Role', backref='company', lazy=True, cascade="all, delete-orphan")

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    role_name = db.Column(db.String(100), nullable=False)
    stream = db.Column(db.Integer, nullable=False, default=1) # 1: Eng, 2: Arts
    skills = db.relationship('RoleSkill', backref='role', lazy=True, cascade="all, delete-orphan")

class RoleSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(20), nullable=False) # core, good, bonus

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    type = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100))
    academic_stream = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    role_name = db.Column(db.String(100))
    matched_skills = db.Column(db.Text)
    missing_skills = db.Column(db.Text)
    ip = db.Column(db.String(50))

# ---------------------------------------------------------------------------- #
#                               HELPER FUNCTIONS                               #
# ---------------------------------------------------------------------------- #

def clean_role_name(name):
    return re.sub(r'\s*\(.*?\)', '', name).strip()

# ---------------------------------------------------------------------------- #
#                              DATABASE OPERATIONS                             #
# ---------------------------------------------------------------------------- #

def init_db():
    """Creates all tables and seeds them with initial data."""
    from database_seed import COMPANIES_DATA
    db.drop_all()
    db.create_all()

    for company_name, company_info in COMPANIES_DATA.items():
        company = Company(name=company_name, logo=company_info["logo"])
        db.session.add(company)
        db.session.flush() # Flush to get the company ID

        for role_data in company_info["roles"]:
            role = Role(company_id=company.id, role_name=clean_role_name(role_data["name"]), stream=role_data["stream"])
            db.session.add(role)
            db.session.flush() # Flush to get the role ID

            for priority, skills in role_data["skills"].items():
                for skill_name in skills:
                    skill = RoleSkill(role_id=role.id, skill_name=skill_name, priority=priority)
                    db.session.add(skill)
    
    db.session.commit()
    print("[OK] Database initialized and seeded successfully with SQLAlchemy!")

# ---------------------------------------------------------------------------- #
#                               DATA ACCESS FNS                                #
# ---------------------------------------------------------------------------- #

def get_all_companies(stream=None):
    if stream:
        return Company.query.join(Role).filter(Role.stream == stream).distinct().order_by(Company.name).all()
    return Company.query.order_by(Company.name).all()

def search_companies(query, stream=None):
    q = Company.query.filter(Company.name.ilike(f'%{query}%'))
    if stream:
        q = q.join(Role).filter(Role.stream == stream).distinct()
    return q.order_by(Company.name).all()

def get_roles_for_company(company_id, stream=None):
    query = Role.query.filter_by(company_id=company_id)
    if stream:
        query = query.filter_by(stream=stream)
    return query.order_by(Role.role_name).all()

def get_skills_for_role(role_id):
    skills = RoleSkill.query.filter_by(role_id=role_id).all()
    result = {"core": [], "good": [], "bonus": []}
    for skill in skills:
        result[skill.priority].append(skill.skill_name)
    return result

def get_company_by_id(company_id):
    return Company.query.get(company_id)

def get_role_by_id(role_id):
    return Role.query.get(role_id)

# ---------------------------------------------------------------------------- #
#                               ACTIVITY LOGGING                               #
# ---------------------------------------------------------------------------- #

def log_activity(data):
    try:
        activity = Activity(**data)
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[ERROR] DB log_activity failed: {e}")

def get_all_activities():
    return Activity.query.order_by(Activity.timestamp.desc()).all()

def clear_all_activities():
    try:
        db.session.query(Activity).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[ERROR] DB clear_all_activities failed: {e}")

# Placeholder for original function, can be removed if not used elsewhere
def estimate_hiring_expectation_months(role_name, stream, company_name=None):
    return "August - November"

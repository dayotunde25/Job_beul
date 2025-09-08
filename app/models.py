from __init__ import db
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    # Basic Information
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    linkedin_url = db.Column(db.String(200))
    portfolio_url = db.Column(db.String(200))

    # Professional Information
    current_position = db.Column(db.String(100))
    years_of_experience = db.Column(db.Integer)
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    skills = db.Column(db.Text)
    certifications = db.Column(db.Text)
    languages = db.Column(db.Text)
    summary = db.Column(db.Text)

    # Job Preferences for Recommendations
    preferred_job_types = db.Column(db.Text)  # JSON string of job types
    preferred_locations = db.Column(db.Text)  # JSON string of preferred locations
    salary_expectation_min = db.Column(db.Integer)
    salary_expectation_max = db.Column(db.Integer)
    remote_work_preference = db.Column(db.String(20))  # 'remote', 'hybrid', 'onsite', 'any'

    # Profile Completeness
    profile_completeness = db.Column(db.Integer, default=0)  # Percentage 0-100

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def calculate_profile_completeness(self):
        """Calculate profile completeness percentage"""
        fields_to_check = [
            self.first_name, self.last_name, self.phone, self.address,
            self.city, self.country, self.current_position, self.summary,
            self.skills, self.experience, self.education
        ]

        completed_fields = sum(1 for field in fields_to_check if field and field.strip())
        total_fields = len(fields_to_check)

        # Add bonus points for optional fields
        bonus_fields = [self.linkedin_url, self.portfolio_url, self.certifications, self.languages]
        bonus_completed = sum(1 for field in bonus_fields if field and field.strip())

        # Base percentage from required fields + bonus from optional fields
        base_percentage = (completed_fields / total_fields) * 85
        bonus_percentage = (bonus_completed / len(bonus_fields)) * 15

        return min(100, int(base_percentage + bonus_percentage))

    def update_profile_completeness(self):
        """Update the profile completeness field"""
        self.profile_completeness = self.calculate_profile_completeness()

    def __repr__(self):
        return f'<User {self.username}>'

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    description = db.Column(db.Text)
    url = db.Column(db.String(500), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(50))  # e.g., 'linkedin', 'indeed'

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'

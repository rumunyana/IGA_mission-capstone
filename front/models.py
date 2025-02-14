from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iga_hifadhi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model (Students & Teachers)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "student" or "teacher"

# Student Profile Model
class StudentProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    career_interest = db.Column(db.String(100))
    subjects = db.Column(db.String(200))
    ai_track = db.Column(db.String(50))  # AI Suggested Track

# AI Recommendations Model
class Recommendations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    recommended_track = db.Column(db.String(50), nullable=False)
    suggested_subjects = db.Column(db.String(255), nullable=False)
    career_suggestions = db.Column(db.String(255), nullable=False)
    teacher_feedback = db.Column(db.String(255), nullable=True)  # Teacher's advice

# Create Tables
with app.app_context():
    db.create_all()

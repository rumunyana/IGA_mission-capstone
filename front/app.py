from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import joblib
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iga_hifadhi.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Load trained ML Model
try:
    model = joblib.load("model_rf.joblib")
except FileNotFoundError:
    model = None
    print("Warning: model_rf.joblib not found. Ensure the model is trained and available.")

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "student" or "teacher"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        role = request.form['role']
        new_user = User(email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('sign.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Homepage Route (Landing Page)
@app.route('/')
def home():
    return render_template("index.html")

# Student & Teacher Login Routes
@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        email = request.form.get('studentEmail')
        password = request.form.get('studentPassword')

        # Check if user exists in database
        user = User.query.filter_by(email=email, role='student').first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('student_dashboard'))  # Redirect to student dashboard
        else:
            flash('Invalid email or password', 'danger')

    return render_template('student-login.html')


@app.route('/student-dashboard')
@login_required
def student_dashboard():
    return render_template('student-dashboard.html')


@app.route('/teacher-login', methods=['GET', 'POST'])
def teacher_login():
    return render_template('teacher-login.html')

if __name__ == '__main__':
    app.run(debug=True)

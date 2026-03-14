from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from shared.database.models import User
from shared.utils.syllabus import get_syllabus_for_level, get_random_suggestions

module1_bp = Blueprint('module1', __name__)

@module1_bp.route('/')
def home():
    return render_template('module1_ui/frontend/home.html')

@module1_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.objects(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('module1.dashboard'))
        flash('Invalid credentials')
    return render_template('module1_ui/frontend/login.html')

@module1_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        academic_level = request.form.get('academic_level', 'high_school')
        
        if User.objects(username=username).first():
            flash('Username already exists')
            return redirect(url_for('module1.register'))
        
        user = User(username=username, email=email, academic_level=academic_level)
        user.set_password(password)
        user.save()
        
        login_user(user)
        return redirect(url_for('module1.dashboard'))
    return render_template('module1_ui/frontend/register.html')

@module1_bp.route('/dashboard')
@login_required
def dashboard():
    syllabus = get_syllabus_for_level(current_user.academic_level)
    suggestions = get_random_suggestions(current_user.academic_level, 5)
    return render_template('module1_ui/frontend/dashboard_new.html', 
                         syllabus=syllabus, 
                         suggestions=suggestions)

@module1_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('module1.home'))

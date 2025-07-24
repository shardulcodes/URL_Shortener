# app/routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import get_db
import re

auth_bp = Blueprint('auth', __name__)

# Password strength validator
def is_strong_password(password):
    """
    Validate password strength:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character
    """
    pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )
    return pattern.match(password)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        db = get_db()

        if not is_strong_password(password):
            flash("Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.")
            return render_template('register.html')

        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password))
            )
            db.commit()
            flash("✅ Registration successful. Please log in.")
            return redirect(url_for('auth.login'))
        except db.IntegrityError:
            flash("❌ Username already taken.")
    
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash("✅ Logged in successfully.")
            return redirect(url_for('shortener.home'))
        else:
            flash("❌ Invalid username or password.")
    
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("👋 Logged out successfully.")
    return redirect(url_for('shortener.home'))

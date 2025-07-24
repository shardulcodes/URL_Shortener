# app/routes/shortener.py

import string, random
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import get_db

shortener_bp = Blueprint('shortener', __name__)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@shortener_bp.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    if request.method == 'POST':
        original_url = request.form['original_url']
        custom_code = request.form.get('custom_code')
        user_id = session.get('user_id')  # None for anonymous

        if custom_code:
            # Check if custom_code already exists
            existing = db.execute("SELECT * FROM urls WHERE short_code = ?", (custom_code,)).fetchone()
            if existing:
                flash("Custom short code already taken. Choose another.")
                return redirect(url_for('shortener.home'))
            short_code = custom_code
        else:
            # Auto-generate short_code until it's unique
            while True:
                short_code = generate_short_code()
                if not db.execute("SELECT 1 FROM urls WHERE short_code = ?", (short_code,)).fetchone():
                    break

        db.execute(
            "INSERT INTO urls (original_url, short_code, user_id) VALUES (?, ?, ?)",
            (original_url, short_code, user_id)
        )
        db.commit()

        return render_template("result.html", short_code=short_code)

    return render_template("home.html")


@shortener_bp.route('/<short_code>')
def redirect_to_original(short_code):
    db = get_db()
    result = db.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()

    if result:
        return redirect(result['original_url'])
    else:
        flash("Invalid short URL.")
        return redirect(url_for('shortener.home'))

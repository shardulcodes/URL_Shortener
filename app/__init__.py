# app/__init__.py

from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Security key for sessions and forms
    app.config['SECRET_KEY'] = 'your-very-secret-key'  # Change before production

    # SQLite database location
    app.config['DATABASE'] = os.path.join(app.root_path, '..', 'app.db')

    # Register blueprints
    from .routes.shortener import shortener_bp
    app.register_blueprint(shortener_bp)

    return app

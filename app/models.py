import sqlite3
import os
from flask import current_app, g

def get_db():
    """Get a database connection (per request)."""
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row  # Access rows like dicts
    return g.db

def close_db(e=None):
    """Close the DB connection after request."""
    db = g.pop('db', None)
    if db:
        db.close()

def init_db():
    """Initialize the database from schema.sql."""
    # Adjust path depending on where you keep schema.sql
    with current_app.open_resource('schema.sql') as f:
        get_db().executescript(f.read().decode('utf8'))

def init_app(app):
    app.teardown_appcontext(close_db)

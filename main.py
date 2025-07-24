from flask import Flask
from app.routes.shortener import shortener_bp
from app.routes.auth import auth_bp
from app.models import init_db
import os

app = Flask(
    __name__,
    template_folder=os.path.join("app", "templates"),
    static_folder=os.path.join("app", "static")
)

app.secret_key = "your_secret_key"

# ✅ Set the database path
app.config["DATABASE"] = os.path.join(os.getcwd(), "app.db")

# ✅ Register Blueprints
app.register_blueprint(shortener_bp)
app.register_blueprint(auth_bp)

# ✅ Initialize DB if needed
with app.app_context():
    init_db()  # make sure this function exists in models.py

if __name__ == '__main__':
    app.run(debug=True)

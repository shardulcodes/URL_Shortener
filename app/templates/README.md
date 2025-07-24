Absolutely, here's the **revised `README.md`** with **no emojis**, written professionally and thoroughly:

---

```markdown
# URL Shortener Web Application

A modern, secure, and user-friendly web application built with **Flask** that allows users to shorten long URLs, create custom aliases, and manage their own personalized dashboard with authentication.

---

## Features

### Authentication

- Secure user registration and login using password hashing.
- Real-time client-side password strength feedback.
- Password policy enforcement for security best practices.

### URL Shortening

- Anonymous users can shorten URLs instantly.
- Authenticated users can generate **custom shortcodes**.
- Unique short URL generation using hash-based logic.

### User Dashboard

- Personalized dashboard for each logged-in user.
- Manage, delete, and view all previously created links.

### Technology Stack

- **Backend:** Python, Flask, SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Security:** Password hashing with Werkzeug, client-side password validation
- **UI Styling:** Responsive design, Font Awesome icons

---

## Project Structure
```

url-shortener/
├── app/
│ ├── **init**.py
│ ├── models.py
│ ├── routes/
│ │ ├── auth.py
│ │ └── shortener.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── dashboard.html
│ │ └── result.html
│ └── static/
│ ├── css/
│ │ ├── base.css
│ │ ├── home.css
│ │ ├── login.css
│ │ ├── register.css
│ │ ├── dashboard.css
│ │ └── result.css
│ └── images/
├── main.py
├── app.db
├── schema.sql
├── requirements.txt
├── tests/
│ ├── test_auth.py
│ └── test_shortener.py
└── README.md

````

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
flask --app main init-db
```

### 5. Start the Development Server

```bash
flask --app main run
```

Open `http://127.0.0.1:5000` in your web browser.

---

## Testing

To run all available unit tests:

```bash
pytest
```

Tests include:

- Authentication functionality
- URL shortening logic
- Database schema integrity

---

## Password Policy

During registration, passwords must satisfy the following:

- At least 8 characters long
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 digit
- At least 1 special character from `@$!%*?&`
- Password and confirm password must match

Real-time feedback is provided on the frontend using JavaScript and Font Awesome icons.

---

## Security Highlights

- Passwords are stored securely using salted hashing (`generate_password_hash`)
- Sessions are securely managed and cleared upon logout
- Inputs are validated and sanitized
- Custom URLs and routes are protected for authenticated users

---

## Future Enhancements

- Link expiration settings (e.g., one-time, 7-day expiry)
- Analytics: click tracking and access logs
- Email-based account verification
- Rate limiting and abuse prevention
- Docker support for containerized deployment

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Shardul Shekatkar**
Final Year, B.Tech Computer Science (Cybersecurity)
GitHub: [github.com/shardulcodes](https://github.com/shardulcodes)

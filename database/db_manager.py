import sqlite3
import hashlib
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "iris_app.db")

def get_db_connection():
    """Create or connect to the SQLite database."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str) -> str:
    """Hash password using SHA-256 with salt."""
    salt = "iris_species_ai_salt_2026"
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def init_db():
    """Initialize database tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'User',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Login history table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        email TEXT NOT NULL,
        login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL,
        ip_info TEXT DEFAULT '127.0.0.1 (Localhost)',
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # Prediction history table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prediction_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT NOT NULL,
        sepal_length REAL NOT NULL,
        sepal_width REAL NOT NULL,
        petal_length REAL NOT NULL,
        petal_width REAL NOT NULL,
        model_used TEXT NOT NULL,
        predicted_species TEXT NOT NULL,
        confidence REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Seed a demo admin user if not exists
    cursor.execute("SELECT * FROM users WHERE email = ?", ("admin@iris.ai",))
    if not cursor.fetchone():
        demo_pwd_hash = hash_password("Admin@123")
        cursor.execute(
            "INSERT INTO users (fullname, email, password_hash, role) VALUES (?, ?, ?, ?)",
            ("System Administrator", "admin@iris.ai", demo_pwd_hash, "Admin")
        )
        
    conn.commit()
    conn.close()

def register_user(fullname: str, email: str, password: str) -> tuple[bool, str]:
    """Register a new user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE LOWER(email) = ?", (email.lower().strip(),))
        if cursor.fetchone():
            return False, "An account with this email already exists."
        
        pwd_hash = hash_password(password)
        cursor.execute(
            "INSERT INTO users (fullname, email, password_hash) VALUES (?, ?, ?)",
            (fullname.strip(), email.lower().strip(), pwd_hash)
        )
        conn.commit()
        return True, "Account registered successfully! Please log in."
    except Exception as e:
        return False, f"Registration error: {str(e)}"
    finally:
        conn.close()

def verify_user(email: str, password: str) -> tuple[bool, dict | None, str]:
    """Verify user credentials and log attempt."""
    conn = get_db_connection()
    cursor = conn.cursor()
    email_clean = email.lower().strip()
    try:
        cursor.execute("SELECT * FROM users WHERE LOWER(email) = ?", (email_clean,))
        user = cursor.fetchone()
        
        if not user:
            # Log failed attempt
            cursor.execute(
                "INSERT INTO login_history (email, status) VALUES (?, ?)",
                (email_clean, "Failed - User Not Found")
            )
            conn.commit()
            return False, None, "No account found with this email."
        
        pwd_hash = hash_password(password)
        if user["password_hash"] == pwd_hash:
            # Log successful login
            cursor.execute(
                "INSERT INTO login_history (user_id, email, status) VALUES (?, ?, ?)",
                (user["id"], email_clean, "Success")
            )
            conn.commit()
            user_dict = {
                "id": user["id"],
                "fullname": user["fullname"],
                "email": user["email"],
                "role": user["role"]
            }
            return True, user_dict, "Login successful!"
        else:
            cursor.execute(
                "INSERT INTO login_history (user_id, email, status) VALUES (?, ?, ?)",
                (user["id"], email_clean, "Failed - Incorrect Password")
            )
            conn.commit()
            return False, None, "Invalid email or password."
    except Exception as e:
        return False, None, f"Login error: {str(e)}"
    finally:
        conn.close()

def reset_password(email: str, new_password: str) -> tuple[bool, str]:
    """Reset user password."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE LOWER(email) = ?", (email.lower().strip(),))
        user = cursor.fetchone()
        if not user:
            return False, "Email address not found in system."
        
        pwd_hash = hash_password(new_password)
        cursor.execute("UPDATE users SET password_hash = ? WHERE id = ?", (pwd_hash, user["id"]))
        conn.commit()
        return True, "Password reset successfully. You can now log in with your new password."
    except Exception as e:
        return False, f"Reset error: {str(e)}"
    finally:
        conn.close()

def log_prediction(user_email: str, sl: float, sw: float, pl: float, pw: float, model: str, species: str, conf: float):
    """Save prediction to database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO prediction_history 
        (user_email, sepal_length, sepal_width, petal_length, petal_width, model_used, predicted_species, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_email, sl, sw, pl, pw, model, species, conf))
        conn.commit()
    finally:
        conn.close()

def get_prediction_history(user_email: str = None, search: str = "", limit: int = 100):
    """Retrieve prediction history with optional search and filters."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM prediction_history WHERE 1=1"
        params = []
        if user_email:
            query += " AND user_email = ?"
            params.append(user_email)
        if search:
            query += " AND (predicted_species LIKE ? OR model_used LIKE ? OR user_email LIKE ?)"
            s_param = f"%{search}%"
            params.extend([s_param, s_param, s_param])
        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()

def get_login_history(user_email: str = None, limit: int = 50):
    """Retrieve login history."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if user_email:
            cursor.execute("SELECT * FROM login_history WHERE email = ? ORDER BY login_time DESC LIMIT ?", (user_email, limit))
        else:
            cursor.execute("SELECT * FROM login_history ORDER BY login_time DESC LIMIT ?", (limit,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()

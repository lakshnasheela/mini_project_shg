# ============================================================
# SHG Smart Assistant - Main Flask Application
# Thanjavur Edition | Tamil + English + Tanglish
# XAMPP MySQL Compatible (uses PyMySQL)
# ============================================================

# MUST be the very first import - installs PyMySQL as MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

import os
from flask import (Flask, render_template, request, redirect,
                   url_for, session, jsonify, flash)
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from chatbot.engine import get_bot_response
from chatbot.language import detect_language


# ============================================================
# App Initialization
# ============================================================
app = Flask(__name__)
app.config.from_object(Config)

# MySQL Configuration (from config.py / .env)
app.config["MYSQL_HOST"] = Config.MYSQL_HOST
app.config["MYSQL_USER"] = Config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = Config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = Config.MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# ============================================================
# Helper Functions
# ============================================================
def get_db():
    """Returns a new MySQL cursor."""
    return mysql.connection.cursor()


# ============================================================
# Home Route
# ============================================================
@app.route("/")
def home():
    """Redirect to chat if logged in, else to login page."""
    if "user_id" in session:
        return redirect(url_for("chat"))
    return redirect(url_for("login"))


# ============================================================
# Authentication Routes
# ============================================================
@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration."""
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]
        lang = request.form.get("lang", "tanglish")

        # Validate fields
        if not username or not email or not password:
            flash("All fields required / எல்லா புலங்களும் தேவை.", "error")
            return redirect(url_for("register"))

        # Check for existing user
        cur = get_db()
        cur.execute(
            "SELECT id FROM users WHERE username=%s OR email=%s",
            (username, email)
        )
        if cur.fetchone():
            cur.close()
            flash("Username or email already exists / ஏற்கனவே உள்ளது.", "error")
            return redirect(url_for("register"))

        # Hash password and insert
        pw_hash = generate_password_hash(password)
        cur.execute(
            "INSERT INTO users (username, email, password_hash, preferred_lang) "
            "VALUES (%s, %s, %s, %s)",
            (username, email, pw_hash, lang)
        )
        mysql.connection.commit()
        cur.close()

        flash("Registered successfully! Please login / வெற்றிகரமாக பதிவு!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        # Fetch user
        cur = get_db()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        # Verify credentials
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["lang"] = user.get("preferred_lang", "tanglish")
            return redirect(url_for("chat"))

        flash("Invalid credentials / தவறான விவரங்கள்.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Clear session and redirect to login."""
    session.clear()
    return redirect(url_for("login"))


# ============================================================
# Chat Routes
# ============================================================
@app.route("/chat")
def chat():
    """Render chat UI with conversation history."""
    if "user_id" not in session:
        return redirect(url_for("login"))

    cur = get_db()

    # Load all conversations for sidebar
    cur.execute(
        "SELECT id, title, created_at FROM conversations "
        "WHERE user_id=%s ORDER BY created_at DESC",
        (session["user_id"],)
    )
    convos = cur.fetchall()

    # Load specific conversation if cid is provided
    conversation_id = request.args.get("cid", type=int)
    messages = []

    if conversation_id:
        # Verify ownership
        cur.execute(
            "SELECT * FROM conversations WHERE id=%s AND user_id=%s",
            (conversation_id, session["user_id"])
        )
        if cur.fetchone():
            cur.execute(
                "SELECT sender, content, created_at FROM messages "
                "WHERE conversation_id=%s ORDER BY id ASC",
                (conversation_id,)
            )
            messages = cur.fetchall()
        else:
            conversation_id = None

    cur.close()

    return render_template(
        "index.html",
        convos=convos,
        messages=messages,
        current_cid=conversation_id,
        lang=session.get("lang", "tanglish")
    )


# ============================================================
# API Routes - Language
# ============================================================
@app.route("/api/set_lang", methods=["POST"])
def set_lang():
    """Change user's preferred language."""
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    lang = request.get_json().get("lang", "tanglish")
    if lang not in ("tamil", "english", "tanglish"):
        lang = "tanglish"

    session["lang"] = lang

    # Update in DB
    cur = get_db()
    cur.execute(
        "UPDATE users SET preferred_lang=%s WHERE id=%s",
        (lang, session["user_id"])
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"ok": True, "lang": lang})


# ============================================================
# API Routes - Chat
# ============================================================
@app.route("/api/new_chat", methods=["POST"])
def new_chat():
    """Create a new empty conversation."""
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    cur = get_db()
    cur.execute(
        "INSERT INTO conversations (user_id, title, language) VALUES (%s, %s, %s)",
        (session["user_id"], "New Chat", session.get("lang", "tanglish"))
    )
    mysql.connection.commit()
    cid = cur.lastrowid
    cur.close()

    return jsonify({"conversation_id": cid})


@app.route("/api/send", methods=["POST"])
def send_message():
    """Handle user message and return bot response."""
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json()
    message = (data.get("message") or "").strip()
    cid = data.get("conversation_id")
    forced_lang = data.get("lang")

    if not message:
        return jsonify({"error": "empty message"}), 400

    # Decide language
    if forced_lang in ("tamil", "english", "tanglish"):
        lang = forced_lang
    elif session.get("lang") in ("tamil", "english", "tanglish"):
        lang = session["lang"]
    else:
        lang = detect_language(message)

    cur = get_db()

    # Create conversation if this is the first message
    if not cid:
        cur.execute(
            "INSERT INTO conversations (user_id, title, language) VALUES (%s, %s, %s)",
            (session["user_id"], message[:40], lang)
        )
        mysql.connection.commit()
        cid = cur.lastrowid
    else:
        # Verify conversation belongs to user
        cur.execute(
            "SELECT title FROM conversations WHERE id=%s AND user_id=%s",
            (cid, session["user_id"])
        )
        row = cur.fetchone()
        if not row:
            cur.close()
            return jsonify({"error": "invalid conversation"}), 403

        # Update title if still default
        if row["title"] == "New Chat":
            cur.execute(
                "UPDATE conversations SET title=%s WHERE id=%s",
                (message[:40], cid)
            )
            mysql.connection.commit()

    # Save user message
    cur.execute(
        "INSERT INTO messages (conversation_id, sender, content) VALUES (%s, %s, %s)",
        (cid, "user", message)
    )
    mysql.connection.commit()

    # Get bot reply
    reply = get_bot_response(message, preferred_lang=forced_lang)

    # Save bot message
    cur.execute(
        "INSERT INTO messages (conversation_id, sender, content) VALUES (%s, %s, %s)",
        (cid, "bot", reply)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({
        "reply": reply,
        "conversation_id": cid,
        "lang": lang
    })


@app.route("/api/delete_chat/<int:cid>", methods=["DELETE"])
def delete_chat(cid):
    """Delete a conversation (and its messages via CASCADE)."""
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    cur = get_db()
    cur.execute(
        "DELETE FROM conversations WHERE id=%s AND user_id=%s",
        (cid, session["user_id"])
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"ok": True})


# ============================================================
# Run Server
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
import datetime
import pytz

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, success


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///volunteers.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET"])
@login_required
def index():
    try:
        data = db.execute("SELECT username, location, subject, day, time, month, id FROM openings WHERE status = 'open' ORDER BY location")
        return render_template("index.html", data=data)
    except:
        return render_template("index.html")


@app.route("/history", methods=["GET"])
@login_required
def history():
    try:
        data = db.execute("SELECT location, level, subject, timing FROM history WHERE username in (SELECT username FROM users WHERE id = ?)", session["user_id"])
        return render_template("history.html", data=data)
    except:
        return render_template("history.html")


@app.route("/join", methods=["POST"])
@login_required
def join():
    id = request.form.get("id")
    data = db.execute("SELECT level, location, subject, day, time, month, id FROM openings WHERE id = ?", id)[0]

    # update index
    db.execute("UPDATE openings SET status = 'closed' WHERE id = ?", id)

    # update history
    timing = datetime.datetime.now(pytz.timezone("Asia/Singapore"))
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
    db.execute("INSERT INTO history(username, location, level, subject, timing) VALUES (?, ?, ?, ?, ?)", username, data["location"], data["level"], data["subject"], timing)
    return redirect("/")

@app.route("/post", methods=["GET", "POST"])
@login_required
def post():
    levels = ["Primary 1", "Primary 2", "Primary 3", "Primary 4", "Primary 5", "Primary 6", "Secondary 1", "Secondary 2", "Secondary 3", "Secondary 4"]
    if request.method == "POST":
        location = request.form.get("location")
        level = request.form.get("level") # change the width of level
        subject = request.form.get("subject") # if got time, create list of subjects (so that math and mathematics are not different values)
        day = request.form.get("day")
        time = request.form.get("time")
        month = request.form.get("month")
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]

        # check if all fields are inputted
        if not location or not level or not subject or not day or not time or not month:
            return apology("Error: Please fill in all fields.", "post.html")
        db.execute("INSERT INTO openings(username, level, location, subject, day, time, month, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", username, level, location, subject, day, time, month, 'open')
        return success("Successfully added!", "post.html")
    else:
        return render_template("post.html", levels=levels)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Error: Must provide username.", "login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Error: Must provide password.", "login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Error: Invalid username and/or password.", "login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        if not email or not username or not password:
            return apology("Error: Cannot leave any fields blank.", "register.html")
        elif "@" not in email:
            return apology("Error: Invalid email.", "register.html")
        elif len(password) < 9:
            return apology("Error: Password too short.", "register.html")

        # check if username is already registered.
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return apology("Error: Username already registered. Choose another one", "register.html")

        db.execute("INSERT INTO users(email, username, hash) VALUES (?, ?, ?)", email, username, generate_password_hash(password))
        return redirect("/")
    else:
        return render_template("register.html")

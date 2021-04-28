# libraries to work with data

# web app libraries
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# helper functions
from helpers import load_specimens_TEST

# error handeling
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)
app.secret_key='hello'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# loading in test data
specs = load_specimens_TEST()


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


### beginning of app routes ### 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method =="POST":
        return 'TODO'
    else:
        return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method =="POST":
        return 'TODO'
    else:
        return render_template("login.html")

@app.route("/entry", methods=["GET", "POST"])
def entry():
    if request.method == "POST":
        return 'TODO'
    else:
        return render_template('entry.html', specimens=specs)

@app.route("/past_entry", methods=["GET", "POST"])
def past_entry():
    if request.method == "POST":
        
        return render_template('past_entry.html')
    else:
        return render_template('past_entry.html')

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        return 'TODO'
    else:
        return render_template('test.html')

# [https://flask.palletsprojects.com/en/1.1.x/errorhandling/]
@app.errorhandler(Exception)
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return render_template('error.html', name = e.name, code = e.code)

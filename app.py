# libraries to work with data

# web app libraries
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# helper functions
from helpers import load_specimens_TEST, short_analysis, keyword_concord
from json import dumps

# error handeling
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

#speech recognition
import speech_recognition as sr

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
    text_file = ""
    t_analysis = ""
    
    if request.method == "POST":
        # print('in post')
        if "file" not in request.files:
            # print('no file')
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            # print('no file name')
            return redirect(request.url)

        if file:
            text_file = file.read()
            # print(text_file)
            t_analysis, _ = keyword_concord(str(text_file))

            #t_analysis = short_analysis(transcript)
        return render_template('entry.html', specimens=specs, j_spec = dumps(specs), description=text_file, t_analysis=t_analysis)
    else:
        return render_template('entry.html', specimens=specs, j_spec = dumps(specs), description=text_file, t_analysis=t_analysis)

@app.route("/text_rec", methods=["GET", "POST"])
def text_rec():
    text_file = ""
    t_analysis = ""

    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            print(file.filename)
            text_file = file.read()
            print('read')
            t_analysis = keyword_concord(str(text_file))
            # print(text_file)
            print('read2')


            # t_analysis = short_analysis(transcript)

    return render_template('text_rec.html', description=literal_eval(text_file), t_analysis=t_analysis)

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

@app.route("/speech_rec", methods=["GET", "POST"])
def speech_rec():
    transcript = ""
    t_analysis = ""

    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            t_analysis = short_analysis(transcript)

    return render_template('speech_rec.html', transcript=transcript, t_analysis=t_analysis)


# [https://flask.palletsprojects.com/en/1.1.x/errorhandling/]
@app.errorhandler(Exception)
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return render_template('error.html', name = e.name, code = e.code)

from flask import Flask,redirect
from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import session
import database as db
import authentication
import logging

app = Flask(__name__)

app.secret_key = b"s@g@d@c0ff33!"

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

navbar = """
        <a href="/">Home</a> | <a href="/aboutus">About Us</a> |
        <a href="/signup">Signup</a> | <a href="/login">Login</a>
        <p/>
        """
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/auth",methods=["GET","POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    is_successful, user=authentication.login(username, password)
    app.logger.info("%s",is_successful)
    if (is_successful):
        session["user"]=user
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/")
def index():
    return render_template("home.html",page="Home")

@app.route ("/aboutus")
def aboutus():
    return render_template("aboutus.html",page="About Us")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html",page="Calendar")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html",page="Chat with Us!")

@app.route("/account")
def account():
    return render_template("account.html",page="My Account")

@app.route("/signup")
def signup():
    return render_template("signup.html",page="Signup")

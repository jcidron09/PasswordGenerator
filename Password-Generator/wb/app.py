from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from datetime import datetime
import time
import Password_Generator
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
app.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(app)

class passwords(db.Model):
    _id_ = db.Column("id", db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    def __init__(self, content):
        self.content = content

generated_passwords = []
@app.route("/menu", methods=['GET', 'POST'])
def menu():
    # 8 booleans: all, lowercase, uppercase, alpha, digits, alphanumerics, punctuation, specials
    print(session.items())
    allowed_characters = [0, False, False, False, False, False, False, False, False]
    if request.method == 'POST':
        allowed_characters[0] = int(request.form["limit"])
        user_values = request.form.getlist("characters")
        if "all" in user_values:
            allowed_characters[1] = True
        if "lowercase" in user_values:
            allowed_characters[2] = True
        if "uppercase" in user_values:
            allowed_characters[3] = True
        if "alphas" in user_values:
            allowed_characters[4] = True
        if "digits" in user_values:
            allowed_characters[5] = True
        if "alphanumerics" in user_values:
            allowed_characters[6] = True
        if "punctuation" in user_values:
            allowed_characters[7] = True
        if "specials" in user_values:
            allowed_characters[8] = True
        this_password = Password_Generator.create_password(allowed_characters[0], allowed_characters[1], allowed_characters[2], allowed_characters[3], allowed_characters[4], allowed_characters[5], allowed_characters[6], allowed_characters[7], allowed_characters[8])
        generated_passwords.append(this_password)
        print(this_password)
        password_tba = passwords(this_password)
        db.session.add(password_tba)
        db.session.commit()
        print(session.items())
    return render_template("menu.html")


@app.route("/generator", methods= ['POST', 'GET'])
def generator():
    return render_template("generator.html", content= str(passwords.query.all()))

@app.route("/")
def home():
    print(session.items())
    return render_template("index.html", content= "")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["nm"]
        session["user"] = username
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")



@app.route("/user")
def user():
    if "user" in session:
        username = session["user"]
        return f"<h1>{username}</h1>"
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0")
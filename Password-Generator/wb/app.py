from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import Password_Generator
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
app.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(app)

generated_passwords = []


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))


@app.route("/")
def home():
    print(session.items())
    return render_template("index.html", num_passwords=db.session.query(Password).count())


@app.route("/menu", methods=['GET', 'POST'])
def menu():
    # 8 booleans: all, lowercase, uppercase, alpha, digits, alphanumerics, punctuation, specials
    print(session.items())
    characters = [0, False, False, False, False, False, False, False, False]

    if request.method == 'POST':
        characters[0] = int(request.form["limit"])
        user_values = request.form.getlist("characters")
        if "all" in user_values:
            characters[1] = True
        if "lowercase" in user_values:
            characters[2] = True
        if "uppercase" in user_values:
            characters[3] = True
        if "alphas" in user_values:
            characters[4] = True
        if "digits" in user_values:
            characters[5] = True
        if "alphanumerics" in user_values:
            characters[6] = True
        if "punctuation" in user_values:
            characters[7] = True
        if "specials" in user_values:
            characters[8] = True
        this_password = Password_Generator.create_password(characters[0], characters[1], characters[2], characters[3],
                                                           characters[4], characters[5], characters[6], characters[7],
                                                           characters[8])
        print(this_password)
        if this_password is None:
            this_password = ""
        print("this_password: " + this_password)
        password_tba = Password(password=this_password)
        generated_passwords.append(this_password)
        session["passwords"] = generated_passwords
        db.session.add(password_tba)
        db.session.commit()

        all_passwords = Password.query.all()
        for item in all_passwords:
            print(item.password)

    return render_template("menu.html")


@app.route("/word_generator", methods= ['POST', 'GET'])
def word_generator():
    if request.method == 'POST':
        word_amount = int(request.form["word_limit"])
        this_password = Password_Generator.create_word_password(word_amount)
        if this_password is None:
            this_password = ""
        password_tba = Password(password=this_password)
        generated_passwords.append(this_password)
        session["passwords"] = generated_passwords
        db.session.add(password_tba)
        db.session.commit()
    return render_template("word_generator.html")


@app.route("/generated_passwords", methods=['POST', 'GET'])
def generated():
    if "passwords" in session.keys():
        for password in session["passwords"]:
            if password is None:
                session["passwords"].remove(password)
    recent_passwords = ""
    if "passwords" in session.keys():
        for item in session["passwords"]:
            if item is not None:
                recent_passwords += item + "<br>"
            else:
                continue
    else:
        recent_passwords += "No passwords!"

    all_passwords = ""
    password_list = Password.query.all()
    for item in password_list:
        if item is None:
            db.session.delete(item)
            db.session.commit()
        else:
            all_passwords += item.password
            all_passwords += "<br>"

    return render_template("generated_passwords.html", recent_passwords=recent_passwords, all_passwords=all_passwords)


@app.route("/master", methods=['GET'])
def master():
    if request.method == 'GET':
        print(db.session.query(Password).delete())
        db.session.commit()
        return ""


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

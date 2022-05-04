from flask import Flask, render_template, request, session, redirect, url_for
from datetime import date, timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Entries.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
app.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    item = db.Column(db.String(1000))
    action = db.Column(db.String(1000))
    amount = db.Column(db.Integer)


@app.route("/")
def home():
    return render_template("index.html", content=read_database())


def read_database():
    table = """
    <table class="table">
        <tr>
          <th scope="col">id</th>
          <th scope="col">Date</th>
          <th scope="col">Item</th>
          <th scope="col">Action</th>
          <th scope="col">Amount</th>
        </tr>
            """
    print(Entry.query.count())
    row = 2
    for entry in Entry.query.all():
        table += (
                "\t\t<tr>\n" +
                "\t\t  <td>" + str(entry.id) + "</td>\n" +
                "\t\t  <td>" + str(entry.date) + "</td>\n" +
                "\t\t  <td>" + str(entry.item) + "</td>\n" +
                "\t\t  <td>" + str(entry.action) + "</td>\n" +
                "\t\t  <td>" + str(entry.amount) + "</td>\n" +
                "\t\t</tr>"
        )
    table += "</table>"
    print(table)
    return table


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    delete = str(input(""))
    if delete == "lol":
        for item in Entry.query.all():
            db.session.delete(item)
            db.session.commit()
    db.session.commit()

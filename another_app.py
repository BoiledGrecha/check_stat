from flask import Flask, request, render_template, session, redirect, url_for
from sqlalchemy import create_engine

app = Flask(__name__)
hashed = "XXXXXXXXXX"
DATABASE_URI = 'sqlite:///test.db'
engine = create_engine(DATABASE_URI)
app.config['SECRET_KEY'] = "XXXXXXXXXX"

@app.route('/', methods=['POST', 'GET'])
def hello():
    if "submit" in request.form and request.form["submit"]=="send":
        if request.form["passwd"] == hashed:
            session["passwd"] = hashed
    if "passwd" in session and session["passwd"] == hashed:
        return render_template("start.html",
            total1 = str(engine.execute("SELECT COUNT(id) as COUNT FROM saves").first()["COUNT"]),
            total2 = str(engine.execute("SELECT COUNT(mail) as COUNT FROM saves").first()["COUNT"]),
            total3 = str(engine.execute("SELECT COUNT(bonus_mail) as COUNT FROM saves").first()["COUNT"]))
    else:
        return render_template("nopass.html")

@app.route("/search", methods=["POST", "GET"])
def search():
    if "passwd" in session and session["passwd"] == hashed:
        if "submit" in request.form and request.form["submit"]=="search":
            a = engine.execute("SELECT * FROM saves WHERE mail LIKE '%{}%'".format(request.form["pattern"]))
            return render_template("search.html", object = a)
        else:
            return render_template("search.html")
    else:
        return redirect("185.159.82.99:7070")


if __name__ == "__main__":
    app.run(host='XXX.XXX.XXX.XXX', port=1010)

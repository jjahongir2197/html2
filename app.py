from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "admin": "1234"
}

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return "Login muvaffaqiyatli"
        else:
            return "Login xato"

    return render_template("index.html")

app.run(debug=True)

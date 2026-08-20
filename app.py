from flask import Flask, render_template

app = Flask(__name__)


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# INSURANCE PAGE
# -------------------------
@app.route("/insurance")
def insurance():
    return render_template("insurance.html")


# -------------------------
# COMPARE PAGE
# -------------------------
@app.route("/compare")
def compare():
    return render_template("compare.html")


# -------------------------
# BUY PAGE
# -------------------------
@app.route("/buy")
def buy():
    return render_template("buy.html")


# -------------------------
# REMINDERS PAGE
# -------------------------
@app.route("/reminders")
def reminders():
    return render_template("reminders.html")


# -------------------------
# EXERCISES PAGE
# -------------------------
@app.route("/exercises")
def exercises():
    return render_template("exercise.html")


# -------------------------
# RUN THE APPLICATION
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
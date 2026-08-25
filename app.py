#dbs prediction gg

from flask import Flask, render_template, request
import joblib

modelPKL = joblib.load("dbs.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    return (render_template("main.html"))

@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    return (render_template("dbs.html"))

@app.route("/result", methods=["GET", "POST"])
def result():
    q = float(request.form.get("q"))
    r = result = modelPKL.predict([[q]])
    return (render_template("result.html", r=r[0]))

if __name__ == "__main__":
    app.run(port=1563)                       

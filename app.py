#dbs prediction gg
1
from flask import Flask, render_template, request
import joblib
import os
from groq import Groq

#delete this line before syn

model = Groq()
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

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    return (render_template("chatbot.html"))

@app.route("/result", methods=["GET", "POST"])
def result():
    q = float(request.form.get("q"))
    r = result = modelPKL.predict([[q]])
    return (render_template("result.html", r=r[0]))

@app.route("/chatResult", methods=["GET", "POST"])
def chatResult():
    q = request.form.get("q")
    r = model.chat.completions.create(
  model="openai/gpt-oss-120b",
  messages=[
    {
      "role": "user","content": "q"
    }])
    return (render_template("chatResult.html", r = r.choices[0].message.content))

if __name__ == "__main__":
    app.run(port=1565)                       

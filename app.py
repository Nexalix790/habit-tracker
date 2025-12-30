from flask import Flask, render_template
from dotenv import load_dotenv
import os
import json

load_dotenv()

with open("config.json") as f:
    config = json.load(f)

app = Flask(__name__)
app.config["DEBUG"] = config["app"]["debug"]
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])

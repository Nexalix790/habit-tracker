from flask import Flask, render_template
from dotenv import load_dotenv
import os, sqlite3, json

# Create a cursor for exucuting SQL commands
db = sqlite3.connect("database.db")
cursor = db.cursor()
# Create a first request for generate a new table (USERS)
cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at DATE DEFAULT (DATE('now')),
    completed_today INTEGER DEFAULT 0
);
""")
db.commit()
db.close()

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

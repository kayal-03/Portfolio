from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__, static_folder="templates/static")
app.secret_key = "kayal_portfolio_secret"

def create_database():
    conn = sqlite3.connect("portfolio.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("portfolio.db")
    conn.execute(
        "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    conn.close()

    flash("Your message was sent successfully!")
    return redirect("/#contact")

if __name__ == "__main__":
    create_database()
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, message TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

# Simple logic-based chatbot response
def get_bot_response(user_message):
    message = user_message.lower()
    if "hello" in message:
        return "Hi! How can I help you today?"
    elif "price" in message:
        return "Please visit our pricing page for full details."
    elif "support" in message:
        return "You can reach our support team at support@example.com."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    bot_reply = get_bot_response(user_message)

    # Save chat to DB
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (user, message, timestamp) VALUES (?, ?, ?)", 
              ("user", user_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    c.execute("INSERT INTO messages (user, message, timestamp) VALUES (?, ?, ?)", 
              ("bot", bot_reply, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

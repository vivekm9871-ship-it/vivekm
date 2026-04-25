from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Health Monitoring Service 🚀"

@app.route("/status")
def status():
    return jsonify({
        "status": "UP",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
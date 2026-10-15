
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python DevOps App is Running!"

@app.route("/about")
def about():
    return "This application is built using Python and Flask."

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

@app.route("/contact")
def contact():
    return "Contact the Python DevOps team."
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "Version 1.0"

@app.route("/")
def home():
    return f"""
    <h1>Deploy and Rollback Automation</h1>
    <h2>{APP_VERSION}</h2>
    <p>My first cloud deployment using Flask.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION
    })

if __name__ == "__main__":
    app.run(debug=True)
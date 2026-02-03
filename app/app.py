app = Flask(Python Flask App)

@app.route("/")
def hello():
    return "Hello from Kubernetes 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
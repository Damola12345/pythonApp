from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "codebuild is working!, it's a web app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5045, debug=True)

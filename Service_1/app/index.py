from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def index():
    return json.dumps({"title": "test"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
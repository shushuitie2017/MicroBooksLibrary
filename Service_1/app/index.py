from flask import Flask
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(
    app
)
@app.route("/")
def index():

    return json.dumps({"title": "thanks"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)



#"headers": {"content-type":"application/json; charset=utf-8",
#                    "Access-Control-Allow-Origin": 'http://127.0.0.1:3000',
#                   "Access-Control-Allow-Headers": "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept" },
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/post/img", methods=["GET"])
def get_img_name():
    return request.args


@app.route("/callback", methods=['POST'])
def callback():
    return "post callback!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

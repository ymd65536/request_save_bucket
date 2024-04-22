import os
import rq_save_obj.gcs as gcs
from flask import Flask, request

app = Flask(__name__)


@app.route("/post/img", methods=["GET"])
def get_img_name():
    args_param = request.args
    download_url = args_param.get("url", None)

    if not download_url:
        return "URL is not found", 400
    else:
        res = gcs.save_obj(download_url)
        return res


@app.route("/callback", methods=['POST'])
def callback():
    return "post callback!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

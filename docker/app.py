import os
import rq_save_obj.gcs as gcs
import gemini_provision.image_to_text as image_to_text
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


@app.route("/img/provison", methods=["GET"])
def gemini_pro_vision():
    req = request.args
    year = req.get("year")
    month = req.get("month")
    img_name = req.get("img_name")

    gcs_file_path = f"gs://{year}/{month}/{img_name}"
    res = image_to_text.get_text(gcs_file_path)
    return res


@app.route("/callback", methods=['POST'])
def callback():
    return "post callback!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

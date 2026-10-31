from flask import Flask, render_template, request

from model import preprocess_img, predict_result

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def prediction():
    try:
        file = request.files["file"]
        if file.filename == "":
            return render_template("result.html", error="No file selected")
        batch = preprocess_img(file.stream)
        digit = predict_result(batch)
        return render_template("result.html", prediction=digit)
    except:
        print("error")

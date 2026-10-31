"""Flask web app that predicts a handwritten digit from an uploaded image."""
from flask import Flask, render_template, request

from model import preprocess_img, predict_result

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Show the upload form."""
    return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def prediction():
    """Predict the digit in the uploaded image and show the result."""
    try:
        file = request.files["file"]
        if file.filename == "":
            return render_template("result.html", error="No file selected")
        batch = preprocess_img(file.stream)
        digit = predict_result(batch)
        return render_template("result.html", prediction=digit)
    except (KeyError, OSError, ValueError):
        return render_template("result.html", error="Could not process the image")

from flask import Flask, render_template, request
from converter.detect import detect_pack_type
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["texturepack"]

    if file:
        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        pack_type = detect_pack_type(filepath)

        return f"Detected: {pack_type}"

    return "No file selected"


if __name__ == "__main__":
    app.run(debug=True)
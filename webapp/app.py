from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)
model = YOLO("models/best.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    result_path = None
    if request.method == "POST":
        file = request.files.get("video")
        if file:
            upload_path = "videos/uploaded.mp4"
            file.save(upload_path)
            model.predict(source=upload_path, save=True, project="outputs", name="web_predict")
            result_path = os.path.join("outputs", "web_predict")
    return render_template("index.html", result_path=result_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

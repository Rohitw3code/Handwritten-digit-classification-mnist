import cv2
import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, url_for, request, app, jsonify

app = Flask(__name__)

model = pickle.load(open("knnmodel.pk","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/digit_predict",methods=["POST"])
def predict_image():
    file = request.files['file']
    filename = file.filename
    if str(filename).strip():
        imgData = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        try:
            rsimg = cv2.resize(imgData, (8, 8))
            prediction = str(model.predict(rsimg.reshape(1, -1))[0])
            pred = "Prediction : The given image is "+prediction
            return render_template("home.html",prediction=pred,img_name=filename)
        except Exception as e:
            print("can not able to resize the image :(")
            return "can not able to resize the image :("

    else:
        return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)

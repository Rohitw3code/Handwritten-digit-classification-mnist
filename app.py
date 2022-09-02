#import cv2
import pandas as pd
import numpy as np
import pickle
from flask import Flask,render_template,url_for,request,app,jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")


if __name__ == "__main__":
	app.run(debug=True)

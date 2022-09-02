# -*- coding: utf-8 -*-
"""DigitMnist-Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LAlLOmyf9XE8m-m0QjD8HeGDwGqvGOrX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Load DataSet"""

from sklearn.datasets import load_digits
data = load_digits()

"""## Target Name"""

data["target_names"]

data.keys()

"""## Display an image from the dataset"""

plt.imshow(data.images[0])

plt.imshow(data.images[15])

"""## Display the value of the crossponding image at the position"""

data.target[15]

"""## Data to DataFrame with Target column"""

df = pd.DataFrame(data.data)
df["target"] = data.target

df.head()

"""## Split - data into Train-Test"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size=0.33, random_state=42)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_ss = scaler.fit_transform(X_train)
X_test_ss = scaler.transform(X_test)

model = knn.fit(X_train_ss,y_train)

pred = model.predict(X_test_ss)

"""## MSE and MAE"""

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

mean_squared_error(y_test,pred)

mean_absolute_error(y_test,pred)

"""## Accuracy Score"""

from sklearn.metrics import accuracy_score
accuracy_score(np.array(y_test),np.array(pred).astype(int))

import pickle

pickle.dump(model,open("knnmodel.pk","wb"))

md = pickle.load(open("knnmodel.pk","rb"))

md.predict(np.array(scaler.transform(X_test))[0].reshape(1,-1))

"""## Save image"""

i = 65
plt.imshow(data.images[i])
md.predict(data.images[i].reshape(1,-1))

cv2.imwrite("6n.png",data.images[i])

"""## import image and predict"""

import cv2
img_name = "6n.png"
img = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
plt.imshow(img)

img.shape

"""## resize the image"""

rsimg = cv2.resize(img,(8,8))

plt.imshow(rsimg)

md.predict(rsimg.reshape(1,-1))

md.predict(scaler.transform(rsimg.reshape(1,-1)))
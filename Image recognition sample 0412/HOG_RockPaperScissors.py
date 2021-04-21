# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:52:41 2019

@author: Alvin
"""

import cv2
import numpy as np
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import joblib
from sklearn.metrics import classification_report,accuracy_score
from imutils import paths
import argparse

resize_img = (300,300)

#使用參數方式傳入Training和Test的dataset
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--training", required=True, help="Path to the logos training dataset")
ap.add_argument("-t", "--test", required=True, help="Path to the test dataset")
args = vars(ap.parse_args())

classList=[]
images=[]

for imagePath in paths.list_images(args["training"]):
    classes = imagePath.split("0")[0].split("\\")[1]
    classList.append(classes)
    image = cv2.imread(imagePath)
    image = cv2.resize(image, resize_img) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    images.append(image)


features = np.array(images, 'int16')
labels = np.array(classList)
#print(features.shape, labels.shape)
list_hog_fd = []

for feature in features:
    fd = hog(feature, orientations=9, pixels_per_cell=(12, 12), cells_per_block=(8, 8), visualise=False)
    list_hog_fd.append(fd)

hog_features = np.array(list_hog_fd, 'float64')
#print(hog_features.shape)

X_train, X_test, y_train, y_test = train_test_split(
    hog_features,
    labels,
    test_size=0.2,
    shuffle=True,
    random_state=42,
)

clf = LinearSVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy: "+str(accuracy_score(y_test, y_pred)))
print(classification_report(y_test, y_pred))

joblib.dump(clf, "hog_svm.pkl", compress=3)

# Load the classifier
clf = joblib.load("hog_svm.pkl")

# Read the input image
imgs = []
files = []

for (i, imagePath) in enumerate(paths.list_images(args["test"])):
    image = cv2.imread(imagePath)
    image = cv2.resize(image, resize_img) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgs.append(image)
    files.append(imagePath.split("\\")[1])

pred_imgs = np.array(np.array(imgs),'int16')

for i, img in enumerate(pred_imgs):
    fd = hog(img, orientations=9, pixels_per_cell=(12, 12), cells_per_block=(8, 8), visualise=False)
    nbr = clf.predict(np.array([fd], 'float64'))
    print("{} ---> {}".format(files[i], nbr[0]))

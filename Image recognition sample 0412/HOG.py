# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:51:33 2019

@author: Alvin
"""

from skimage import exposure    #exposure可用來調整影像中像素的強度
from skimage import feature
import cv2

image = cv2.imread("Kobe-Bryant-Michael-Jordan.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# feature.hog除了傳回HOG資訊外，亦可傳回視覺化影像圖
(H, hogImage) = feature.hog(gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), transform_sqrt=True, visualise=True)

#調整影像強度範為介於0~255之間（rescale_intensity可將影像的像素強度進行壓縮或放大）
hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))

#數值類型更改為Unsigned Integer 8 bits
hogImage = hogImage.astype("uint8")

#顯示HOG視覺圖
cv2.imshow("HOG Image", hogImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
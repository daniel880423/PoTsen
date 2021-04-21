import cv2
import numpy as np

#讀入相片檔案
image = cv2.imread("license.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)
binaryIMG = cv2.Canny(blurred, 20, 150)

(cnts, _) = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)

i = 0
maxArea = 0
maxAreaIndex = 0
for c in cnts:        
    area = cv2.contourArea(c)  #計算面積
    if area > maxArea:
        maxArea = area
        maxAreaIndex = i  
    i = i + 1
    
mask = np.zeros(gray.shape, dtype="uint8")  #依Contours圖形建立mask
cv2.drawContours(mask, [cnts[maxAreaIndex]], -1, 255, -1) #255 →白色, -1→塗滿
   
cv2.imshow("Image", clone)
cv2.imshow("mask", mask)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("result", result)  

cv2.waitKey(0) 
cv2.destroyAllWindows()

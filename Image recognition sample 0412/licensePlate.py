import cv2
import sys
import numpy as np
import math
def nothing(x):
    pass

cv2.namedWindow('hsv_demo',cv2.WINDOW_NORMAL)
cv2.namedWindow('canny_demo',cv2.WINDOW_NORMAL)

sliderValue=0
sliderMaxValue = 255

cv2.createTrackbar('threshold', 'canny_demo', sliderValue,   100, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', sliderValue, 5, nothing)

cv2.createTrackbar('hl', 'hsv_demo', sliderValue, sliderMaxValue, nothing)
cv2.createTrackbar('hu', 'hsv_demo', sliderValue, sliderMaxValue, nothing)
cv2.createTrackbar('sl', 'hsv_demo', sliderValue, sliderMaxValue, nothing)
cv2.createTrackbar('su', 'hsv_demo', sliderValue, sliderMaxValue, nothing)
cv2.createTrackbar('vl', 'hsv_demo', sliderValue, sliderMaxValue, nothing)
cv2.createTrackbar('vu', 'hsv_demo', sliderValue, sliderMaxValue, nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("license.jpg")

while True:
    hl = cv2.getTrackbarPos('hl', 'hsv_demo')
    hu = cv2.getTrackbarPos('hu', 'hsv_demo')
    sl = cv2.getTrackbarPos('sl', 'hsv_demo')
    su = cv2.getTrackbarPos('su', 'hsv_demo')
    vl = cv2.getTrackbarPos('vl', 'hsv_demo')
    vu = cv2.getTrackbarPos('vu', 'hsv_demo')

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])
    
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("hsv_demo", result)
    
    threshold = cv2.getTrackbarPos('threshold', 'canny_demo')
    ratio = cv2.getTrackbarPos('increase_ratio', 'canny_demo')
    
    gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    edges = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, 3)
    cv2.imshow("canny_demo", edges)
    
    key = (cv2.waitKey(1) & 0xFF)
        
    newImage = image.copy()
    
    try:
        plines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 30, 1)
        for i in plines:
            print(plines)
        
            for pl in i:
                cv2.line(newImage, (pl[0], pl[1]), (pl[2], pl[3]), (255, 0, 0), 3)
                
        cv2.imshow("HoughLinesP", newImage)
        
        if key == ord("q"):
            cv2.imwrite("licensePlate.png", newImage)
            break
    
    except TypeError:
        print("The HoughlinesP function returns None, try decrease the threshold!")
        
cv2.destroyAllWindows()   


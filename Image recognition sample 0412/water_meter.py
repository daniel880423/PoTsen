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
    image = cv2.imread("wm3.jpg")

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
        plines = cv2.HoughLines(edges, 1, np.pi/180, 80)
        for lines in plines:
            for (rho, theta) in lines:
                x0 = np.cos(theta)*rho 
                y0 = np.sin(theta)*rho
                pt1 = ( int(x0 + (h+w)*(-np.sin(theta))), int(y0 + (h+w)*np.cos(theta)) )
                pt2 = ( int(x0 - (h+w)*(-np.sin(theta))), int(y0 - (h+w)*np.cos(theta)) )
                cv2.line(newImage, pt1, pt2, (0, 0, 255), 3) 

        cal = (math.atan((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))*180)%360
        print(cal)
        
        cv2.imshow("HoughLines", newImage)
        
        if key == ord("q"):
            cv2.imwrite("water_meter.png", newImage)
            break
    
    except TypeError:
        print("The Houghlines function returns None, try decrease the threshold!")
        
cv2.destroyAllWindows()   


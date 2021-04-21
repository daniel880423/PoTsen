import cv2
import sys
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('canny_demo',cv2.WINDOW_NORMAL)
cv2.createTrackbar('threshold',      'canny_demo', 0, 1000, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 200,  nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("test.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 10, 60])
upper = np.array([20, 150, 255])
  
binary = cv2.inRange(hsv, lower, upper)
    
test = cv2.bitwise_and(image,image, mask=binary)
    
cv2.imshow("preview", test) 

# convert RGB to Gray to Binary
gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
#(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

while True:
    newimage =image.copy()
    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')
    
    edges = cv2.GaussianBlur(gray, (9, 9), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=7)

    cv2.imshow("canny_demo", edges)
    
    (contours, _) = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(newimage, contours, -1, (0,255,0), 1)
    cv2.imshow("Contours", newimage)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):        
        break

cv2.destroyAllWindows()



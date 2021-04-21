import cv2
import numpy as np

#image = cv2.imread("lena256rgb.jpg")


cap = cv2.VideoCapture(0)
# Capture frame-by-frame

def nothing(x):
    pass

cv2.namedWindow('canny_demo')
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)

while True:
    ret, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of purple color in HSV
    lower = np.array([0, 10, 60])
    upper = np.array([20, 150, 255])
    
    # Threshold the HSV image to get only purple colors
    binary = cv2.inRange(hsv, lower, upper)

    bitwise_not = cv2.bitwise_not(binary)
    cv2.imshow("Bitwise_not", bitwise_not)
    
    bitwise_and = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("Bitwise_and", bitwise_and)
    
    binary = cv2.GaussianBlur(binary, (33, 33), 0)
      
    bitwise_and_blur = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("Bitwise_and_blue", bitwise_and_blur)
    
    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(binary, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=3)
    cv2.imshow("canny_demo", edges)
    
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


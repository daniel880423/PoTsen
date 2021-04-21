import cv2
import numpy as np

#image = cv2.imread("lena256rgb.jpg")


cap = cv2.VideoCapture(0)
# Capture frame-by-frame


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
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


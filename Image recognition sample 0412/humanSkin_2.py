import cv2 
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('org_demo', frame)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 58, 50])
    upper = np.array([30, 255, 255])
    
    # Threshold the HSV image to get only purple colors
    binary = cv2.inRange(hsv, lower, upper)
    bitwise_and = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("Bitwise_and", bitwise_and)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("gray_demo.png", bitwise_and)
        break

cap.release()
cv2.destroyAllWindows()   

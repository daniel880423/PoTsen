import cv2
import numpy as np

#image = cv2.imread("lena256rgb.jpg")

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# Capture frame-by-frame

cv2.namedWindow('Gaussian_Blur')
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 30, nothing)

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
    
    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')
    binary = cv2.GaussianBlur(binary, (2*ksize+1, 2*ksize+1), 0)
    cv2.imshow("Gaussian_Blur", binary)
    
    bitwise_and_blur = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("Bitwise_and_blur", bitwise_and_blur)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


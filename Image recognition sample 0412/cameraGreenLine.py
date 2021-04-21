import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# Capture frame-by-frame

def nothing(x):
    pass


cv2.namedWindow('canny_demo')
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)

while True:
    ret, frame = cap.read()
    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')    
    
    cv2.imshow("preview", frame)
    # Our operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=3)
    
    frame[edges != 0] = (0, 255, 0)
    
    cv2.imshow('canny_demo', frame)
       
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

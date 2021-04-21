import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# Capture frame-by-frame

def nothing(x):
    pass

cv2.namedWindow('Gaussian_Blur')
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 30, nothing)

cv2.namedWindow('canny_demo')
cv2.createTrackbar('threshold',      'canny_demo', 0, 150, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 10,  nothing)

while True:
    ret, frame = cap.read()
       
    cv2.imshow("preview", frame)
    # Our operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of purple color in HSV
    lower = np.array([0, 10, 60])
    upper = np.array([20, 150, 255])
    
    # Threshold the HSV image to get only purple colors
    binary = cv2.inRange(hsv, lower, upper)
    
    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')
    blurred = cv2.GaussianBlur(binary, (2*ksize+1, 2*ksize+1), 0)
    
    kernel = np.ones((35,35), np.uint8)
    erode  = cv2.erode(blurred, kernel, iterations=1)
    dilate = cv2.dilate(blurred, kernel, iterations=1)
    
    bitwise_and_blur = cv2.bitwise_and(frame, frame, mask=blurred)  
    
    cv2.imshow("Gaussian_Blur", bitwise_and_blur)

    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')
    binaryIMG = cv2.Canny(blurred, threshold, threshold * ratio, apertureSize=3)

    cv2.imshow("canny_demo", binaryIMG)
    
    #(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (cnts, _) = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    clone = frame.copy()
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
    try:
        cv2.drawContours(mask, [cnts[maxAreaIndex]], -1, 255, -1) #255 →白色, -1→塗滿
    except:
        pass
    
    #將mask與原圖形作AND運算
    cv2.imshow("Image + Mask", cv2.bitwise_and(frame, frame, mask=mask))              
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

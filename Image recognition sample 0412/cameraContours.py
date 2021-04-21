import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# Capture frame-by-frame

def nothing(x):
    pass



while True:
    ret, frame = cap.read()
       
    cv2.imshow("preview", frame)
    # Our operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    binaryIMG = cv2.Canny(blurred, 20, 160)
    
    #(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (cnts, _) = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    clone = frame.copy()
    cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
    
    for c in cnts:        
            mask = np.zeros(gray.shape, dtype="uint8")  #依Contours圖形建立mask
            cv2.drawContours(mask, [c], -1, 255, -1) #255 →白色, -1→塗滿
    
            # show the images
            cv2.imshow("Image", frame)
            cv2.imshow("Mask", mask)
    
    #將mask與原圖形作AND運算
            cv2.imshow("Image + Mask", cv2.bitwise_and(frame, frame, mask=mask))       
       
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

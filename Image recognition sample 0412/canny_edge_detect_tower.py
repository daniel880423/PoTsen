import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3,3), 0) # Denoise
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold*ratio,apertureSize=kernel_size) # Canny Edge Detect
    dst = cv2.bitwise_and(im, im, mask=detected_edges) # Get Edge Image With Color
    cv2.imshow('canny', dst)

# Settings
lowThreshold = 0 # Track Bar Start from State-0
max_lowThreshold = 100 # Track Bar End with State-100
ratio = 3 # threshold2 = threshold1 * ratio
kernel_size = 3 # Size of Sobel
# Running

im = cv2.imread('tower.jpg') # Read From File
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # GBR Convert To Gray
cv2.namedWindow('canny') # Create New Windo
CannyThreshold(0)

cv2.waitKey(0)
cv2.destroyAllWindows()   

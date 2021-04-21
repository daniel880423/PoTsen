import cv2
import sys
import numpy as np

imagePath = sys.argv[1]
image = cv2.imread(imagePath)
cv2.imshow("preview", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
count = 0

lower = np.array([11, 168, 0])
upper = np.array([32, 255, 255])

binary = cv2.inRange(hsv, lower, upper)
select = cv2.bitwise_and(image, image, mask=binary)

cv2.imshow("select", select)

for i in range(len(hsv)):
    for j in range(len(hsv[0])):
        if select[i,j,0]!=0 or select[i,j,1]!=0 or select[i,j,2]!=0:
            count = count + 1
            if hsv[i,j,2] * 1.5 > 255:
                hsv[i,j,2] = 255
            else:
                hsv[i,j,2] = hsv[i,j,2] * 1.5
 
print(count)
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
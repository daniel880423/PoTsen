import cv2
import sys

imagePath = sys.argv[1]
image = cv2.imread(imagePath)
cv2.imshow("preview", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
count = 0

for i in range(len(hsv)):
    for j in range(len(hsv[0])):
        if hsv[i,j,0]==0:
            count = count + 1
            if hsv[i,j,1] * 3 > 255:
                hsv[i,j,1] = 255
            else:
                hsv[i,j,1] = hsv[i,j,1] * 3

print(count)
image2 = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("preview2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
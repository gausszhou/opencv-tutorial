# BGR 
# 灰度图
import cv2

image = cv2.imread("./images/opencv_logo.jpg")

cv2.imshow("image", image)

cv2.imshow("blue", image[:,:,0])
cv2.imshow("green", image[:,:,1])
cv2.imshow("red", image[:,:,2])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray) # 灰度图

cv2.waitKey()
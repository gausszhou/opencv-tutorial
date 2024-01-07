# 裁剪

import cv2

image = cv2.imread("./images/opencv_logo.jpg")

# [行, 列]
crop = image[10:170, 40:200]

cv2.imshow("image", image)
cv2.imshow("crop", crop)

cv2.waitKey()
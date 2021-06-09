import cv2
import numpy as np

img = cv2.imread("images/6.jpg")
print(img.shape)

imgResize = cv2.resize(img, (400, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Imagei", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
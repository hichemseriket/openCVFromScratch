import cv2
import numpy as np
img = cv2.imread("images/5.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# cap = cv2.VideoCapture(imgGray)
cv2.imshow("Original image", img)
cv2.imshow("Garay image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)




# ma facon de couper l'appli en cliquant sur 'q'
# while True:
#     cv2.imshow("Hichem", imgGray)
#     key = cv2.waitKey(0) & 0xFF
#     if key == ord('q'):
#         break
# cv2.destroyAllWindows()
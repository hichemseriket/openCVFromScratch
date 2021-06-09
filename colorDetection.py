import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
# cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
# cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("Val Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("Hue Max", "HSV", 179, 179, empty)
# cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
# cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)
# mon briquet jaune fenetre ouvert
# cv2.createTrackbar("Hue Min", "HSV", 14, 179, empty)
# cv2.createTrackbar("Sat Min", "HSV", 88, 255, empty)
# cv2.createTrackbar("Val Min", "HSV", 126, 255, empty)
# cv2.createTrackbar("Hue Max", "HSV", 77, 179, empty)
# cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
# cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)
# mon briquet jaune fenetre fermé
cv2.createTrackbar("Hue Min", "HSV", 16, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 24, 255, empty)
cv2.createTrackbar("Val Min", "HSV", 124, 255, empty)
cv2.createTrackbar("Hue Max", "HSV", 73, 179, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)

while True:

    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])

    cv2.imshow("Horizontal Stacking", hStack)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
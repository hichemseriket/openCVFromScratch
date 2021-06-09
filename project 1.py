import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

# le premier mon briquet jaune, le second ma capsule violette, le troisieme mon tapis de priere vert,# le dernier est mon briquet rouge transparent
# pour ajouter des couleurs je doit les rajouter dans la liste myColors en les detectant en live avec le detecteur de couleur,
# puis rajouter leur correspondance dans la liste myColorValues pour dessiner la couleur
myColors = [[16, 24, 124, 73, 255, 255],
            [88, 75, 226, 148, 255, 255],
            [74, 51, 117, 109, 247, 255],
            [0, 103, 141, 179, 255, 255]]
#
myColorValues = [[64, 255, 255],
                 [255, 0, 255],
                 [0, 255, 0],
                 [0, 0, 255]]
myPoints = []  # [x, y, colorId]


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    # je prends l'element 0 correspond a jaune index 0
    # lower = np.array(myColors[0][0:3])
    # upper = np.array(myColors[0][3:6])
    # mask = cv2.inRange(imgHSV, lower, upper)
    # cv2.imshow("img", mask)
    # pour detecter mes 3 color je rajoute une boucle
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # str color donne un nom different a chaque fntre est correspond au premier element de chaque color
        # cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    # je fait une rotation de 180 pour ecrire droit ^^
    hichem = cv2.flip(imgResult, 180)

    cv2.imshow("Result", imgResult)
    cv2.imshow("Hichem Inversé", hichem)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

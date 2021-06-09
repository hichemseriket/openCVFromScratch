import cv2
import numpy as np

# pour detecté les visage j'utilise ici une methode créé par viola et jones
# pour detecter les visage je doit detecter plusieurs positives qui vont etre les images de visage et aussi detecter les negative qui vont etre tout sauf les images de visage
# j'utilise pour ça des models créé par opencv : les haarcascades
# la methode de cascade et vielle mais fonctionne toujours bien et elle est rapide dans certain circonstance
faceCascade = cv2.CascadeClassifier("models/haarcascade_frontalface_alt2.xml")
path = 'images/6.jpg'

img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# le 1.1 est le scalage , et le 4 est pour geré les voisin
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# pour chaque visage detecté je rajoute un rectangle
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Original", img)
cv2.waitKey(0)

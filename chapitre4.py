import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# print(img)
# img[200:400, 200:400] = 255, 0, 0
# img[200:400, 100:200] = 100, 50, 80
# img[100:200, 100:200] = 0, 255, 0
# img[0:100, 0:100] = 80, 100, 50
# img[400:512, 400:512] = 0, 0, 255

# tentative drapeau algerie
# img[0:512, 0:256] = 150, 255, 50
# img[0:512, 256:512] = 255, 255, 255

# j'ai fait des lines partant depuis le centre vers les coins
cv2.line(img, (0, 0), (256, 256), (0, 255, 0), 25)
cv2.line(img, (256, 256), (512, 512), (255, 0, 0), 25)
cv2.line(img, (256, 256), (512, 0), (0, 0, 255), 5)
cv2.line(img, (256, 256), (0, 512), (255, 255, 255), 5)
# trait blanc fin passe au milieu
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 255, 255), 3)

# je dessine des forme
# si je veux remplir le rectangle je remplace le 3 thikness par cv2.FILLED
cv2.rectangle(img, (0, 0), (256, 256), (255, 0, 0), 3)
cv2.circle(img, (256, 256), 50, (255, 255, 0), 5)

# mettre du tect
cv2.putText(img, "OPENCV", (300, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 150, 0), 1)
cv2.putText(img, "OPENCV", (300, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Image", img)

cv2.waitKey(0)

import cv2
import numpy as np

# tuto pour isoler une carte et lui rendre sa perspective je doit juste verifier la ligne 9 pts1 et donner les bonne coordonées de la carte a isolé
# finalement j'ai bien isolé la carte
img = cv2.imread("images/7.png")
# imgResize = cv2.resize(img, (600, 400))
print(img.shape)
width, height = 200, 300
#les coordonnées je les ai pris a l'oeil nu sur paint 
pts1 = np.float32([[100, 4], [197, 10], [83, 150], [185, 158]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image traitement chelou", imgOutput)
# cv2.imshow("Image", imgResize)
cv2.waitKey(0)


import cv2
import numpy as np

img = cv2.imread("PerlaDian.jpg")
alto, largo, canales = img.shape

respaldo = np.zeros((alto, largo, 3), dtype=np.uint8)

for l in range(100,350):
    for a in range(175,470):
        respaldo[a, l] = img[a, l]
        img[a, l] = img[a, (l+580)]

for l in range(680,930):
    for a in range(175,470):
        img[a, l] = respaldo[a, (l-580)]

# cv2.imshow("Imagen en negro",respaldo)
cv2.imshow("Imagen Original",img)

cv2.waitKey()
cv2.destroyAllWindows()
import cv2

img = cv2.imread()

contornosUno = []
contornosDos = []

cv2.matchShapes(contornosUno, contornosDos, 1, 0, 0)

cv2.imshow()

cv2.waitKey()
cv2.destroyAllWindows()
import cv2

# LEER LA IMAGEN Y REDIMENSIONARLA
img = cv2.imread("poker.jpg")
alto, largo, canales = img.shape
img = cv2.resize(img, ( int(  (largo/3)  ), int(  (alto/3)  ) ))

# CREAR COPIA
copia = img

# ESCALA DE GRISES
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# APLICAR DESENFOQUE --> IDENTIFICAR MÁS FÁCILMENTE LOS BORDES
img = cv2.GaussianBlur(img, (5,5), 0)

# DETECTAR ESOS BORDES CON CANNY
img = cv2.Canny(img, 50, 180)

# CONTORNOS
contornos, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontrar los contornos
copia = cv2.drawContours(copia, contornos, -1, (232, 127, 64), 2) # Dibujar los contornos
print(f"\nFIGURAS EN TOTAL: {len(contornos)}")

# ENCONTRAR LOS CENTROS
n = 0
print("AREAS:")
for i in contornos:
    momento = cv2.moments(i)
    ejeX = int(momento['m10'] / momento['m00'])
    ejeY = int(momento['m01'] / momento['m00'])

    cv2.circle(copia, (ejeX, ejeY), 3, (255, 255, 255), -1) # Dibujar el circulo
    cv2.putText(copia, f"{n}", (ejeX+5, ejeY+10), 2, 0.5, (255,255,255), 1) # Enumerar la figura en turno
    print(f"{n}. {cv2.contourArea(i)}") # Imprimir el área de la figura en turno
    n += 1

# MOSTRAR LA IMAGEN
cv2.imshow("Imagen",copia)

cv2.waitKey()
cv2.destroyAllWindows()

# Castellanos Moreno José Ángel  01-ISOF #:21050066
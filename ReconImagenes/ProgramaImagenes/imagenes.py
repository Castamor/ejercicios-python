# Castellanos Moreno José Ángel  01-ISOF #:21050066

import cv2
import os
import numpy as np
from tkinter import filedialog

def pedirImagen():
    direccion = filedialog.askopenfilename(filetypes=(  ("Todas las imagenes", ("*.jpg", "*.jpeg", "*.png")), ("Todos los archivos", "*.*")  ))
    
    #Verificar si se eligió un archivo
    if direccion:
        # Guardar la direccion
        dirImg = open("direccionImg.txt", "w")
        dirImg.write(str(direccion))
        dirImg.close()

        return direccion
    else:
        print("\n<< No se ha seleccionado ningún archivo >>\n")

def nombreImagen(arc):
    nombreArchivo = arc.split("/")
    name = nombreArchivo[-1]
    return name

def ventanaAjustable(imagen):
    cv2.namedWindow("ventana AUTOSIZE", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("ventana AUTOSIZE", imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()

def ventanaNormal(imagen):
    cv2.namedWindow("ventana ORIGINAL", cv2.WINDOW_NORMAL)
    cv2.imshow("ventana ORIGINAL", imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()

def ventanaMaximizada(imagen):
    cv2.namedWindow("ventana FULLSCREEN", cv2.WND_PROP_FULLSCREEN) 
    cv2.setWindowProperty("ventana FULLSCREEN", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("ventana FULLSCREEN", imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()



# Todo este if sirve para recordar la imagen anterior para no tener que volver a seleccionar la imagen, si es que hubo una imagen antes
if os.path.exists("direccionImg.txt"):
    arc = open("direccionImg.txt", "r")
    archivo= arc.read()
    arc.close()

    print(f"\n\tSe cargó la imagen '{nombreImagen(archivo)}'\n".upper())
else:
    print("\n\tSelecciona una imagen para trabajar en ella\n")
    archivo = pedirImagen()
    print(f"\n\tSe cargó la imagen '{nombreImagen(archivo)}'\n".upper())



while True:
    opc = int(input("Selecciona una opción del menú:\n[1] Seleccionar otra imagen\n[2] Tres tamaños de imagen\n[3] Imagen en R, G, B\n[4] Transladar imagen\n[5] Crear marco\n[6] Borrar centro y esquinas\n[7] Salir\n>>> "))

    if opc == 1:
        archivo = pedirImagen()
        print(f"\n\tSe cargó la imagen '{nombreImagen(archivo)}'\n".upper())
        nombreImagen(archivo)

    img=cv2.imread(nombreImagen(archivo))

    if opc == 2:
        print("\tMostrando ventanas...\n")
        ventanaAjustable(img)
        ventanaNormal(img)
        ventanaMaximizada(img)

    if opc == 3:
        print("\n\tImagen en R, G, B...\n")
        
        # COLOR ROJO
        img = cv2.imread(nombreImagen(archivo))
        img = cv2.resize(img,(400,400))
        b, g ,r = cv2.split(img)
        img[:,:,0] = 0
        img[:,:,1] = 0
        cv2.imshow("ImagenROJO",img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imwrite("ImagenROJO.jpg",img)

        # COLOR VERDE
        imgG = cv2.imread(nombreImagen(archivo))
        imgG = cv2.resize(imgG,(400,400))
        b, g ,r = cv2.split(imgG)
        imgG[:,:,2] = 0
        imgG[:,:,0] = 0
        cv2.imshow("ImagenVERDE",imgG)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imwrite("ImagenVERDE.jpg",imgG)

        # COLOR AZUL
        imgB = cv2.imread(nombreImagen(archivo))
        imgB = cv2.resize(imgB,(400,400))
        b, g ,r = cv2.split(imgB)
        imgB[:,:,2] = 0
        imgB[:,:,1] = 0
        cv2.imshow("ImagenAZUL",imgB)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imwrite("ImagenAZUL.jpg",imgB)

    if opc == 4:
        print("\n\tTransladar Imagen...\n")
        imagen = cv2.imread(nombreImagen(archivo))
        imagenDos = cv2.resize(imagen,(400,400))
        alto, largo, canales = imagenDos.shape

        tx=25
        ty=35

        mT = np.float32([[1,0,tx],[0,1,ty]])
                        
        imgT = cv2.warpAffine(imagenDos, mT, (largo, alto))
        cv2.imshow("T", imgT)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imwrite("ImagenTrasladada.jpg",imgT)

    if opc == 5:
        print("\n\tCrear marco...\n")
        img=cv2.imread(nombreImagen(archivo))
        alto, largo, canales = img.shape

        for l in range(largo):
            for a in range(alto):
                if l==0 or l==largo-1:
                    img[l,a]=[0,0,255]
                if a==0 or a==alto-1:
                    img[l,a]=[0,0,255]
        
        cv2.imshow("ImagenConMarco",img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imwrite("ImagenConMarco.jpg",img)

    if opc == 6:
        print("\n\tBorrar centro y esquinas...\n")   
        img=cv2.imread(nombreImagen(archivo))
        alto, largo, canales = img.shape

        #Bordes
        for x in range(largo):
            for y in range(alto):
                if x==0 and y==0:
                    img[x,y]=[0,0,255]
                    img[x+1,y]=[0,0,255]
                    img[x,y+1]=[0,0,255]
                    img[x+1,y+1]=[0,0,255]
                
                if x==largo-1 and y==alto-1:
                    img[x,y]=[0,0,255]
                    img[x-1,y]=[0,0,255]
                    img[x,y-1]=[0,0,255]
                    img[x-1,y-1]=[0,0,255]
                    
                if x==0 and y==alto-1:
                    img[x,y]=[0,0,255]
                    img[x+1,y]=[0,0,255]
                    img[x,y-1]=[0,0,255]
                    img[x+1,y-1]=[0,0,255]
                    
                if x==largo-1 and y==0:
                    img[x,y]=[0,0,255]   
                    img[x-1,y]=[0,0,255] 
                    img[x,y+1]=[0,0,255] 
                    img[x-1,y+1]=[0,0,255] 
                
                # Centro
                if x in range (int(largo/2)-20,int(largo/2)+20):
                    if y in range (int(alto/2)-20,int(alto/2)+20):
                        img[x,y]=[0,0,255] 
            
        cv2.imshow("Centro y bordes",img)
        cv2.imwrite("Centro y bordes.jpg",img) 
        cv2.waitKey()
        cv2.destroyAllWindows()


    if opc == 7:
        print("\n\tSaliste del programa...\n")
        break

# https://recursospython.com/guias-y-manuales/examinar-archivo-o-carpeta-en-tk-tkinter/
# https://www.youtube.com/watch?v=wjFLve0wZ7E&list=WL&index=2
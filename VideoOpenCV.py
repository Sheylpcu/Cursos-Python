import cv2 as cv
import numpy as np
import glob

def CrearVideo(ruta):
    img_array = []
    for filename in glob.glob(ruta): #recorre todos los archivos .png de la carpeta
        img = cv.imread(filename) #lee la imagen
        height, width, layers = img.shape #obtiene el tamaño de la imagen (ancho, alto y numero de colores)
        size = (width,height) #alamacenamos en una variable el tamaño del video
        img_array.append(img) #mete la imagen en la lista de imagenes
    
    #crea el video 
    #fourcc = especificas el formato 
    #15 = numero de imagenes por segundo (frames)
    out = cv.VideoWriter('project.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size) 
    
    #
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


CrearVideo('./dicom_salida/*.png')
import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import blackman

#height, width, and color
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)


#img = cv.imread('./body0001.png')
#cv.imshow('Body001', img)

#1- Pintar la imagen de un color
#blank[:]= 0,255,0
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

#2- Crear un rectangulo
#origen, tamaño, color, bordes
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=-1)

#cv.imshow('Rectangulo', blank )

#3- Circulo
#-1 relleno
#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
#cv.imshow('Circle', blank)

#4- Lineas
#cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,0), thickness=3)
#cv.line(blank, (100,150), (300,400), (255,255,255), thickness=3)
#cv.imshow('Line', blank)

#5- Text
#3.0 = tamaño del texto
cv.putText(blank, 'Hello', (0,255), cv.FONT_HERSHEY_TRIPLEX, 3.0, (0,255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)

import cv2 as cv
import numpy as np


img = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#imagen en negro del mismo tamaño que la imagen original
blank = np.zeros(resized.shape[:2], dtype='uint8')
#cv.imshow('Blank image', blank )

#Mascara circulo
#centro (del centro te puedes mover), radio, color, thikness
circle = cv.circle(blank, (resized.shape[1]//2 + 70, resized.shape[0]//2), 100, 255, -1)
#cv.imshow('mask', mask)

#Mascara rectangulo
#centro (del centro te puedes mover), end point, color, thikness
#mask = cv.rectangle(blank, (resized.shape[1]//2, resized.shape[0]//2),(resized.shape[1]//2 + 100 , resized.shape[0]//2 +100), 100, 255, -1)
#cv.imshow('mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('ee', weird_shape)

masked = cv.bitwise_and(resized, resized, mask=weird_shape)
cv.imshow('Masked image', masked)








cv.waitKey(0)
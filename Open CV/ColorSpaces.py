import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./perro.jpg')
cv.imshow('Dog', img)

#con grafico
#plt.imshow(img)
#plt.show()

#BGR to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#BGR to HSV
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('Gray', hsv)

#BGR to Lab   
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

#BGR to RGB
#rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

#hsv to BGR
#hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow('hsv_bgr', hsv_bgr)

#lab to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr', lab_bgr)


cv.waitKey(0)
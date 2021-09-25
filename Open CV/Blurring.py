import cv2 as cv
import numpy as np

img = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Averagin
#size
average = cv.blur(resized, (3,3))
cv.imshow('Average blur', average)

#Gaussian BLur
#sigmaX = 0
gauss = cv.GaussianBlur(resized, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median blur
median = cv.medianBlur(resized, 3)
cv.imshow('Median Blur', median)

#Bilateral blur
bilater = cv.bilateralFilter(resized, 10, 15, 15)
cv.imshow('Bilateral blur', bilater)



cv.waitKey(0)
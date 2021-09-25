import cv2 as cv
import numpy as np

original = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
img = cv.resize(original, (500,500), interpolation=cv.INTER_CUBIC)
#v.imshow('Resized', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combines_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('combination', combines_sobel)


canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)
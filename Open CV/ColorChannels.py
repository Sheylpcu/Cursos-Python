import cv2 as cv
import numpy as np

img = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#imagen en  blanco de dos canales
#basically consists of the height and with, not necessarily number of color
blank = np.zeros(resized.shape[:2], dtype='uint8')

b,g,r = cv.split(resized)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)





cv.waitKey(0)
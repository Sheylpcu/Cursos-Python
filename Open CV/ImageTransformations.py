import cv2 as cv
import numpy as np

img = cv.imread('./perro.jpg')
cv.imshow('Dog', img)

#translation
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x left
# -y up
# x right
# y down

#img, x, y
translated = translate(img, -100, 100)
#cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is  None:
        rotPoint=(width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
#cv.imshow('Rotates', rotated)

rotated_rotated= rotate(rotated, -45)
#cv.imshow('Rotated rotated', rotated_rotated)

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#Flip
#0 boca abajo y de un lado
#1 espejo mas menos por decirlo asi
#-1 boca abajo y de un lado
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)


#Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
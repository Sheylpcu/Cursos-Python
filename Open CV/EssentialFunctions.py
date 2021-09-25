import cv2 as cv

img = cv.imread('./perro.jpg')
#cv.imshow('Body0001', img)


#1-convertir en escala de grises
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#2- Blur
#Quitar ruido en la imagen
#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#3- Edge cascade
canny = cv.Canny(img, 125, 175)
#canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#4- Dilating
dilated= cv.dilate(canny, (7,7), iterations=5)
cv.imshow('Dilated', dilated)



#5- Eroding
eroded = cv.erode(dilated,(3,3), iterations=3)
cv.imshow('Erore', eroded)

#5- Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#6- Cropping
crope = img[50:200, 200:400]
cv.imshow('Cropped', crope)

cv.waitKey(0)
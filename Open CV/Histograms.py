import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#convertir a escala de grises
#gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blank = np.zeros(resized.shape[:2], dtype='uint8')
circle = cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(resized, resized, mask=circle)
#cv.imshow('Mask', mask)


#GraySclae histogram
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
#plt.figure()
#plt.title('Grayscale histogram')
#plt.xlabel('bins') #intervalos e intensidad de los pixeles [256]
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.show()


#Colour histograma
plt.figure()
plt.title('histogram')
plt.xlabel('bins')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([resized], [i], None, [256], [0,256] )
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)
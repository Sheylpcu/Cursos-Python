import cv2 as cv

original = cv.imread('./foto.jpg')
#cv.imshow('foto', img)

# resizing
img = cv.resize(original, (500,500), interpolation=cv.INTER_CUBIC)
#v.imshow('Resized', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholder', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholder inverse', thresh_inv)

#adaptative thresholding
adaptative_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptative thres', adaptative_thresh)



cv.waitKey(0)
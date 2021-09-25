import cv2 as cv
import numpy as np


#off 0, on 1

#imagen en negro
blank = np.zeros((400,400), dtype='uint8')

#starting points, across, color, fill the image 
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

#cv.imshow('Rectangle', rectangle)
#cv.imshow('Circle', circle)

#bitwise AND = intersecting regions
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bit_and)

#bitwise OR = non intersecting and intersecting regions
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bit_or)

#bitwise XOR = non intersection regions
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bit_xor)

#bitwise NOT = invert the color 
bit_not = cv.bitwise_not(circle)
cv.imshow('NOT', bit_not)




cv.waitKey(0)
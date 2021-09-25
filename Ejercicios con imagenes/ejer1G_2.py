import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Leer la imagen
image1 = cv2.imread('body0001.png')

def mask(image1,color):
	# Aplicar threshold a la imagen
	img = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
	ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

	image2 = np.zeros(shape=(512,512,3), dtype=np.uint8)

	for x in range(image2.shape[0]):
		for y in range(image2.shape[1]):
			for rgb in range(image2.shape[2]):
				image2[x, y, rgb] = 300#thresh1[x,y]-color[rgb]
	

	# newImage = thresh1.copy()
	# imgColor = Image.new('RGB', (212, 212), color = (255,0,0))

	# combine foreground+background
	#final = cv2.bitwise_and(image2,mask)
 

	# Visualización
	cv2.imshow('Binary Threshold', thresh1)
	cv2.imshow('final', image2)

	#esto es así
	cv2.waitKey(0)
	cv2.destroyAllWindows()


mask(image1, color=(3,194,255))
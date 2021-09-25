import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Leer la imagen
image1 = cv2.imread('x.png')

def mask(image1,color):
    # Aplicar threshold a la imagen
    img = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    #Mascara de color 
    mask = np.zeros(shape=(512,512,3), dtype=np.uint8)
    mask[:,:] = color

    #Se aplica el valor a la imagen en los 3 colores
    image2 = np.zeros(shape=(512,512,3), dtype=np.uint8)
    image2[:,:,0] = thresh1
    image2[:,:,1] = thresh1
    image2[:,:,2] = thresh1

    # newImage = thresh1.copy()
    # imgColor = Image.new('RGB', (212, 212), color = (255,0,0))

    # combine foreground+background
    final = cv2.bitwise_and(image2,mask)
 

    # Visualización
    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Mascara', mask)
    cv2.imshow('final', final)

    #esto es así
    cv2.waitKey(0)
    cv2.destroyAllWindows()


mask(image1, color=(3,194,255))

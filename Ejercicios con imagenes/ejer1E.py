from PIL import Image
import pydicom as dicom
import matplotlib.pyplot as plt
import numpy as np


def histograma(nombre_del_archivo):
    ds= dicom.dcmread(nombre_del_archivo)
    #pixelarray= ds.pixel_array
    
#Convertir los valores hounsfield en escala de grises y contarlos
    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)
    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)
    max= image_2d_scaled.max() #coger el valor mas alto de todos los pixeles
    datos= [0 for _ in range(max+1)]
    # recorre todos los pixeles de todas las filas
    for i,fila in enumerate(image_2d_scaled):
        for j,pixel in enumerate(fila):
            datos[pixel]+=1
            #print(pixel)
    
    plt.figure(1)
    x=range(len(datos))
   # plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title('Histograma')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    
    plt.savefig("histograma.png", bbox_inches='tight')
    #print(datos)

histograma('./body0001.dcm')

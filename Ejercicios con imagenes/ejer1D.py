import os
from sys import path
import pydicom as dicom
import matplotlib.pyplot as plt
import numpy as np



path="C:\\Users\\Prácticas\\Desktop\\Ejercicios\\dicom"
def planes_3(path):
    CT_images= os.listdir(path)

    slices=[dicom.read_file(path+'/'+s, force=True) for s in CT_images]

    slices= sorted(slices,key=lambda x:x.ImagePositionPatient[2])

    pixel_spacing=slices[0].PixelSpacing
    slice_thickness=slices[0].SliceThickness

    axial_aspect_ratio= pixel_spacing[1]/pixel_spacing[0]
    sagital_aspect_ratio=pixel_spacing[1]/slice_thickness
    coronal_aspect_ratio=slice_thickness/pixel_spacing[0]

    print(pixel_spacing) 
    print(slice_thickness) #grosor de las capas
    print(axial_aspect_ratio) #aspect_ratio : relacion entre ancho y alto
    print(sagital_aspect_ratio)
    print(coronal_aspect_ratio)

    image_shape=list(slices[0].pixel_array.shape) #anchoXalto de las imagenes
    image_shape.append(len(slices)) #añadir a esa lista el número de capas
    volume3d=np.zeros(image_shape)

    for i,s in enumerate(slices):
        array2d=s.pixel_array
        volume3d[:,:,i]=array2d 

    print(array2d.shape)
    print(volume3d.shape)

    axial=plt.subplot(2,2,1)
    plt.title("Axial")
    #de un volumen en 3d se pasa a una matriz 2d de donde se obtiene la capa intermedia
    """plt.imshow(slices[100].pixel_array, cmap=plt.cm.bone)"""
    plt.imshow(volume3d[:,:,image_shape[2]//2], cmap=plt.cm.bone)
    axial.set_aspect(axial_aspect_ratio)

    sagital=plt.subplot(2,2,2)
    plt.title("Sagital")
    plt.imshow(volume3d[:,image_shape[1]//2,:], cmap=plt.cm.bone)
    sagital.set_aspect(sagital_aspect_ratio)

    coronal=plt.subplot(2,2,3)
    plt.title("Coronal")
    plt.imshow(volume3d[image_shape[0]//2,:,:].T, cmap=plt.cm.bone)
    coronal.set_aspect(coronal_aspect_ratio)

    plt.subplots_adjust(wspace=0.8, hspace=1)
    plt.show()

planes_3(path)
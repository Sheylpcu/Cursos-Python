import numpy as np
import png 
import os, pydicom

source_folder = r'./dicom/'
output_folder = r'./dicom_salida/'


def dicom2png(source_folder, output_folder):
    list_of_files = os.listdir(source_folder)
    for file in list_of_files:
        try:
            ds = pydicom.dcmread(os.path.join(source_folder,file)) #al nombre de la carpeta le une el nombre de archivo
            shape = ds.pixel_array.shape #devulve[alto, ancho]

            # Convert to float to avoid overflow or underflow losses.
            image_2d = ds.pixel_array.astype(float)

            # Rescaling grey scale between 0-255
            image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

            # Convert to uint
            image_2d_scaled = np.uint8(image_2d_scaled)

            # Write the PNG file
            file= file.split(".dcm")[0] #quitar el texto que no se quiere
            with open(os.path.join(output_folder,file) +'.png' , 'wb') as png_file: #wb :w de escritura y b de que es archibo binario
                w = png.Writer(shape[1], shape[0], greyscale=True) #ancho y alto
                w.write(png_file, image_2d_scaled)
               
        except:
            print('Could not convert: ', file)


dicom2png(source_folder, output_folder)
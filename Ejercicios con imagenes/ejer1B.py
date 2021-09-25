import pydicom as dicom
import matplotlib.pylab as plt
import json

image_path = './body0001.dcm'
output_name = "fichero"

def write_dicom_json(image_path, output_name):
    ds=dicom.dcmread(image_path)
     
    diccionario = {'Columns': ds.Columns, 'Rows': ds.Rows }

    with open(output_name+'.json', 'w') as json_file:
     json.dump(diccionario, json_file) #Escribir lo que hay en diccionario en el fichero



write_dicom_json(image_path, output_name)

   

import pydicom as dicom
import matplotlib.pylab as plt

image = './body0001.dcm'

def open_dicom_file(image_path):
    ds = dicom.dcmread(image_path)
    plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
    plt.show()


open_dicom_file(image)



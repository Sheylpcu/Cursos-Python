import cv2 as cv

#Imagenes
#img = cv.imread("./body0001.png")
#cv.imshow('Body0001', img)

#Videos
#0 = camara conectada
video =  cv.VideoCapture("./project.avi")
while True:
    isTrue, frame = video.read()
    cv.imshow('Video', frame)

    #velocidad de reproduccion & que se cierre la ventana de visualización cuando pulses una letra
    if cv.waitKey(100) & 0xFF==ord('x'):
        break

video.release()
cv.destroyAllWindows()




#cv.waitKey(0)
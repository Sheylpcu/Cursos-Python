import cv2 as cv

#Imagen,video and live video
img =cv.imread('./body0001.png')
cv.imshow('Body0001', img)

def rescaleFrame(frame, scale=0.75):
    #ancho y alto
    width = int(frame.shape[1] * scale)
    height =int( frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)



def changeRes(width, height):
    #Live video
    video.set(3, width)
    video.set(4,height)



#########################################
 #Video

video =  cv.VideoCapture("./project.avi")
while True:
    isTrue, frame = video.read()
    
    #PAra reescalar
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    #velocidad de reproduccion & que se cierre la ventana de visualización cuando pulses una letra
    if cv.waitKey(100) & 0xFF==ord('x'):
        break

video.release()
cv.destroyAllWindows()
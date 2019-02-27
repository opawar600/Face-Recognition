
import numpy as np

import cv2


detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)


while(True):

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 10)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),2)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
    
cam.release()

cv2.destroyAllWindows()
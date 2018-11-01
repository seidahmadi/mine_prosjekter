''' proggramet skal opne kameraport og prove og skanne
alle pikseler og gjennskjenne bilder'''

import cv2
import numpy as np

objekt_csc = cv2.CascadeClassifier('sukkerbit00.xml')
cam = cv2.VideoCapture(0) #apner kameraet

while(True):
    tf , img = cam.read() # mens det er true setter img = kameraingangen

    #importerer bildet til gray for det er enklere a forholdet seg til
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    objekter = objekt_csc.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in objekter:
        cv2.rectangle(img, (x,y),(x+w, y+h),(255,255,255),3)
    cv2.imshow('img',img)

    key= cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()

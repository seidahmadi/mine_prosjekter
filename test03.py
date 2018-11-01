''' proggramet skal opne kameraport og prove og skanne
alle pikseler og gjennskjenne bilder'''

import cv2
import numpy as np

#objekt_csc = cv2.CascadeClassifier('myhaar.xml')
objekt_csc = cv2.CascadeClassifier('regulator01.xml')
cam = cv2.VideoCapture(0) #apner kameraet

while(True):
    tf , kamera = cam.read() # mens det er true setter img = kameraingangen
    #importerer bildet til gray for det er enklere a forholdet seg til
    gray = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)

    objekter = objekt_csc.detectMultiScale(gray,1.1,4)

   # cv2.HaarDetectObjects(kamera, 'myhaar.xml', 'pos', scale_factor=1.1, min_neighbors=3, flags=0, min_size=(0, 0))
    for (x,y,w,h) in objekter:
        cv2.rectangle(kamera, (x,y),(x+w, y+h),(255,255,255),3)
#        cv2.HaarDetectObjects('a1,jpg', 'myhaar.xml', 'pos', scale_factor=1.1, min_neighbors=3, flags=0,min_size=(0, 0))
    cv2.imshow('kamera',kamera)

    key= cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()


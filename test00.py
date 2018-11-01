 # programmet skal lese in bildet og se etter pa kamera ingangen og prove a gjenskjenne bildet '''
# klarte ikke

import urllib  # siden vi bruker python 2.7 request fungerer ikke sa erstatet og brukes slik urllib.urlopen(url)
import cv2
import numpy as np
import os






img = cv2.imread("regulator_sukkerbit.jpg") # leser bildet
regulator_csc =  cv2.CascadeClassifier('regulator_sukkerbit_reguleringshjul.xml') # leser haarcascade filen

#importerer bildet til gray for det er enklere a forholdet seg til
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = regulator_csc.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,255,255),3)

cv2.imshow('img',img)
cv2.waitKey(0)








'''
cam = cv2.VideoCapture(0)  # her kan vi apne kamera
#face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # den opner har kaskaden vi har lagdt

while (True):
    tf, img = cam.read()

    b1 = cv2.imread('a1.jpg') # her er de fire bilder vi skal sammenligne med videoen
    b2 = cv2.imread('a30.bmp')
    b3 = cv2.imread('a32.bmp')
    b4 = cv2.imread('a27.bmp')
    objekt_csc = cv2.CascadeClassifier('myhaar.xml') # den opner haar_kaskaden vi har lagdt



    gray_1 = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY) #konverterer bildet til gray for at det skal vaere enklere a forholde seg til
    #gray2 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    #gray3 = cv2.cvtColor(b3, cv2.COLOR_BGR2GRAY)
    #gray4 = cv2.cvtColor(b4, cv2.COLOR_BGR2GRAY)

    #ansikt = face_csc.detect.MultiScale(gray_1,1.1,4)
    objekt = objekt_csc.detect.MultiScale(gray_1,1.1,4)
    #objekt2 = objekt_CSC.detect.MultiScale(gray2,1.1,4)
    #objekt3 = objekt_CSC.detect.MultiScale(gray3,1.1,4)
    #objekt4 = objekt_CSC.detect.MultiScale(gray4,1.1,4)


    for (x,y,w,h) in objekt:
        cv2.rectangle(b1, (x,y),(x+w, y+h),(255,255,255),3)

    cv2.imshow('b1',b1)

    key= cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.waitKey(0)



'''

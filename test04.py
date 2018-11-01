''' proggramet skal opne kameraport og prove og skanne
alle pikseler og gjennskjenne bilder'''

import cv2
import numpy as np

regulator_csc = cv2.CascadeClassifier('regulator01.xml') # tenkte a lage en kaskade for hver av objektene mine
sukkerbit_csc = cv2.CascadeClassifier('regulator_sukkerbit002.xml')
#obj3_csc = cv2.CascadeClassifier('myhaar.xml')

cam = cv2.VideoCapture(0) #apner kameraet

while(True):
    ret , img = cam.read() # mens det er true setter img = kameraingangen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #importerer bildet til gray for det er enklere a forholdet seg til
    regulator = regulator_csc.detectMultiScale(gray, 1.1, 4)
    sukkerbit = sukkerbit_csc.detectMultiScale(gray, 1.1, 3)
    #obj3 = obj3_csc.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in regulator:
        cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),3) #lager rektangle rundt obj1 med blue farget
        #for at rektalngel skal ikke vaere uten for objektet angir jeg plasseringen
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    for (x1, y1, w1, h1) in sukkerbit:
        cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 3)  # lager rektangle rundt obj1 med blue farget
        # for at rektalngel skal ikke vaere uten for objektet angir jeg plasseringen
        roi_gray1 = gray[y1:y1 + h1, x1:x1 + w1]
        roi_color2 = img[y1:y1 + h1, x1:x1 + w1]


    cv2.imshow('img',img)

    key= cv2.waitKey(30) & 0xff
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()

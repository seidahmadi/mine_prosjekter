''' programmet skal detektere sukerbiten  pa et bildet
for a gjore dette ma jeg bruke bibliotek fila myhaar.xml som jeg har laget
'''

import cv2
import numpy as np


img = cv2.imread("regulator_sukkerbit0.jpg") # leser bildet
sukerbit_csc =  cv2.CascadeClassifier('sukkerbit00.xml') # leser haarcascade filen

#importerer bildet til gray for det er enklere a forholdet seg til
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = sukerbit_csc.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,255,255),3)

cv2.imshow('img',img)
cv2.waitKey(0)



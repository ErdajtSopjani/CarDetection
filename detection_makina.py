import numpy as np
import cv2

kerret_detection = cv2.CascadeClassifier("module_per_makina.xml")

video = cv2.VideoCapture("kerret.mp4")

while video.isOpened():
    ret, img = video.read()
    e_hint = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kerret = kerret_detection.detectMultiScale(e_hint, 1.3, 2)

    for (x,y,w,h) in kerret:
        cv2.rectangle(img,(x, y), (x+w+5, y+h+5), (0,0,255),3) 
        
    cv2.imshow("Detector per Makina", img)   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
video.release()
cv2.destroyAllWindows()
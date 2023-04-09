import numpy as np
import cv2



print("\n\nHello and welcome to Car Detection, Made by Erdajt Sopjani.\nThis program can detect cars anywhere now with te latest update it can even use your own camera.\nIt can help and solve a lot of everyday problems.\nTest it out from our generated video or detect cars from your device camera.\n")

mode = input("\n\nPress 1 to see a prototype with our generated video.\nPress 2 to test out the program from your own camera.\n\n")

if mode == "1":
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

if mode == "2":

    #XML (ALGORITHMA)
    kerretxml = cv2.CascadeClassifier("module_per_makina.xml")


    #DETEKTIMI 
    def detect(frame):
        kerri = kerretxml.detectMultiScale(frame, 1.15, 4)

        for (x, y, w, h) in kerri:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
            cv2.putText(frame, "Detected Car!", (x+w, y+h), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness = 1)

        return frame

    #KAMERA DHE DISPLAY
    def kamera():
        video_kamera = cv2.VideoCapture(0)

        while video_kamera.isOpened():
            ret, frame = video_kamera.read()
            butoni = cv2.waitKey(1)

            if ret :
                makina_xy = detect(frame)
                cv2.imshow("Car Detection by Erdajt Sopjani", makina_xy)

            else :
                break

            if butoni == ord('q'):
                break

        video_kamera.release()
        cv2.destroyAllWindows()

    kamera()

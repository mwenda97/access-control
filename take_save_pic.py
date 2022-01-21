import cv2
import numpy as np
import imutils
import time

face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

def take_photo(name):  # code takes photos and stroes them to input folder//only takes a photo when a face is detected
    print("INFO::Starting Video stream")
    #name = input('enter your name')
    cap = cv2.VideoCapture(0)
    photos = 0
    while photos < 1:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('captured_photo/' + str(name) + '.jpg', frame)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.32, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]
            cv2.imshow('min frame', roi_color)
            photos = photos + 1
            #time.sleep(1)
            if photos == 1:
                print('INFO:: Done taking photos')

        cv2.imshow('main frame', frame)
        key = cv2.waitKey() & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

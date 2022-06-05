import cv2
import time

from cv2 import threshold
# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')


threshold = 0
    

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    faces = [f for f in faces if f[2]*f[3] > 500] # prevent smaller objects:

    if faces == []:
        threshold += 1
    else:
        threshold = 0

    if threshold >= 10 :
        print("DISTRACTED ! ! ! \n")
        print('\a')

    for (x, y, w, h) in faces:
         if (w*h > 100000):
             cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    time.sleep(0.5)

cap.release()
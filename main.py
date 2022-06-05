import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    faces = [f for f in faces if f[2]*f[3] > 100000] # prevent smaller objects:
    if faces == []:
        print("distracted!!! \a")
    # for (x, y, w, h) in faces:
    #     if (w*h > 100000) 
    #         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    time.sleep(0.1)

    # cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
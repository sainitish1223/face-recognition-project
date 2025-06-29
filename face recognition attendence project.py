import cv2
import numpy as np
import os
import pandas as pd
import sqlite3
from datetime import datetime

# Initialize the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to mark attendance
def mark_attendance(name):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Attendance
                      (Name TEXT, Date TEXT, Time TEXT)''')
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    cursor.execute("INSERT INTO Attendance (Name, Date, Time) VALUES (?, ?, ?)", (name, date, time))
    conn.commit()
    conn.close()

# Load images and create encodings
path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    img = cv2.imread(f'{path}/{cl}')
    images.append(img)
    classNames.append(os.path.splitext(cl)[0])

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Recognize the face (for simplicity, we assume the first face detected is the student)
        name = classNames[0]  # Replace with actual recognition logic
        mark_attendance(name)

    cv2.imshow('Face Recognition', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

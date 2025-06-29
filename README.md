# face-recognition-project
# Face-Recognition-Attendance-System
Face Recognition Attendance System
This project proposes an automated attendance system using real-time face recognition to streamline student attendance. The system implements face detection and recognition using OpenCV and Haar Cascade Classifier for high accuracy.

Requirements
OpenCV
NumPy
Pandas
SQLite
Run the Python file
Overview
Nowadays, computer vision has developed to a point where it can recognize and process images and videos for various applications such as face recognition, color detection, etc. This project leverages these advancements to automate the attendance marking process, eliminating the need for manual attendance taking.

Main Purpose
The main purpose of this application is to automate the attendance process using face recognition technology. This system captures the student’s face, recognizes it, and marks the attendance in a database, thus streamlining the attendance process and reducing manual effort.

How It Works
Face Detection: The system uses Haar Cascade Classifier to detect faces in real-time from the webcam feed.
Face Recognition: Recognized faces are matched against a pre-stored database of student images.
Attendance Marking: Once a face is recognized, the system marks the attendance in an SQLite database with the student’s name, date, and time.
Hardware Requirements
A webcam or a built-in camera for face recognition.
Procedure for Operating
Capture Images: Capture images of students and store them in the Images folder.
Run the Script: Execute the Python script to start the face recognition and attendance marking process.
Mark Attendance: The system will automatically detect and recognize faces, and mark the attendance in the database.

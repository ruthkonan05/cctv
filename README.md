# 🚀 Smart Detection System using Sensors
## 📌 Project Overview
The Smart Detection System using Sensors is a project designed to identify specific individuals by analyzing 
their movement patterns using an ultrasonic sensor (HC-SR04) and a Machine Learning model (LSTM).

This system is designed for use in an office to distinguish between the owner and visitors. It relies on a Raspberry 
Pi, which collects the data and sends it to an interactive dashboard for visualization.

## 🎯 Project Goals
✅ Design a sensor-based detection system
✅ Use artificial intelligence to identify individuals
✅ Store and analyze real-time data with MongoDB
✅ Provide a visual interface for tracking results

## 🛠️ Technologies Used
### Hardware: Raspberry Pi, HC-SR04 Sensor
### Development: Python (Flask, TensorFlow, NumPy)
### Database: MongoDB
### Machine Learning: LSTM (Long Short-Term Memory) Neural Networks
### Dashboard: Flask, HTML/CSS, JavaScript

## ⚙️ How It Works
### 1️⃣ Data Collection

An ultrasonic sensor (HC-SR04) detects movements in the room
The Raspberry Pi records the data and sends it to MongoDB
### 2️⃣ Smart Identification

An LSTM neural network model analyzes the movement data
It distinguishes the owner of the office from visitors
### 3️⃣ Data Visualization

Results are displayed on an interactive dashboard
The user can view presence and identification statistics
📊 Use Cases
🔹 Office or restricted space monitoring
🔹 Automatic identification of individuals based on their movements



# README - Advanced Person Detection System

## Project Overview

In the second semester, we improved our initial project by integrating a camera to enhance person detection. Additionally, we developed a mobile application using Flutter, which sent alerts upon detecting a person and displayed information about lab members. If an unknown person was detected, their information was also shown.

## Technologies & Components Used

Ultrasonic Sensor (HC-SR04): Continued use for movement detection.

Camera: Added for visual recognition of detected individuals.

OpenCV (Python Library): Used for face detection and recognition.

Raspberry Pi: Used for processing sensor and camera data.

MongoDB: Real-time database for storing detected individuals.

Flutter (Mobile App): Developed to send alerts and display information.

Notification System: Sends alerts when a person is detected.

Implementation Details

Person Detection:

The HC-SR04 sensor and camera work together to detect movement and capture images.

OpenCV processes the images to recognize known individuals.

### Real-Time Alert System:

If a person is detected, their data is stored in MongoDB.

The Flutter app receives a notification with the detected person's details.

If the person is unknown, their image is displayed in the app.

### Mobile Application:

Built with Flutter to allow real-time monitoring.

Displays lab members and unknown individuals.

Sends notifications when someone enters the monitored area.

Goals Achieved

Integrated camera-based detection using OpenCV.

Developed a mobile application for real-time alerts.

Implemented real-time notifications with person information.


How to Use

Connect the camera and HC-SR04 sensor to the Raspberry Pi.

Run the detection script to start person recognition.

Open the Flutter mobile app to receive notifications.

Train the face recognition model for improved accuracy.



Author

[Konan Ruth ]
🔹 Real-time visualization of entries and exits

## 🚀 Conclusion
The Smart Detection System using Sensors is an innovative solution combining IoT, artificial intelligence, and real-time data processing.
This project demonstrates how sensors and machine learning can be used to improve identification and management of secure spaces.

Laser-Tracking-and-Targeting-System

Overview

I developed this project to learn and explore computer vision, Arduino programming, servo motor control, and embedded systems.

The system uses a smartphone running the IP Webcam application as a wireless camera source. The live video stream is processed in Python using OpenCV to detect and track moving objects in real time.

Based on the detected object position, tracking coordinates are sent to an Arduino Uno through serial communication. The Arduino controls a pan-tilt mechanism that continuously aligns a laser pointer with the tracked object.

I also designed and built a simple launcher mechanism using wooden sticks, rubber bands, and a servo-based trigger. The trigger mechanism can be activated manually by clicking the mouse inside the tracking window.

All Python code was written by me using a standard keyboard in Visual Studio Code, and the Arduino program was developed and uploaded using Arduino IDE.

Features

- Real-time motion detection
- Object tracking and target locking
- Motion prediction
- Pan-Tilt servo control
- Laser tracking
- Smartphone IP Webcam integration
- Serial communication between Python and Arduino
- Mouse-click controlled trigger servo
- Rubber-band powered launcher mechanism
- Live OpenCV video display

Hardware Used

- Arduino Uno
- Smartphone with IP Webcam
- 2 × SG90 Servo Motors (Pan and Tilt)
- 1 × SG90 Servo Motor (Trigger)
- Laser Module
- Breadboard
- Jumper Wires
- USB Cable
- External 5V Power Supply
- Wooden sticks
- Rubber bands
- Cardboard base

Software Used

- Python 3.x
- OpenCV
- NumPy
- PySerial
- Visual Studio Code
- Arduino IDE
- IP Webcam

How It Works

1. Start IP Webcam on the smartphone.
2. Copy the video stream IP address.
3. Update the IP address in the Python code.
4. Run the Python program.
5. The system detects and tracks moving objects.
6. Tracking coordinates are sent to Arduino.
7. The pan and tilt servos move the laser toward the target.
8. The launcher trigger can be activated using a mouse click.

Repository Files

- Tracking.py
- Tracking.ino
- complete setup.jpg
- camera and tracking system.jpg
- launcher and camera.jpg
- servo connections.jpg
- Arduino UNO wiring.jpg
- tracking and shooting video.mp4

---

Author

Muhammad Faisal P

B.Tech Electronics and Communication Engineering

This project was designed, assembled, programmed, tested, and documented by me as a personal learning project in computer vision, Arduino, and embedded systems.

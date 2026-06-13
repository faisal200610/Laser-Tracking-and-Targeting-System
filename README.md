# Laser-Tracking-and-Targeting-System

Developed by: Muhammad Faisal P
Btech Government engineering college sreekrishnapuram 

Project Overview

I designed and developed a motion tracking turret system using Python, OpenCV, Arduino, and servo motors. The system detects moving objects through a live camera feed, automatically locks onto the target, predicts its movement, and continuously tracks it using pan-tilt servos.

A manual firing mechanism is also integrated. When the user clicks on the video screen, a trigger servo activates a rubber-band launcher mounted on the turret.

Technologies Used

- Python
- OpenCV
- NumPy
- Arduino
- Servo Motors
- Serial Communication
- IP Webcam

Working Principle

1. The camera continuously captures live video.
2. OpenCV detects moving objects using background subtraction.
3. Noise is removed using morphological filtering.
4. The largest moving object is selected as the target.
5. The system locks onto the target.
6. Motion prediction estimates the target's future position.
7. Pan and tilt servos automatically align the turret toward the target.
8. Clicking on the video screen activates the trigger servo.
9. The launcher fires a rubber band toward the tracked target.

Features

- Automatic target detection
- Real-time object tracking
- Motion prediction algorithm
- Pan-tilt servo control
- Manual firing mechanism
- Live video monitoring
- Arduino-Python communication
- Target lock system

Hardware Components

- Arduino Uno
- 2 × SG90 Servo Motors (Pan-Tilt)
- 1 × Trigger Servo
- IP Webcam Mobile Camera
- Rubber Band Launcher
- Power Supply
- Mounting Structure

Software Components

- Python
- OpenCV
- NumPy
- PySerial
- Arduino IDE

Applications

- Computer Vision Learning
- Robotics Projects
- Motion Tracking Systems
- AI Surveillance Demonstration
- Educational Automation Projects

Future Improvements

- Face Recognition
- Object Classification using AI
- BCI (Brain Computer Interface) Control
- Voice Command Integration
- Automatic Target Selection
- Wireless Control System

Project Outcome

The developed system successfully detects moving objects, locks onto them, predicts their movement, and controls servo motors in real time to keep the target centered in the camera view. The firing mechanism can be activated through a mouse click on the tracking interface.

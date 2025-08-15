### WELCOME TO MY BLURRED FACE PROJECT ###

This is a small project for a well bigger project that im working on.
What this project does is that it opens a webcam device and automatically blur a face.
This project uses OpenCV in conjunction of Google's MediaPipe to automatically blur a face with training

## REQUIREMENTS ##
- UNIX/Linux Based systems
- OpenCV
    https://opencv.org/
- MediaPipe
    https://ai.google.dev/edge/mediapipe/solutions/guide
- Recent version of Python
    - With this project im using 3.10.12
- Recent version of Numpy
    - With this project im using 1.26.4

## Installation ##
    1. After downloading this project, head to the directory in which you stored this project in
    2. Install both OpenCV and MediaPipe
        - source venv/bin/activate
        - pip install mediapipe
        - pip install opencv-python
    3. After dependancies are installed run:
        - python3 main.py

## WHAT HAPPENS ##
    - A pop up will display on your screen, saying `Blurred Face detected` in which your face will automatically blur
    

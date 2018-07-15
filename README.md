# raspberry_pi_face_detector
A small python-based OpenCV Haar Cascade frontal face detector for the Raspberry Pi 3 camera module

Purpose:  With only 2 libraries (cv2 and time) you can run this!  Very few scripts exist out there that are lean enough with few dependencies to do reasonable facial detection.  Most require you to install bulky libraries or are simply too CPU intensive for a Raspberry Pi.  After installing and trying lots of these scripts (with little or no success) I found two that when merged with some edits to get the job done.  Of course this is not an industrial quality face detector, it is for a "front-of-face" target only, but it's pretty slim, fast and able to be tweaked easily.  

# Code citations:  
- Picamera activation snippet from Adrian's Picamera + OpenCV + Python + Raspberry Pi 
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

- Face detection snippet from Shantu's 'webcam_face_detector'
https://github.com/shantnu/Webcam-Face-Detect


# Pre-requisites:  (what I used)
Raspberry Pi 3 B+   (but if your Pi can run CV2, you'll be fine)
Camera module V2 (this one:  https://www.raspberrypi.org/products/camera-module-v2/)  
OS is Rasbian Stretch, latest as of 2018
CV2 library installed
Monitor, mouse, keyboard

# Installing CV2
To install CV2 library on Rasbian Stretch, definitely check out Adrian's incredibly detailed install tutorial and buy his book:
https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/


# How to use this script on Rasbian Stretch
0)  You absolutely MUST have CV2 installed.  To check and see if it is there first enter your python shell:
```
python
```
then type the following commands:
```
import cv2
cv2.__version__
```
This will return the version you are using, the one I used was 3.3.0
CTRL-D to exit python.

# Now that the boring stuff is over...

1)  Open a terminal shell, be in your normal users's directory and type the following (edit if desired):
```
cd Downloads
git clone 
```
2)  Change directory into the new folder that was created

3)  Run the script by typing:
```
python rpi_face_detect.py
```

# What SHOULD happen:
Your camera light should turn on and a window will pop up displaying the video feed.  You need to have the FRONT of your face looking into the camera and it will draw a green bounding box around it.  The response time is pretty decent considering the simplicity of the entire system.  It isn't incredibly smooth but like I said, it gets the job done.

# How to quit
Simply press the 'q' key on the keyboard

# What's going on, how does this work?
The first thing you might have noticed if you looked at the files in this git is the xml file:  "haarcascade_frontalface_default.xml".  The name sort of says what it does, it contains almost a full megabyte of parameters regarding front-of-face analytics.  This is a pre-baked data file from OpenCV and is used to compare image data you feed it with the call to "faceCascade" in the python script.  There are other Haar Cascade files for different things located here:

https://github.com/opencv/opencv/tree/master/data/haarcascades

In order to understand what's going on with this style of face detection, I highly recommend you read about the OpenCV library and face detection using Haar Cascades:

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html



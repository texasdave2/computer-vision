# raspberry_pi_face_detector
A small python based OpenCV Haar Cascade face detector for the Raspberry Pi 3 camera module

Purpose:  With only 2 libraries (cv2 and time) you can run this!  Very few scripts exist out there that are lean enough with few dependencies to do reasonable facial detection.  Most require you to install bulky libraries or are simply too CPU intensive for a Raspberry Pi.  After installing and trying lots of these scripts (to little or no success) I found two that when merged with some edits work to get the job done.  Of course this is not an industrial quality face detector, but it's pretty slim, fast and able to be tweaked easily.  

# Code citations:  
- Picamera activation snippet from Adrian's Picamera + OpenCV + Python + Raspberry Pi 
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

- Face detection snippet from Shantu's 'webcam_face_detector'
https://github.com/shantnu/Webcam-Face-Detect


# Pre-requisites:  (what I used)
Raspberry Pi 3 B+   (but if your Pi can run CV2, you'll be fine)
OS is Rasbian Stretch, latest as of 2018
CV2 library installed

# Installing CV2
To install CV2 library on Rasbian Stretch, definitely check out Adrian's incredibly detailed install tutorial and buy his book:
https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/

# About face detection
In order to understand what's going on with this style of face detection, I highly recommend you read about the OpenCV library and face detection using Haar Cascades:

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html

# How to use this script on Rasbian Stretch
0)  You absolutely MUST have CV2 installed.  To check and see if it is there do this:
type:
python 
1)  Open a terminal.  In your shell, change directory to your downloads or some directory to bring these files into
2)  You'll be making a self-contained folder in that directory of these files with the next step
3)  Clone this git into that directory by typing:  

2)  Change directory into the directory that was created

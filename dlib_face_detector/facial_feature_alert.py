# USAGE
# python facial_landmarks.py

# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import time
from datetime import datetime

# sensehat imports
from sense_hat import SenseHat
import numpy as np
import ect
from random import randint
import sys

# initialize sensehat
sense = SenseHat()

w = [150, 150, 150]
b = [0, 0, 255]
e = [0, 0, 0]


# create empty screen
screen = np.array([
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
])



# pi camera imports
from picamera.array import PiRGBArray
from picamera import PiCamera


# code for raspberry pi camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow camera to warm up
time.sleep(0.1)



# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# grab the raw NumPy array representing the image, then initialize the timestamp
# and occupied/unoccupied text
  image = frame.array

# load the input image and convert it to grayscale
#image = cv2.imread("example.jpg")
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
  rects = detector(gray, 0)

# loop over the face detections
  for (i, rect) in enumerate(rects):
# determine the facial landmarks for the face region, then
# convert the facial landmark (x, y)-coordinates to a NumPy
# array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

# lets light up the sensehat during detection
# stack images ontop of each other

    for x in range(0, 2):
      r = randint(0,100)
      g = randint(0,100)
      b = randint(0,100)
      image1 = ect.circle(screen,(4,4), 3, [r, g, b], 0.1)
      image2 = ect.circle(image1,(4,4), 2, [r, g, b], 0.1)
      image3 = ect.circle(image2,(4,4), 1, [r, g, b], 0.1)

    image3 = ect.clear(image3)


# loop over the (x, y)-coordinates for the facial landmarks
# and draw them on the image
    for (x, y) in shape:
      cv2.circle(image, (x, y), 2, (0, 255, 0), -1)


# write some instruction text on the frame
  text = "press p to take a PHOTO, press q to QUIT"
  xcoord = 50
  ycoord = 25
  font = cv2.FONT_HERSHEY_PLAIN
  cv2.putText(image,text,(xcoord,ycoord), font, 1, (0,255,0), 1, cv2.LINE_AA)

# Display the resulting frame
# following blocks should be at the same indentation level as the main for
## only two spaces!

  cv2.imshow('Video', image)
  key = cv2.waitKey(1) & 0xFF

# clear the stream in preparation for the next frame
  rawCapture.truncate()
  rawCapture.seek(0)


# if the 'p' key was pressed, take a picture and save it to disk
  if key == ord("p"):
    filename = ('face-' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
    cv2.imwrite(filename, image)
#    filename = datetime.now().strftime("%Y%m%d-%H%M%S")
#    cv2.imwrite(('face-' + filename + '.jpg'), image)
    resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    cv2.namedWindow("YOUR_PICTURE")
    cv2.imshow("YOUR_PICTURE", resized)
    cv2.waitKey(1)


# if the `q` key was pressed, break from the loop
  if key == ord("q"):
    cv2.destroyAllWindows()
    break


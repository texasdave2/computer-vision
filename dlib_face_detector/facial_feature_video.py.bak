# USAGE
# python facial_landmarks.py

# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import time

# pi camera imports
from picamera.array import PiRGBArray
from picamera import PiCamera


# code for raspberry pi camera
camera = PiCamera()
camera.resolution = (1200, 800)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(1200, 800))

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

# loop over the (x, y)-coordinates for the facial landmarks
# and draw them on the image
    for (x, y) in shape:
      cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

# Display the resulting frame
# following blocks should be at the same indentation level as the main for
## only two spaces!

  cv2.imshow('Video', image)
  key = cv2.waitKey(1) & 0xFF

# clear the stream in preparation for the next frame
  rawCapture.truncate()
  rawCapture.seek(0)

# if the `q` key was pressed, break from the loop
  if key == ord("q"):
    cv2.destroyAllWindows()
    break


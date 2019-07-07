import cv2
import time

# pi camera imports
from picamera.array import PiRGBArray
from picamera import PiCamera


# code for raspberry pi camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow camera to warm up
time.sleep(0.1)

# haar cascade data
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


# Capture frame-by-frame

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
  image = frame.array
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

# Draw a rectangle around the faces
  for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
  cv2.imshow('Video', image)
  key = cv2.waitKey(1) & 0xFF

# clear the stream in preparation for the next frame
  rawCapture.truncate(0)
	
# if the `q` key was pressed, break from the loop
  if key == ord("q"):
    cv2.destroyAllWindows()
    break



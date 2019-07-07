#time lapse image maker

import time
import picamera

video_days = 1
frames_per_hour = 60
hours = 3
frames = frames_per_hour * hours * video_days

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.resolution = (640, 480)
        cam.capture("/home/pi/Pictures/time_lapse/frame%03d.jpg" % frame)

# capture the images

for frame in range(frames):
    start = time.time()
    capture_frame(frame)
    time.sleep(int(60 * 60 / frames_per_hour) - (time.time() - start))
    
quit()

#cycles through all the effects in the picamera library

from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.start_preview()
#sleep(3)
#camera.capture('/home/pi/Desktop/image.jpg')
#camera.stop_preview()


for effect in camera.IMAGE_EFFECTS:
    camera.start_preview()
    camera.image_effect = effect
    camera.annotate_text = effect
    sleep(2)
    camera.stop_preview()

quit()

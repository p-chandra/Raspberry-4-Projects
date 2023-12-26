import time, libcamera
from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
from signal import pause
import cv2

picam = Picamera2()	
pir = MotionSensor(18)		#18 is the gpio pin connected to the motionsensor
cam = cv2.VideoCapture(1)	#/dev/video# 

config = picam.create_preview_configuration()	#Default config
picam.configure(config)				#Setting configs
picam.start()					#Start camera
ret, image = cam.read()

counter = 0


def take_picture():
   picam.capture_file("/home/pi/Pictures/pi-camera/image.jpg")
   cv2.imwrite('/home/pi/Pictures/webcam/image.jpg', image)

def motion_function(timeout):
   print("Motion Detected")
   take_picture()

def no_motion_function():
   print("Motion stopped")

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()
picam.stop()
cam.release()

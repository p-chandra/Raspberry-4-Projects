from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(18)

def motion_function():
	print("Motion Detected")

def no_motion_function():
	print("No Motion Detected")

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()

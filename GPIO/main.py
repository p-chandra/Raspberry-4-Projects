import time
import neopixel
import board
from picamera2 import Picamera2
from gpiozero import MotionSensor

# Configure LED strip
pixel_pin = board.D18  # GPIO 18
num_pixels = 8         # Number of LEDs in your strip
ORDER = neopixel.GRB   # WS2812 strips are often Green-Red-Blue

# Initialize the strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)


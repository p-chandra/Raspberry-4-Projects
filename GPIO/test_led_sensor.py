import time
import neopixel
import board

# Install Python3 pip and venv if you don't have them
# sudo apt install python3-pip python3-venv -y

# Create a virtual environment (recommended for modern Raspberry Pi OS)
# python3 -m venv ~/my_env
# source ~/my_env/bin/activate

# Install the required libraries for controlling the WS2812 LED strip
# pip3 install rpi_ws281x adafruit-circuitpython-neopixel

# Run the script with sudo to access GPIO pins
# sudo ~/my_env/bin/python3 Raspberry-4-Projects/GPIO/test_led_sensor.py

# Configuration
pixel_pin = board.D18  # GPIO 18
num_pixels = 8         # Number of LEDs in your strip
ORDER = neopixel.GRB   # WS2812 strips are often Green-Red-Blue

# Initialize the strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

try:
    print("Starting LED sequence. Press Ctrl+C to stop.")
    
    while True:
        pixels.fill((255, 0, 0))  # Red
        pixels.show()
        time.sleep(1)
        
        pixels.fill((0, 0, 255))  # Blue
        pixels.show()
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[Ctrl+C detected] Cleaning up...")

finally:
    # Now Python knows exactly what clear_strip() is!
    pixels.fill((0, 0, 0))
    pixels.show()
    print("LEDs safely turned off.")
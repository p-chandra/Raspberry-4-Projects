from machine import UART
import time

uart = UART(0, baudrate=115200)

while True:
    if uart.any():
        data = uart.read()
        uart.write(b"Echo: " + data)
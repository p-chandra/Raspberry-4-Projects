# Start Guide
You should have a micro controller plugged/powered by the raspberry pi. You can check using this command `ls /dev/ttyACM*`. 

You may need to enter the python virtual environment. `source ~/my_env/bin/activate`. Read the README file in the GPIO folder for instructions. 

If the output matches then you're good to go. Open MicroPython REPL with `mpremote connect auto repl`. To exit press `'CTRL + ]'` 

To upload a file to the microcontroller `mpremote fs cp blink.py :` and to run `mpremote run blink.py`

IMPORTANT NOTE: when pressing Ctrl-C to stop the code you will notice that the LED is still blinking. CTRL-C stops your host process, not the code running on the microcontroller — the board continues executing the uploaded script (or a boot script) unless the board itself receives an interrupt/reset. To stop interrupt the code you can enter `mpremote repl` and then press Ctrl-C to interrupt. 

## Testing UART (GPIO non USB)

First make sure that you have serial hardware enabled from raspi-config. Run `ls -l /dev/serial0` and you should see something like "/dev/serial0 -> ttyS0" If you don't then your UART is not connected. 

Install a serial terminal minicom `sudo apt install minicom`. 

Upload the test_uart.py to the micro controller and run it. Then open a new terminal and execute `minicom -D /dev/serial0 -b 115200`. The serial0 is using the pins connected from RaspberryPi to Micro Controller. So essentially communicating using UART via pin connections.

in the minicom terminal here are the two essential commands to know
- Ctrl+A, then Z → Help menu
- Ctrl+A, then X → Exit

You can also use python serial communication `sudo apt install python3-serial`. Run the rasp_python_serial.py on the new terminal and it should echo back hello

Remember to mpremote repl then Ctrl-C to exit the code running on micro controller. 

## Testing I2C

install `sudo apt install i2c-tools -y i2c-tools python3-smbus2`

run `i2cdetect -y 1` and you should see a chart


## Testing SPI

run `ls /dev/spidev*` and you should see 

- /dev/spidev0.0
- /dev/spidev0.1

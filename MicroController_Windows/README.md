# Raspberry Pi Pico on VS Code

This test environment uses VSC ode instead of Thonny IDE to run scripts on the Raspberry Pi Pico micro controller.

The extension Raspberry Pi Pico is a must for this to work. Install this extension and it will install other extensions along side automatically such as:
- Serial Monitor
- RTOS Views
- Peripheral Viewer
- MicroPico
- CortexDebug

If these extensions listed above aren't installed along side of Raspberry Pi Pico extension, then it must mean that there was an update and so do not install the extras

# Set Up

Once the extensions are installed, on the left hand side select Raspberry Pi Pico Project extension. Then select New MicroPython Project. Set the location to MicroController Folder in the Raspberry Pi Repo. By doing it like this you can work on other projects non micro controller related and also you can connect to the to the micro controller on a new tab versus dedicating a whole window to just one project.

Currently I have 2 setups. A raspberry pi 4 connected to a pico and a windows machine connected to a pico.

# Goals

I will be creating projects utilizing communication protocols such as UART I2C and SPI in both python and C programming
# Raspberry Pi 4 Pinout Reference

Below is the structured markdown reference for the Raspberry Pi 4 pinout structure, including pin types, communication protocols, hardware capabilities, and a full 40-pin layout chart.

---

## 1. Overview & Pin Types

The Raspberry Pi 4 features a 40-pin GPIO (General Purpose Input/Output) header that allows communication with external sensors, actuators, and electronic circuits. The pins are divided into the following categories:

* **GPIO Pins:** Programmable digital pins that can be configured as inputs (to read states like a button press) or outputs (to drive components like LEDs or relays).
* **Power Pins:** Rails providing continuous voltage. 
  * **5V Power:** Pins 2 and 4.
  * **3.3V Power:** Pins 1 and 17.
* **Ground (GND) Pins:** Used to complete electrical circuits. There are 8 ground pins on the header: **6, 9, 14, 20, 25, 30, 34, and 39**.
* **Special Function Pins:** Multi-plexed pins that carry underlying hardware serial communication protocols (I2C, SPI, UART, PWM).

---

## 2. Special Function Communication Protocols

### I2C (Inter-Integrated Circuit)
A synchronous, multi-master/multi-slave, packet-switched, single-ended, serial communication bus. It uses two lines to connect multiple peripherals to the Pi using only two data lines:
* **SDA (Serial Data)**
* **SCL (Serial Clock)**

### SPI (Serial Peripheral Interface)
A synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems. It offers faster throughput than I2C and utilizes a master-slave architecture requiring four core lines:
* **SCLK (Serial Clock)**
* **MOSI (Master Out Slave In)**
* **MISO (Master In Slave Out)**
* **CE / SS (Chip Enable / Slave Select)**

### UART (Universal Asynchronous Receiver/Transmitter)
An asynchronous serial communication protocol that translates data between parallel and serial forms. It is commonly configured for terminal debugging console access or communicating with serial modules (e.g., GPS, Bluetooth) using two pins:
* **TXD (Transmit Data)**
* **RXD (Receive Data)**

---

## 3. 40-Pin GPIO Layout Table

The physical pins alternate between the Left Column (Odd Numbers) and the Right Column (Even Numbers). 

| Left Side (Odd Pins) | Pin # | Pin # | Right Side (Even Pins) |
| :--- | :---: | :---: | :--- |
| **3.3V Power** | **1** | **2** | **5V Power** |
| GPIO 2 (`SDA`) | **3** | **4** | **5V Power** |
| GPIO 3 (`SCL`) | **5** | **6** | **Ground (GND)** |
| GPIO 4 (`GPCLK0`) | **7** | **8** | GPIO 14 (`TXD`) |
| **Ground (GND)** | **9** | **10** | GPIO 15 (`RXD`) |
| GPIO 17 | **11** | **12** | GPIO 18 (`PWM0`) |
| GPIO 27 | **13** | **14** | **Ground (GND)** |
| GPIO 22 | **15** | **16** | GPIO 23 |
| **3.3V Power** | **17** | **18** | GPIO 24 |
| GPIO 10 (`MOSI`) | **19** | **20** | **Ground (GND)** |
| GPIO 9 (`MISO`) | **21** | **22** | GPIO 25 |
| GPIO 11 (`SCLK`) | **23** | **24** | GPIO 8 (`CE0`) |
| **Ground (GND)** | **25** | **26** | GPIO 7 (`CE1`) |
| GPIO 0 (`ID_SD`) | **27** | **28** | GPIO 1 (`ID_SC`) |
| GPIO 5 | **29** | **30** | **Ground (GND)** |
| GPIO 6 | **31** | **32** | GPIO 12 (`PWM0`) |
| GPIO 13 (`PWM1`) | **33** | **34** | **Ground (GND)** |
| GPIO 19 (`MISO`) | **35** | **36** | GPIO 16 |
| GPIO 26 | **37** | **38** | GPIO 20 (`MOSI`) |
| **Ground (GND)** | **39** | **40** | GPIO 21 (`SCLK`) |

---

## 4. Hardware Supported Functions (RP1 / IO_BANK0)

The core architecture supports multiplexing the GPIO pins into several dedicated interfaces:
* **5 x UART** interfaces
* **6 x SPI** interfaces
* **4 x I2C** interfaces
* **2 x I2S** interfaces (Clock Producer and Clock Consumer instances)
* **Registered IO (RIO)** interface
* **24-bit DPI** output
* **4-channel PWM** output
* Stereo PWM audio output (`AUDIO_OUT`)
* General-purpose clock input and output (`GPCLK`)
* **eMMC/SDIO** bus with a 4-bit interface
* Interrupt generation driven by pin logic levels or edge transitions

---

> **Console Shortcut:** When working directly on a Raspberry Pi local environment, you can output an interactive visual reference layout anytime by opening the command terminal and running:
> ```bash
> pinout
> ```
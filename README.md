# Aegis Core RP2350A 

# Overview 

When I decided to make the Aegis Core, I set out to make a clean, professional looking, all-in-one controller board for high end automated turrets and robotic aiming platforms. Typically, projects of this kind involve a clutter of jumper wires, stacked development boards, and external regulator boards, all of which can be affected by electrical noise and poor connections in high-vibration moments.

I designed Aegis Core to solve these challenges head-on. By integrating everything onto a custom 2-Layer PCB powered by the new RP2350A, Aegis Core handles real-time USB tracking telemetry, high-current low-side N-Channel MOSFET flywheel driver stages, multi-channel precision servo actuation, automated reloading sequences, and system audio feedback, all driven natively from a compact 2S Li-ion battery architecture.

# How It Works: System Architecture

Aegis Core is structured into three primary electrical and computational domains to ensure high performance and zero brownouts under heavy mechanical load.

1. Power Regulation & Destribution
    Input Stage: Power is connected through an XT30 connector (+BATT) directly connected to a bulk filtering electrolytic capacitor where the severe    inductive current transients that occur when the flywheel motors and servos snap into action are absorbed.
  
  Buck Regulation: A high-efficiency, 500kHz synchronous buck converter reduces the battery voltage range of approximately 7.4V nominal/8.4V max to   a strong and clean 5.0V system rail. Input voltage allows for up to 8S batteries to be connected, although it is not    recommend. Input voltage ranges from 6-30V. The input ceramic decoupling capacitors, output bypass capacitors, bootstrap capacitor and soft-start capacitor are carefully chosen low-ESR surface-mount devices to ensure loop stability. 

2. Processing & Core Logic
   The RP2350 microcontroller is located near the center of the board and is supported by the external Winbond SPI Flash memory, and a 3225-package    crystal oscillator with high precision.

   The RP2350A processes incoming USB serial tracking commands from a host computer running computer vision scripts, translating coordinates into
   smooth PWM signals and hardware triggers in real-time.

3. Actuation & Peripherals
   Flywheel Control: Flywheel cages are driven by a pair of high-current brushed motors controlled by a low-side A03400A N-Channel MOSFET high speed
   electronic switch.

   Servos: Three exclusive header channels for accurate PWM output of 50Hz for pan, tilt, and an automatic reload indexing mechanism.

   Audio & Input: An integrated piezo buzzer emits audible telemetry signals (startup melodies, arming tones and firing clicks), and the tactile
   push buttons allow the user with BOOTSEL and RESET buttons.

# Visuals & Layouts

   Schemaitc:

   <img width="1392" height="891" alt="image" src="https://github.com/user-attachments/assets/8b5833c2-1684-4783-a9b0-4fdb03ee47af" />


   Board Layout:

   <img width="813" height="637" alt="image" src="https://github.com/user-attachments/assets/d8bc6f1d-df69-4ba8-9adc-b2d72eb7c6d2" />


   3D Model:

<img width="762" height="636" alt="image" src="https://github.com/user-attachments/assets/3a36af24-6eda-4ba8-b78d-382a8a8dde8f" />



# Wiring & Interconnect Diagram

Because Aegis Core concentrates peripheral connections onto organized onboard headers, external hand-wiring is kept to an absolute minimum:

- XT30 Connector: Main 2S Li-ion battery input
- Flywheel Output Terminals: Screw terminals connected to the drain pins of the A03400A MOSFET low-side drivers.
- Pan Servo Header: 3-pin header (signal to RP2350 GPIO 0, 5V, GND)
- Tilt Servo Header: 3-pin header (signal to RP2350 GPIO 1, 5V, GND)
- Reload Servo Header: 3 pin header (signal to RP2350 GPIO 2, 5V, GND)
- RGB LED Strip Input: 01x04 Screw Terminal (GPIO 26, 27, 28, 5V). Built for common anode strips.
   

# BOM

| Part / Description | Notes / Function | Qty | Unit Price | Total Price | Vendor |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Electrolytic Capacitor 220uF | Electrical Noise Filtering | 10 | $0.04 | $0.40 | LCSC |
| Ceramic Capacitor 4.7uF | Passive | 10 | $0.02 | $0.20 | LCSC |
| Ceramic Capacitor 22pF | Passive | 50 | $0.01 | $0.50 | LCSC |
| Ceramic Capacitor 22uF | Passive | 20 | $0.02 | $0.40 | LCSC |
| 1N5819 Diode | Passive | 20 | $0.04 | $0.80 | LCSC |
| XT30 Power Connector | 2S Lithium Battery Input | 5 | $0.23 | $1.15 | LCSC |
| 01x02 Terminal Block | Motor Input | 5 | $0.10 | $0.50 | LCSC |
| Inductor 15uH | Step Down Regulator (Passive) | 5 | $0.10 | $0.50 | LCSC |
| AO3400A N-Channel Mosfet | One-Way Motor Control | 20 | $0.04 | $0.80 | LCSC |
| Resistor 33 Ohms (100 Pack) | Passive | 1 | $0.17 | $0.17 | LCSC |
| Resistor 100K Ohms (100 Pack) | Passive | 1 | $0.21 | $0.21 | LCSC |
| Resistor 100 Ohms (100 Pack) | Passive | 1 | $0.16 | $0.16 | LCSC |
| Resistor 52.3K Ohms (100 Pack) | Passive | 1 | $0.17 | $0.17 | LCSC |
| RP2350A | Raspberry Pi Microcontroller - Brain of the board | 1 | $1.30 | $1.30 | LCSC |
| W25Q128JVSIQ 128MBit Flash Memory | Flash Memory for RP2350A | 1 | $2.80 | $2.80 | LCSC |
| TPS62933DRLR Step Down IC | Voltage Step Down IC | 1 | $0.48 | $0.48 | LCSC |
| Crystal 12MHz | Passive | 5 | $0.09 | $0.45 | LCSC |
| PCB (5 pcs) | Main Board to assemble components on | 1 | $4.00 | $4.00 | JLCPCB |
| Tax & shipping | For the whole order | -- | -- | -- | -- |

# Flashing the Firmware

Download and install the MicroPython Firmware. Download and install the MicroPython Firmware.
Go to the official MicroPython downloads page or the RP2350 port repository to download the latest stable RP2350 .uf2 firmware.

Save the .uf2 file to your computer.

To put Aegis Core in BOOTSEL Mode, follow the steps below.
Find BOOT button (SW1) and RESET button (SW2) on your Aegis Core board.

Press and hold the BOOT button on the Aegis Core, then connect the Aegis Core board to your computer using the USB-C port, and hold the BOOT button down.

Press the BOOT button and then release it. A chime will sound and your computer will identify the board as a virtual USB mass storage device (RPI-RP2 or RP2350).

This step requires flashing the firmware.Step 3: Flash Firmware.
Copy the downloaded MicroPython .uf2 file to the virtual drive window.

The file will now be automatically copied, the board will restart and exit BOOTSEL mode.

Select Step 4: Verify Connection from the pop-up menu.From the pop-up window, choose Step 4: Verify Connection.
Download and open Thonny.

Click on Tools > Options... and then the Interpreter tab.

Select MicroPython (Raspberry Pi Pico) as the interpreter and ensure that the correct USB COM port for Aegis Core is selected. Click OK.

Confirm that the MicroPython interactive prompt (>>>) is on by checking the Shell window below.

Click "step 5" to upload the main.py Control Script.Click step 5 to upload the main.py Control Script.
In Thonny, create a new file, and paste your control script into it, then select File > Save As... > MicroPython device.

Save it to the root directory as file main.py.

Click on the Aegis Core hardware RESET button. The start-up tone should be heard through the buzzer (BZ1) and the console shall print out initialisation logs.

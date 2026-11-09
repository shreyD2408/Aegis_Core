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

    <img width="900" height="675" alt="image" src="https://github.com/user-attachments/assets/41cfcbc3-bc01-4a1e-a4a4-481c7179d8cd" />


# Wiring & Interconnect Diagram

Because Aegis Core concentrates peripheral connections onto organized onboard headers, external hand-wiring is kept to an absolute minimum:

- XT30 Connector: Main 2S Li-ion battery input
- Flywheel Output Terminals: Screw terminals connected to the drain pins of the A03400A MOSFET low-side drivers.
- Pan Servo Header: 3-pin header (signal to RP2350 GPIO 0, 5V, GND)
- Tilt Servo Header: 3-pin header (signal to RP2350 GPIO 1, 5V, GND)
- Reload Servo Header: 3 pin header (signal to RP2350 GPIO 2, 5V, GND)
- RGB LED Strip Input: 01x04 Screw Terminal (GPIO 26, 27, 28, 5V). Built for common anode strips.
   



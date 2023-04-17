# Rain-detector-system-project
This is Rain detector system IoT based project, developed it using python language and integrate with sensors and actuators and FavorIoT cloud platform

How to setup this project:

1. For this project, all the component that we must have are:
   i. NodeMCU ESP32
   ii. YL-83 Rain Sensor Control Board
   iii. YL-83 Rain Sensor Detection Board
   iv. Breadboard
   v. Jumper wire (M to F)
   vi. Micro USB

2. Once all the component are already available, we assemble the component based on the circuit diagram provided. You can see the circut diagram named as "Circuit    diagram 1. png"

3. To connect YL-83 Rain Sensor Detection Board with NodeMCU ESP32, you have to follow this Pin Wiring configuration:
   VCC ---> Vin
   GND ---> GND
   A0 ---> EN
   
4. Setup FavorIoT platform. Before setup, you must have an account or register new one. You can access the platform via this link: https://www.favoriot.com/

5. To setup the favorIoT, you can follow the step in youtube https://www.youtube.com/@FAVORIOT

6. Once you get the API key, you need to put it into the source code

7. The setup is already installed. Now the project can be launch

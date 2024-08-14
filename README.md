ESP32 LoRa  Application

Overview

This project uses MicroPython-programmed ESP32 LoRa devices to construct a basic Internet of Things application. The application sets up a simple web server for data management and visualization, shows off long-range device connection, and shows important information on an OLED panel.

Features

Wi-Fi availability
synchronization of NTP time
OLED display to show the time and device IP
Data packet transmission and reception using LoRa communication
Data logging with control over file size
Web server for showing data that has been logged Hardware specifications
OLED display on the ESP32-S3 LoRa device (SSD1306)
USB cable needed for power and programming Software Requirements
The MicroPython firmware for the ESP32-S3 Thonny IDE (or any other IDE compatible with MicroPython)
Libraries that are necessary: ssd1306, sx127x Configuration Guide
Firmware for MicroPython Flash

Get the most recent MicroPython firmware for the ESP32-S3 by visiting micropython.org.
Use esptool.py—chip esp32s3 erase_flash to erase the ESP32 flash.
Using esptool.py—chip esp32s3—baud 460800 write_flash -z 0x0 esp32s3-XXXXXXX.bin, flash the updated firmware.
Substitute the real firmware version for XXXXXXXX.
Set Up Necessary Libraries

ESP32 connection made with Thonny IDE
Utilize Tools > Control packages for ssd1306 installation
Install the sx127x library manually to enable LoRa.
Set Up the Program

In your IDE, open main.py.
Revise the WiFi login credentials:
'your_wifi_ssid' is the SSID.
'your_wifi_password' is the password.
If necessary, change pin configurations to fit your hardware arrangement.
Put the Code Online

Transfer the altered main.py file to your ESP32 gadget.
Using the ESP32 device's Application Power

The Device will automatically

Establish a WiFi connection
Coordinate time using an NTP server.
IP and time should be shown on the OLED screen.
Open the LoRa communication channel.
Start up a web server to display data.
Join the same Wi-Fi network as the ESP32 and use a web browser to go to http://<ESP32-IP-ADDRESS> to view logged data.

Troubleshooting
Verify your login information and network availability if the device is unable to establish a Wi-Fi connection.
Check for correct wiring and antenna connection in case of LoRa communication problems.
In case of non-operation of the OLED display, check the I2C connections and address
Making a contribution
We welcome your contributions to this project. Kindly fork the repository and send in a pull request including the updates you made.

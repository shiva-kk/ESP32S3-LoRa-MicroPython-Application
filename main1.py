from machine import Pin, I2C
from sx1262 import SX1262
import ssd1306
import time
import network

# Reset the device
reset_pin = Pin(21, Pin.OUT)
reset_pin.value(0)
time.sleep(0.1)
reset_pin.value(1)

# Initialize I2C and OLED display
i2c = I2C(0, scl=Pin(18), sda=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize the SX1262 LoRa module
sx = SX1262(spi_bus=1, clk=9, mosi=10, miso=11, cs=8, irq=14, rst=12, gpio=13)

# Configure LoRa settings
sx.begin(
    freq=923, bw=500.0, sf=12, cr=8, syncWord=0x12,
    power=-5, currentLimit=60.0, preambleLength=8,
    implicit=False, implicitLen=0xFF,
    crcOn=True, txIq=False, rxIq=False,
    tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True
)

# Function to display messages on the OLED screen
def display_message(line1, line2):
    display.fill(0)  # Clear the screen
    display.text(line1, 0, 0)
    display.text(line2, 0, 10)
    display.show()

# Callback function to handle LoRa events
def lora_callback(events):
    if events & SX1262.RX_DONE:
        msg, err = sx.recv()
        status_msg = SX1262.STATUS[err]
        try:
            # Expecting messages in the format "device_id:data"
            device_id, data = msg.decode('utf-8').split(':', 1)
        except ValueError:
            device_id = 'Unknown'
            data = msg.decode('utf-8')
        
        # Display received message
        print('Received from {}: {}, {}'.format(device_id, data, status_msg))
        display_message(f'From: {device_id}', f'Data: {data}')
    elif events & SX1262.TX_DONE:
        print('Transmission complete.')

# Function to send messages
def transmit_message(device_id, data):
    message = f'{device_id}:{data}'
    sx.send(message.encode('utf-8'))

# Set the callback function for LoRa events
sx.setBlockingCallback(False, lora_callback)

# Main loop
while True:
    transmit_message('Group 2', 'Hello People!')
    time.sleep(10)
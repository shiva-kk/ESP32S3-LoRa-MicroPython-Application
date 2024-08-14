from machine import Pin, SPI, I2C
from ssd1306 import SSD1306_I2C
from sx127x import SX127x  # Import your LoRa module library

# Define SPI and I2C pins
spi = SPI(baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)
reset = Pin(14, Pin.OUT)

# Initialize LoRa
lora = SX127x(spi, cs, reset)

# Initialize the I2C and OLED display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Send a message
    lora.send('Hello LoRa')

    # Display message on OLED
    oled.fill(0)
    oled.text('Sending: Hello', 0, 0)
    oled.show()

from machine import Pin, I2C
import ssd1306
import time

reset_pin = Pin(21, Pin.OUT)
reset_pin.value(0)  
time.sleep(0.1)     
reset_pin.value(1)  

i2c = I2C(0, scl=Pin(18), sda=Pin(17))

devices = i2c.scan()

if devices:
    try:
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.text('Hello World!', 0, 0)
        oled.show()
    except Exception as e:
        print('Error initializing OLED:', e)
else:
    print('No I2C devices found.')
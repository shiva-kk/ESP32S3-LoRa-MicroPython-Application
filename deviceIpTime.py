from machine import Pin, I2C
import ssd1306
import time
import network
import ntptime

# Wi-Fi credentials
#ssid = 'MikroTik-D47CBA'
#password = '12345678'

ssid = 'ManaWifi'
password = 'richierich@180'

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    max_attempts = 10
    attempt = 0
    
    while attempt < max_attempts and not wlan.isconnected():
        print('Attempting to connect...')
        attempt += 1
        time.sleep(1)
    
    if wlan.isconnected():
        print('Connected to Wi-Fi')
        print('Network configuration:', wlan.ifconfig())
    else:
        print('Failed to connect to Wi-Fi')

# Initialize I2C and OLED
def init_oled():
    reset_pin = Pin(21, Pin.OUT)
    reset_pin.value(0)
    time.sleep(0.1)
    reset_pin.value(1)

    i2c = I2C(0, scl=Pin(18), sda=Pin(17))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    return oled

# Draw a circle
def draw_circle(oled, x0, y0, radius, color):
    f = 1 - radius
    ddF_x = 1
    ddF_y = -2 * radius
    x = 0
    y = radius

    oled.pixel(x0, y0 + radius, color)
    oled.pixel(x0, y0 - radius, color)
    oled.pixel(x0 + radius, y0, color)
    oled.pixel(x0 - radius, y0, color)

    while x < y:
        if f >= 0:
            y -= 1
            ddF_y += 2
            f += ddF_y
        x += 1
        ddF_x += 2
        f += ddF_x

        oled.pixel(x0 + x, y0 + y, color)
        oled.pixel(x0 - x, y0 + y, color)
        oled.pixel(x0 + x, y0 - y, color)
        oled.pixel(x0 - x, y0 - y, color)
        oled.pixel(x0 + y, y0 + x, color)
        oled.pixel(x0 - y, y0 + x, color)
        oled.pixel(x0 + y, y0 - x, color)
        oled.pixel(x0 - y, y0 - x, color)

# Draw some graphics for fun
def draw_graphics(oled):
    oled.rect(0, 0, 128, 64, 1)  # Border rectangle
    oled.line(0, 0, 127, 63, 1)  # Diagonal line
    oled.line(0, 63, 127, 0, 1)  # Diagonal line
    draw_circle(oled, 64, 32, 10, 1)  # Circle in the center

# Main function
def main():
    connect_to_wifi()
    oled = init_oled()
    
    # Sync time with NTP server
    ntptime.settime()

    while True:
        oled.fill(0)
        
        ifconfig = network.WLAN(network.STA_IF).ifconfig()
        ip_address = ifconfig[0]
        local_time = time.localtime()
        formatted_time = "{:02}:{:02}:{:02}".format(local_time[3], local_time[4], local_time[5])
        
        oled.text('IP: {}'.format(ip_address), 0, 0)
        oled.text('Time: {}'.format(formatted_time), 0, 10)
        
        draw_graphics(oled)
        
        oled.show()
        time.sleep(1)

# Run the main function
main()
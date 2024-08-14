import network
import time

# Replace with your Wi-Fi credentials
ssid = 'MikroTik-D47CBA'
password = '12345678'

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    wlan.active(True)  # Activate the interface
    wlan.connect(ssid, password)  # Connect to Wi-Fi

    max_attempts = 10
    attempt = 0

    # Wait for the connection to establish
    while attempt < max_attempts and not wlan.isconnected():
        print('Attempting to connect...')
        attempt += 1
        time.sleep(1)

    if wlan.isconnected():
        print('Connected to Wi-Fi')
        print('Network configuration:', wlan.ifconfig())
    else:
        print('Failed to connect to Wi-Fi')

# Call the function to connect to Wi-Fi
connect_to_wifi()
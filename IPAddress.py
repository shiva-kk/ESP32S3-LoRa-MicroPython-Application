import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected():
    ip_address = wlan.ifconfig()[0]
    print('Device IP Address:', ip_address)
else:
    print('Device is not connected to a network.')

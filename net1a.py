# net1a.py
# written by G.D. Walters
# for FCM 185 September 2022

import machine
import network
import time
import secret
import sys

# Check that the board is a Pico-W with wireless support
def GetWhichPico():
    which1 = sys.implementation
    if "Pico W" in (sys.implementation[2]):
        return True
    else:
        return False
    
if GetWhichPico():
    # Setup onboard LED
    led=machine.Pin("LED",machine.Pin.OUT)
    led.off()
    # Setup Network
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    # Provide SSID and PASSWORD from secret.py file
    ap=secret.SSID
    pwd=secret.PASSWORD
    # Try to connect to the wireless network
    wlan.connect(ap,pwd)
    # Loop until we get connected
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting to connect")
        time.sleep(1)
    # Print the status value and the ifconfig values
    print(wlan.status())
    print(wlan.ifconfig())
    # Turn on the onboard LED
    led.on()
else:
    print('This microcontroller board does not support Wireless!')
    

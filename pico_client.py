from machine import Pin
import network
import socket

WIFI_SSID = "AgencyRobot"
WIFI_PASSWORD = "theagency3021"

SERVER_IP = '10.30.21.200'
PORT = 8000

pins = range(2,17)
buttons = []

for pin in pins:
    buttons.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))
    
def check_buttons():
    n = 0
    for i in range(len(buttons)):
        #Deal with it
        n += buttons[i].value() * 2**i
    return n

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
print(wlan)
#Maybe assign an ip address?
#Right here, please

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))


button_state = 0
while True:
    new_state = check_buttons()
    if button_state != new_state:
        button_state = new_state
        sock.send(str(button_state)+'\n')
        print(bin(button_state))
    #sock.send("whatever")
    

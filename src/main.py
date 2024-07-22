import network
from machine import Pin
import time

# Config file name:
WIFI_CONFIG_FILE = 'config.txt'
FALSE = ['0', "false", "False", "FALSE", False, None, "no", "No", "NO", "N"]
TRUE = ['1', "true", "True", "TRUE", True, "yes", "Yes", "YES", "Y"]

# Define row and column pin numbers for the 5x5 matrix
ROWS = [1, 2, 3, 4, 5]
COLS = [6, 7, 8, 9, 10]

# Initialize row and column pins
#ROW_PINS = [Pin(row, Pin.OUT) for row in ROWS]
#COL_PINS = [Pin(col, Pin.IN, Pin.PULL_UP) for col in COLS]

LED_BUS = 22
#LED_PIN = Pin(LED_BUS, Pin.OUT)

#time.sleep(1)


def read_wifi_credentials_from_ini(file_path=WIFI_CONFIG_FILE):
    ssid = None
    password = None
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('ssid='):
                    ssid = line.strip().split('=')[1]
                elif line.startswith('password='):
                    password = line.strip().split('=')[1]
                elif line.startswith('wifi_enabled'):
                    wifi_enabled = line.strip().split('=')[1]
                    if wifi_enabled in ['0', "false", "False", "FALSE"]:
                        return None, None
        return ssid, password
    except FileNotFoundError:
        return None, None


def scan_buttons():
    button_presses = []  # Store coordinates of pressed buttons as tuples (row, col)
    for row_index, row_pin in enumerate(ROW_PINS):
        row_pin.value(0)  # Activate row
        for col_index, col_pin in enumerate(COL_PINS):
            if not col_pin.value():  # Check if button is pressed
                button_presses.append((row_index, col_index))
        row_pin.value(1)  # Deactivate row
    return button_presses


def connect_to_wifi(ssid, password):
    print("Connecting to WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(wlan.scan())

    #wlan.connect(ssid, password)
    #while not wlan.isconnected():
    #    pass
    #print("Connected to WiFi")
    #return wlan


def main():
    # set the boot up neopixel to blue
    #import neopixel
    #array = neopixel.NeoPixel(LED_PIN, 35)
    #array.fill((1, 1, 1))
    #array.write()
    #array.fill((0,0,0))
    #array.write()



    ssid, password = read_wifi_credentials_from_ini()
    if ssid and password:
        wlan = connect_to_wifi(ssid, password)


    #last_ntp_update = time.time()

    while True:
        ...
        #pressed_buttons = scan_buttons()
        #if pressed_buttons:
        #    print("Buttons pressed:", pressed_buttons)
        #
        # Periodic NTP time update
        #
        #if time.time() - last_ntp_update > 300:
        #    last_ntp_update = time.time()
        #
        # time.sleep(0.1)  # Main loop delay

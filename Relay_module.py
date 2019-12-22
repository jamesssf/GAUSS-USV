# This file is to control the relays
# There are 8 relays
# Relay 1 -> GPIO 17
# Relay 2 -> GPIO 27
# Relay 3 -> GPIO 15
# Relay 4 -> GPIO 16
# Relay 5 -> GPIO 13
# Relay 6 -> GPIO 19
# Relay 7 -> GPIO 26
# Relay 8 -> GPIO 22

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)                            # GPIO.BOARD is using the numbers of GPIO
pinList = [17, 27, 15, 16, 13, 19, 26, 22]          # Used for initializing the relays below
samplePins = [13, 19, 26, 22]                       # Sent to Suck_it for iterating through samples

# set all pins to high so the relays are closed, because they are active low relays
GPIO.setup(pinList, GPIO.OUT, initial=GPIO.HIGH)     # Setting the GPIO pins as outputs and high

flush_pin = 17                                       # Relay connected to the solonoid for flushing the system
pump_pin = 15                                        # Relay connected to the peristaltic pump
pump_status = GPIO.input(pump_pin)                   # Used to check if the pump is on or off

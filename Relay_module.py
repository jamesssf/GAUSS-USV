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

GPIO.setmode(GPIO.BOARD)  #BOARD is using the numbers of GPIO
pinList = [17, 27, 15, 16, 13, 19, 26, 22]  #used for initializing the relays
sample_1 = 13   #relay connected to sample container 1
sample_2 = 19   #relay connected to sample container 2
sample_3 = 26   #relay connected to sample container 3
sample_4 = 22   #relay connected to sample container 4
flush = 17      #relay connected to the solonoid for flushing the system
pump = 15       #relay connected to the peristaltic pump

# set all pins to high so the relays are closed, because they are active low relays
for i in pinList:
    GPIO.setup(i, GPIO.setup, GPIO.OUT)     #setting the GPIO pins as outputs
    GPIO.output(i, HIGH)                    #iterate through all pins and set to high for active low relays


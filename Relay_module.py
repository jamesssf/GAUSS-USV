# Relay module for the GAUSS USV
# 12/22/2019
# Author: James Stevens
# There are 8 relays
# Relay 1 -> GPIO 17 - Flush Solenoid
# Relay 2 -> GPIO 27
# Relay 3 -> GPIO 15 - Pump Solenoid
# Relay 4 -> GPIO 16
# Relay 5 -> GPIO 13 - Solenoid 1
# Relay 6 -> GPIO 19 - Solenoid 2
# Relay 7 -> GPIO 26 - Solenoid 3
# Relay 8 -> GPIO 22 - Solenoid 4

import RPi.GPIO as GPIO   # Import GPIO module for Raspberry Pi

flushPin = 17  # Relay connected to the solonoid for flushing the system
pumpPin = 15  # Relay connected to the peristaltic pump
pinList = [17, 27, 15, 16, 13, 19, 26, 22]  # Used for initializing the relays below

def relay_init():  # set all pins to high so the relays are closed, because they are active low relays
    GPIO.setmode(GPIO.BOARD)  # GPIO.BOARD is using the numbers of GPIO
    GPIO.setup(pinList, GPIO.OUT)  # Setting the GPIO pins as outputs
    all_relay_off()  # Turn off all the relays

def get_pin(sample_counter):
    sample_pins = [13, 19, 26, 22]  # Sent to Suck_it for iterating through samples
    return sample_pins[sample_counter]  # Return the pin of the number of sample we are on

def all_relay_off():
    GPIO.output(pinList, GPIO.HIGH)  # Setting the GPIO pins as high

def pump_on():
    GPIO.out(pumpPin, LOW)  # Turn the pump on

def pump_off()
    GPIO.out(pumpPin, HIGH)  # Turn the pump off

def solenoid_on(sample_pin):
    GPIO.out(sample_pin, LOW)  # Turn the solenoid on

def solenoid_off(sample_pin)
    GPIO.out(sample_pin, HIGH)  # Turn the solenoid off

def flush_on():
    GPIO.out(flushPin, LOW)  # Turn the flush solenoid on

def flush_off()
    GPIO.out(flushPin, HIGH)  # Turn the flush solenoid off

def pump_stat():
    return GPIO.input(pumpPin)  # Used to check if the pump is on or off
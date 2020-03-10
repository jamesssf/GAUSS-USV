# Relay module for the GAUSS USV
# 12/22/2019
# Author: James Stevens
# There are 8 relays
# Relay 1 -> GPIO 17 - Solenoid 4
# Relay 2 -> GPIO 27 - 
# Relay 3 -> GPIO 5 - Solenoid 1
# Relay 4 -> GPIO 6 - Pump Solenoid
# Relay 5 -> GPIO 13 - Flush Solenoid
# Relay 6 -> GPIO 19 - Solenoid 3
# Relay 7 -> GPIO 26 - 
# Relay 8 -> GPIO 22 - Solenoid 2

import RPi.GPIO as GPIO  # Import GPIO module for Raspberry Pi

GPIO.setmode(GPIO.BCM)  # GPIO.BCM is using the numbers of GPIO


flushPin = 22  # Relay connected to the solonoid for flushing the system
pumpPin = 5  # Relay connected to the peristaltic pump
pinList = [5, 6, 13, 17, 19, 22, 26, 27]  # Used for initializing the relays below
sample_pins = [6, 13, 19, 17]  # Sent to Suck_it for iterating through samples

def relay_init():  # set all pins to high so the relays are closed, because they are active low relays
    GPIO.setmode(GPIO.BCM)  # GPIO.BCM is using the numbers of GPIO
    GPIO.setup(pinList, GPIO.OUT)  # Setting the GPIO pins as outputs
    all_relay_off()  # Turn off all the relays


def get_pin(sample_counter):
    return sample_pins[sample_counter]  # Return the pin of the number of sample we are on


def all_relay_off():
    GPIO.output(pinList, GPIO.HIGH)  # Setting the GPIO pins as high

def all_relay_on():
    GPIO.output(pinList, GPIO.LOW)


def pump_on():
    GPIO.output(pumpPin, GPIO.LOW)  # Turn the pump on


def pump_off():
    GPIO.output(pumpPin, GPIO.HIGH)  # Turn the pump off


def solenoid_on(sample_pin):
    GPIO.output(sample_pin, GPIO.LOW)  # Turn the solenoid on


def solenoid_off(sample_pin):
    GPIO.output(sample_pin, GPIO.HIGH)  # Turn the solenoid off


def flush_on():
    GPIO.output(flushPin, GPIO.LOW)  # Turn the flush solenoid on


def flush_off():
    GPIO.output(flushPin, GPIO.HIGH)  # Turn the flush solenoid off


def pump_stat():
    return GPIO.input(pumpPin)  # Used to check if the pump is on or off

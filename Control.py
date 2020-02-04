# Control module for the GAUSS USV - This is the main code for the USV
# 12/22/2019
# Author: James Stevens

import Relay  # Import the module for the relays
import LIDAR  # Import the module for the LIDAR
import Suck_it as Suck  # Import Suck it module
#import Thrust
import RPi.GPIO as GPIO
import time

def sample_test():
	GPIO.setwarnings(False)
	sample_counter = 0  # Keeps track of the samples taken. Update after each one is taken
	Relay.relay_init()
#Relay.all_relay_on()

#time.sleep(2)

# System startup - Do checks and initialize
#time.sleep(10)
#Relay.all_relay_off()
#Relay.solenoid_on(22)
#Relay.pump_on()
#time.sleep(3)
#Relay.all_relay_off()
	while sample_counter < 4:  # for testing
    		Suck.suck_it(sample_counter)
    		print('done suckin number #' + str(sample_counter) + ' Sir!')  # for testing purposes
    		sample_counter += 1


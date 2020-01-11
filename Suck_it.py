# Suck it module for the GAUSS USV
# 12/22/2019
# Author: James Stevens

import Relay
import time
import Pumps

pump_control = Pumps.Pump_Control()

in_position = 1  # this needs to come from another header
water_flow = .5  # needs to be from ADC <---------------------------------------------------------------------------------------- Still needs to be written
flushed_flag = 0  # Set to 1 after flush. Flush before each sample.


def suck_it(sample_counter):
    Relay.relay_init()  # Initialize all the GPIO pins
    global flushed_flag  # Give access to global variable
    sample_pin = Relay.get_pin(sample_counter)  # Sample counter. Counts four samples. This needs to come from main loop
    while in_position:  # in_position variable checks location of USV against the target GPS location
        pump_control.init_sample(sample_pin)


def flush():  # Function to flush the system
    global flushed_flag
    Relay.all_relay_off()  # Close all relays
    Relay.pump_on()  # Turn the pump on
    Relay.flush_on()  # Open the flush solenoid
    time.sleep(180)  # Flush for 3 minutes
    Relay.all_relay_off()  # Close all relays, stop the pump and close flush valve
    flushed_flag = 1  # Set flag to 1 so program doesn't flush twice on one sample

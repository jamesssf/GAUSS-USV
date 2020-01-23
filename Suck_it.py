# Suck it module for the GAUSS USV
# 12/22/2019
# Author: James Stevens

import Relay
import time

in_position = 1  # this needs to come from another header <-----------------------------------------------------------------------
water_flow = .5  # needs to be from ADC <---------------------------------------------------------------------------------------- Still needs to be written
flushed_flag = 0  # Set to 1 after flush. Flush before each sample.


def suck_it(sample_counter):
    Relay.relay_init()  # Initialize all the GPIO pins
    global flushed_flag  # Give access to global variable
    sample_pin = Relay.get_pin(sample_counter)  # Sample counter. Counts four samples. This needs to come from main loop
    while in_position:  # in_position variable checks location of USV against the target GPS location
        if flushed_flag:  # If the system is flushed...
            Relay.pump_on()  # Turn the pump on
            Relay.solenoid_on(sample_pin)  # Turn the specific solenoid on given by sample variable
            while ~finished_pump:  # Monitor finished-pump which is updated by the water flow meter
                if water_flow < 1:  # if the water flow drops below 1V <-------------------------------------------------- needs empirical evidence
                    Relay.all_relay_off()  # Turn off all the relays
                    flushed_flag = 0
                    return
        else:
            flush()  # Start the flush


def flush():  # Function to flush the system
    global flushed_flag
    Relay.all_relay_off()  # Close all relays
    Relay.pump_on()  # Turn the pump on
    Relay.flush_on()  # Open the flush solenoid
    time.sleep(180)  # Flush for 3 minutes
    Relay.all_relay_off()  # Close all relays, stop the pump and close flush valve
    flushed_flag = 1  # Set flag to 1 so program doesn't flush twice on one sample

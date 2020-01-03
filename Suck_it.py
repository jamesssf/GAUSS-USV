# Suck it module for the GAUSS USV
# 12/22/2019
# Author: James Stevens

import Relay
import time

in_position = 1 #this needs to come from another header
flushed_flag = 0  # Set to 1 after flush. Flush before each sample.
water_flow = .5 #needs to be from ADC <---------------------------------------------------------------------------------------- Still needs to be written

def suck_it(sample_counter):
    Relay.relay_init()   # Initialize all the GPIO pins
    global flushed_flag
    finished_pump = 0  # Set to 1 only when done, in case interrupt before finish filling sample
    sample_pin = Relay.get_pin(sample_counter)  # Sample counter. Counts four samples. This needs to come from main loop
    while in_position:  # in_position variable checks location of USV against the target GPS location
        if flushed_flag:  # If the system is flushed...
            Relay.pump_on()  # Turn the pump on
            Relay.solenoid_on(sample_pin)  # Turn the specific solenoid on given by sample variable
            while ~finished_pump:  # Monitor finished-pump which is updated by the water flow meter
                if water_flow < 1:  # if the water flow drops below 1V <-------------------------------------------------- needs empirical evidence
                    time.sleep(5)  #delete me. only for testing
                    Relay.all_relay_off()  # Turn off all the relays
                    finished_pump = 1  # Update finished_pump and leave suck_it loop
                    flushed_flag = 0
                    return
        else:
            flush()  # Start the flush


def flush():  # Function to flush the system
    global flushed_flag
    Relay.all_relay_off()  # Close all relays
    Relay.pump_on()  # Turn the pump on
    Relay.flush_on()  # Open the flush solenoid
    time.sleep(5)  # Flush for 3 minutes - time.sleep(180)
    Relay.all_relay_off()  # Close all relays, stop the pump and close flush valve
    flushed_flag = 1  # Set flag to 1 so program doesn't flush twice on one sample

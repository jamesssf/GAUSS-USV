# Pump Class

import RPi.GPIO as GPIO  
import Relay
import time

class Pump_Control:
    
    flo = 0
    last_det = 0
    flushed_flag = 0

    def __init__(self)
        self.last_det = time.time()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Prepare GPIO 24 for rising edge interupt
        GPIO.add_event_detect(24, GPIO.RISING, callback=detect_high, bouncetime=0) # Configure GPIO 24 to activate detect_high on each high voltage in  

    def flush(self, flush_time = 180):  # Function to flush the system: flush_time = amt of time to flush the system in seconds
        Relay.all_relay_off()  # Close all relays
        Relay.pump_on()  # Turn the pump on
        Relay.flush_on()  # Open the flush solenoid
        time.sleep(flush_time)  # Flush for 3 minutes by default
        Relay.all_relay_off()  # Close all relays, stop the pump and close flush valve
        self.flushed_flag = 1  # Set flag to 1 so program doesn't flush twice on one sample
        
    def init_sample(self, pump):
        if ~self.flushed_flag:
            self.flush() # Flush for default time
        else:
            Relay.pump_on()  # Turn the pump on
                Relay.solenoid_on(pump)  # Turn the specific solenoid on given by input variable
                while ~finished_pump:  # Monitor finished-pump which is updated by the water flow meter
                    if self.flo < 1:  # if the water flow drops below 1V <-------------------------------------------------- needs empirical evidence
                        Relay.all_relay_off()  # Turn off all the relays
                        self.flushed_flag = 0
                        return
                    
    def flo_check(self): # Returns the flow rate through the water main
        return flo
        
    def detect_high(self): # Calculates flow rate with every pulse
        f = 1 / (time.time() - self.last_det) # Calculate frequency of pulses with f = 1/T
        last_det = time.time()
        self.flo = f / 420                         # Change 420 to flow rate to frequency conversion rate
        
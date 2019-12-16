def suck_it()

    sample_counter = 0                  # Sample counter. Counts four samples
    flushed_flag = 0                    # Set to 1 after flush. Flush before each sample. reset to 0 when finished_pump = 1
    finished_pump = 0                   # Set to 1 only when done, in case interrupt before finish filling sample

    while in_position:                  # in_position variable checks location of USV against the target GPS location
        if flushed_flag:

        else:
            flush()

def flush():
    global flushed_flag              # Give access to flush function to flushed_flag
    GPIO.out(pinList, HIGH)          # Close all relays
    GPIO.out(pump_pin, LOW)          # Turn the pump on
    GPIO.out(flush_pin, LOW)         # Open the flush solenoid
    time.sleep(180)                  # Flush for 3 minutes
    GPIO.out(pinList, HIGH)          # Close all relays, stop the pump and close flush valve
    flushed_flag = 1                 # Set flag to 1 so program doesn't flush twice on one sample


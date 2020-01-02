# Control module for the GAUSS USV - This is the main code for the USV
# 12/22/2019
# Author: James Stevens

import Relay          # Import the module for the relays
import LIDAR            # Import the module for the LIDAR
import Suck_it as Suck                 # Import Suck it module
import Motor

sample_counter = 0  # Keeps track of the samples taken. Update after each one is taken

# System startup - Do checks and initialize
Relay.relay_init()

Suck.suck_it(sample_counter)
sample_counter += sample_counter


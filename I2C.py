# I2C Module or notes
# 1/2/2020
# Author: James Stevens

#I2C addresses
# Compass 68
# GPS 10
# ADC 48
# PWM 40 & 70
from smbus2 import SMBus
import time
bus = SMBus(1)
address = 0x68
timer = 0;

with SMBus(1) as bus:
    while timer<10:
        zero = bus.read_i2c_block_data(address, 0, 2)
        print(zero)
        one = bus.read_i2c_block_data(address, 1, 2)
        print(one)
        two = bus.read_i2c_block_data(address, 2, 2)
        print(two)
        print(" ")
        x = bus.read_i2c_block_data(address, 3, 2)
        print(x)
        y = bus.read_i2c_block_data(address, 5, 2)
        print(y)
        z = bus.read_i2c_block_data(address, 7, 2)
        print(z)
        print(" ")
        time.sleep(2)
        timer+= 1
        
        if timer == 10:
            print("Done")



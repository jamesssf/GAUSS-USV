# I2C Module or notes
# 1/2/2020
# Author: James Stevens

#I2C addresses
# Compass 68
# GPS 10
# ADC 48
# PWM 40 & 70

import time
from ServoPi import PWM
#!/usr/bin/python

import smbus

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x40      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
#pwm = PWM(0x40)

#pwm.set_pwm_freq(60, 5.5)
#pwm.output_enable()
#pwm.set_pwm(1,0,360)
#pwm.set_pwm(4,0,1200)
#pwm.set_pwm(5,0,1500)
#pwm.set_pwm(8,0,1900)
#time.sleep(8)

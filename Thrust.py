# Motor module for the GAUSS USV
# 12/22/2019
# Author: James Stevens

import RPi.GPIO as GPIO
import time



def motor_init():
    GPIO.setmode(GPIO.BOARD)  # GPIO.BOARD is using the numbers of GPIO)
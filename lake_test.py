import Thrust
import time
from time import sleep
import Control

#This test makes GAUSS drive forward
def test1():
    print("Testing Forward Movement")
    Thrust.ramp(3,1975)
    sleep(5)
    Thrust.stop(3)

#This test makes Gauss turn left and right (not sure about the order)
def test2():
    print("Testing turn")
    Thrust.ramp(0, 1975)
    sleep(8)
    Thrust.stop(0)
    Thrust.ramp(0, 1825)
    sleep(8)
    Thrust.stop(0)

#This test makes GAUSS fill up the sample containers
def test3():
    print("Pump and move forward")
    Control.sample_test()
    test1()

def test4():
	print("Moving Forward and backward and testing turn")
	Thrust.ramp(3, 1950)
	Thrust.ramp(0, 1975)
	sleep(8)
	Thrust.stop(3)
	sleep(5)
	Thrust.ramp(3, 1850)
	Thrust.ramp(0,1825)
	sleep(8)
 	Thrust.stop(3)
def test5():
	Thrust.ramp(3, 1925)
	sleep(3)
	Thrust.ramp(3, 1975)
	sleep(4)
	Thrust.ramp(3, 1950)
	sleep(2)
	Thrust.ramp(3, 1875)
	sleep(6)
	Thrust.ramp(3, 1850)
	sleep(3)
	Thrust.ramp(3, 1825)
	sleep(3)
	Thrust.stop(3)

def test6():
	Thrust.ramp(1,1975)
	sleep(5)
	Thrust.ramp(1,1975)
	sleep(3)
	Thrust.stop(3)
	

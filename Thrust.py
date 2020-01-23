# Motor module for the GAUSS USV
# 12/22/2019
# Author: James Stevens

#1900uS = Full speed
#1500uS = stopped
#1100uS = Full speed reverse

#400uS between stop full speed and reverse

import RPi.GPIO as GPIO
import time
import math
#import Sunfounder_PWM_Servo_Driver
from ServoPi import PWM
#pwm_driver = Sunfounder_PWM_Servo_Driver.PWM()
pwm_driver = PWM(0x40)
pwm_speeds = [1500,1500,1500,1500,1500,1500,1500,1500,1500]

pwm_freq = 0

u_period = 0

def motor_init(freq = 100):
    global pwm_freq
    global pwm_driver
    global u_period
    # Set PWM to 400Hz
    pwm_driver.set_pwm_freq(freq, 5.5)
    pwm_freq = freq
    u_period = 1000000/freq
    for x in range(1,7):
        pwm_driver.set_pwm(x, pwm_convert(1500), pwm_convert(u_period-1500))
    time.sleep(3)

def pwm_convert(x):
    a = int(4096*pwm_freq*float(x)/1000000)
    print(a)
    return a

# Sets the speed in uS, takes a number between 100 and -100
# 100 is full speed forward
# -100 is full speed reverse
def set_speed(speed, channel):
    final = speed * 4 + 1500
    ramp(final, channel)
    
# Slowly ramp down the speed of motors
# Final is the final value desired
# Time is the time in seconds that ramp down will take (default 3)
# step_p_sec is the amount of steps per second, default 20
def ramp(final, channel, on_time=5, step_p_sec=20):
    global pwm_speeds
    global pwm_freq
    global pwm_driver
    global u_period
    # Set the PWM ramp steps
    pwm_int = int(round(float(abs(pwm_speeds[channel] - final))*float(step_p_sec)/float((on_time*1000))))
#    print(str(abs(pwm_speeds[channel]-final)) + "*" + str(step_p_sec) + "/" + str(on_time*1000) + "=" + str(pwm_int))
    # Set the time interval
    time_int = 1000/step_p_sec
    print(time_int)
    # Set the direction of the PWM steps
    if pwm_speeds[channel] > final:
        pwm_int = -pwm_int
    print(pwm_int)
    # Set the update time to 0 so it immediatley updates
    updateTime = 0
    while abs(pwm_speeds[channel] - final) > 10:
        if time.time()*1000 - updateTime >= time_int:
            # Get current PWM value
            next_pwm = pwm_speeds[channel] + pwm_int
            # Get time in milliseconds
            updateTime = time.time()*1000
            # Set pwm value
            pwm_driver.set_pwm(channel, pwm_convert(next_pwm), pwm_convert(u_period-next_pwm))
	    pwm_speeds[channel] = next_pwm
            print(pwm_driver.get_pwm_on_time(1))
            pwm_driver.set_pwm(channel, pwm_convert(final), pwm_convert(u_period - final))

def stop_now(channel):
    pwm_driver.setPWM(channel, 1500, 0)
    pwm[channel] = 0

motor_init()
print("PWM Initialized")
#for i in range(1,8):
#    print(i)
#set_speed(50,1)
#print("Speed set to " + str(50)  + "% of max")
#time.sleep(2)
#set_speed(0,1)
print("Speed back to 0")
i = 1400
while i < 2048:
    pwm_driver.set_pwm(1, i, 4096-i)
    print(i)
    i+=10
    time.sleep(5)

import Adafruit_PCA9685
import time
from time import sleep

pwm = Adafruit_PCA9685.PCA9685()

# Don't change this!!
pwm_freq = 60
pwm.set_pwm_freq(60)

m_speed = [0, 0, 0]

# Convert microseconds to duty cycle
def u_to_duty(u_secs):
    global pwm_freq
    duty = 1000000/pwm_freq
    duty = float(u_secs) / float(duty)
    duty = int(duty * 4096)
    return duty

# Initialize ESCs, optionaly set frequency
def esc_init():
    global pwm_freq
    global pwm
    pwm.set_pwm_freq(pwm_freq)
    for i in range(0, 7):
        set_pulse(i, 1900)
    sleep(5)
    print("ESCs initialized")

# Set the pulse based on microseconds
def set_pulse(channel, u_secs):
    m_speed[channel] = u_secs
    pwm.set_pwm(channel, u_to_duty(u_secs), 4096 - u_to_duty(u_secs))

# Stop motors by channel
def stop(channel):
    if channel == 3:
	for i in range(0,2):
	    set_pulse(i, 0)
	    m_speed[i] = 0
    elif channel < 3 and channel >= 0:
	set_pulse(channel, 0)

# Slowly move between two speeds
def ramp(channel, u_final ):
    inc = 0
    if m_speed[channel] == 0:
	set_pulse(channel, 1900)
    	sleep(3)
    while abs(m_speed[channel] - u_final) > 5:
        if u_final > m_speed[channel]:
	    inc = 1
        else:
            inc = -1
        set_pulse(channel, m_speed[channel] + inc)
        print(m_speed[channel])
        sleep(.01)
    set_pulse(channel, u_final)
    print("Done")

# esc_init()
"""
pwm.set_pwm(1, 65535 - u_to_duty(1700), u_to_duty(1700))
65535 - u_to_duty(time.sleep(5)
pwm.set_pwm(1, 65535 - u_to_duty(1500), u_to_duty(1500))
time.sleep(5)
pwm.set_pwm(1, 65535 - u_to_duty(1350), u_to_duty(1350))
time.sleep(5)
pwm.set_pwm(1, 65535 - u_to_duty(1500), u_to_duty(1500))

"""

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
        set_pulse(0, 0)
	set_pulse(1, 0)
	set_pulse(2, 0)
    elif channel < 3 and channel >= 0:
	set_pulse(channel, 0)

# Slowly move between two speeds
def ramp(channel, u_final):
    inc = 0
    inc1 = 0
    inc2 = 0
    # Channel 3 will activate both rear motors
    if(channel == 3):
	if u_final == 0:
	    stop(1)
	    stop(2)
        set_pulse(1, 0)
	set_pulse(2, 0)
	sleep(.5)
        set_pulse(1, 1900)
	set_pulse(2, 1900)
	sleep(1)
	m2_final = u_final
	m1_final = 1900 - (u_final - 1900)
	m1_done = False
	m2_done = False
        while True:
            if m_speed[2] < m2_final:
	        inc2 = 1
	    else:
	        inc2 = -1
	    if m_speed[1] < m1_final:
	        inc1 = 1
	    else:
                inc1 = -1
	    if m1_done == False:
	        set_pulse(1, m_speed[1] + inc1)
		if abs(m_speed[1] - m1_final) < 10:
		    set_pulse(1, m1_final)
                    print("abs(" + str(m_speed[1]) + "-" + str(m1_final) + ")=" + str(abs(m_speed[1] - m1_final)))
 		    m1_done = True
	    if m2_done == False:
		set_pulse(2, m_speed[2] + inc2)
		print("abs(" + str(m_speed[2]) + "-" + str(m2_final) + ")=" + str(abs(m_speed[2] - m2_final)))
                if abs(m_speed[2] - m2_final) < 10:
                    set_pulse(2, m2_final)
		    m2_done = True
	    sleep(.01)
	    print("M1: " + str(m_speed[1]))
	    print("M2: " + str(m_speed[2]))
	    if m1_done and m2_done:
		break
    else:
	if u_final == 0:
	    stop(channel)
	set_pulse(channel, 0)
        sleep(.5)
        set_pulse(channel, 1900)
	sleep(1.5)
	if channel == 2:
	    u_final = -u_final
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

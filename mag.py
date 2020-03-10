# Nick Purcell - UWT 2020
# Basic magnetometer code
import time
import Adafruit_PCA9685
import board
import busio
import adafruit_lsm9ds1
import math
import csv
import threading

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

pwm = Adafruit_PCA9685.PCA9685()

pwm_freq = 60
pwm.set_pwm_freq(60)


with open('mag_test.csv', mode='w+') as magdata:
    magwriter = csv.writer(magdata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    def spin_servo():
        t = time.time()
        servo(1840)
        while time.time() < t + 1:
            log()
        t = time.time()
        servo(1850)
        while time.time() < t + 1:
            log()
        t = time.time()
        servo(1856)
        while time.time() < t + 1:
            log()
        servo(1850)
    def servo(speed):
        pwm.set_pwm(3, speed, 4096 - speed)
    def get_head():
        try:
            # Read magnetometer.
            mag_x, mag_y, mag_z = sensor.magnetic
            mag_x -= .15
            mag_y -= .3
            # Get angle in Degrees
            head = math.atan2(mag_y, mag_x)*180/math.pi
            head += 175
            if head < -180:
                head = 360 + head
            if head > 180:
                head = head - 360
            return head
        except IOError:
            print("NO MAG")
            return 0
    def loop():
        while True:
            print(get_head())
    def log():
        mag_x, mag_y, mag_z = sensor.magnetic
        mag_x -= .15
        mag_y -= .3
        print(str(mag_x-.15) + " " + str(mag_y-.3))
        magwriter.writerow([mag_x, mag_y])
#    spin_servo()

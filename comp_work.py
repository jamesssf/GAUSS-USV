import smbus2
import time
from smbus2 import SMBus

bus = SMBus(1)
bus.write_byte_data(0x68, 0x6A, 0x20)
time.sleep(1)
bus.write_byte_data(0x68, 0x24, 0x0D)
time.sleep(1)
bus.write_byte_data(0x68, 0x25, 0x8C)
time.sleep(1)
bus.write_byte_data(0x68, 0x26, 0x48)
time.sleep(1)
bus.write_byte_data(0x68, 0x27, 0x81)
time.sleep(.010)
while True:
    for i in range(0, 15):
        bus.write_byte_data(0x68, 0x25, 0x8C)
        bus.write_byte_data(0x68, 0x26, 0x48)
        bus.write_byte_data(0x68, 0x27, 128 + i)
        print(i)
        time.sleep(0.02)
        print(bus.read_byte_data(0x68, 73))

# import motor control script
import Thrust
import threading
import math
# import evdev
from evdev import InputDevice, categorize, ecodes
from time import sleep

# Speed information
speed_forward = 0
speed_reverse = 0
speed_turn = 0

new_speed_turn = False
new_speed_fwd = False
# creates object gamepad
gamepad = InputDevice('/dev/input/event2')
# prints out device info at start
print(gamepad)
# Give it some time to get everything set up
sleep(2)

# Control speed of rover
def speed_control():
    global speed_forward, speed_reverse, speed_turn, new_speed_turn, new_speed_fwd
    while True:
        # Stop if both triggers pressed
        if speed_forward > 0 and speed_reverse > 0:
            Thrust.stop(3)
        else:
            # Saturate speed
            if abs(speed_turn) > 255:
                speed_turn = math.copysign(255, speed_turn)
            # Turn thruster
            if new_speed_turn:
                Thrust.ramp(0, speed_turn + 1900)
                new_speed_turn = False
            # Back Thruster
            if new_speed_fwd:
                Thrust.ramp(3, 1900 + speed_forward - speed_reverse)
                new_speed_fwd = False

t = threading.Thread(name='speed_control', target=speed_control)
t.start()

# Get gamepad input in a loop
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
    # Analog inputs
    if event.type == ecodes.EV_ABS:
        if(event.code == 0):
            speed_new = (event.value - 128) * 2
            # Dead zone
            if abs(speed_new) < 30:
                speed_new = 0
            # Saturate speed_turn
            if abs(speed_new) > 255:
                speed_new = math.copysign(255, speed_new)
            if speed_new != speed_turn:
                speed_turn = speed_new
                new_speed_turn = True
        # Get forward and reverse speed from triggers
        if event.code == 5:
            print(event.value)
            speed_forward = event.value
            new_speed_fwd = True
        if event.code == 2:
            print(event.value)
            speed_reverse = event.value
            new_speed_fwd = True 

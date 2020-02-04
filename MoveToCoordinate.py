#James Cathey
#Gauss USV 2020
#This module uses the thrusters, compass and GAUSS' GPS Coordinates as well as a goal GPS goal coordinates
#to navigate within a small radius of the goal location.

import DistancetoGoal as Dist
import Thrust
from time import sleep
TargetRadius = 10                       #Target radius in meters for the moving to end.
#state = 0                               #state = 0: All thrusters off
#state = 1                              #state = 1: Rear thrusters thrusting forward
#state = 2                              #state = 2: Rear thrusters thrusting forward and front thruster turning GAUSS right
#state = 3                              #state = 3: Rear thrusters thrusting forward and front thruster turning GAUSS left
#state = 4                              #state = 4: Rear thrusters off and front thruster is turning GAUSS right
#state = 5                              #state = 5: Rear thrusters off and front thruster is turning GAUSS left
#state = 6
def MoveToCoordinate(targetLat, targetLong):
    gaussLat = GPS.SomeFunction()
    gaussLong = GPS.someFunction()
    gaussHead = Compass.getHead()
    goalHead = Dist.getGoalHeading(gaussLat, gaussLong, targetLat, targetLong)
    headDiff = gaussHead - goalHead             #If this value is negative, Gauss needs to turn RIGHT
    while Dist.getGoalDistance(gaussLat, gaussLong, targetLat, targetLong) > TargetRadius:
        if abs(headDiff) < 5:
            state = 1
        elif abs(headDiff) < 20:
            if headDiff < 0:
                state = 2
            else:
                state = 3
        else:
            if headDiff < 0:
                state = 4
            else:
                state = 5
        if state == 0:
            Thrust.stop(3)
        elif state == 1:
            Thrust.ramp(3, Thrust.speed[2], 2100)       ##modified version of ramp where we ramp from current speed to desired speed
        elif state == 2:
            Thrust.ramp(3, Thrust.speed[2], 2100)
            Thrust.ramp(0, Thrust.speed[0], 2100)
        elif state == 3:
            Thrust.ramp(3, Thrust.speed[2], 2100)
            Thrust.ramp(0, Thrust.speed[0], 1700)
        elif state == 4:
            Thrust.stop(2)
            Thrust.stop(1)
            Thrust.ramp(0, Thrust.speed[0], 2100)
        else:
            Thrust.stop(2)
            Thrust.stop(1)
            Thrust.ramp(0, Thrust.speed[0], 1700)
    Thrust.stop(3)
    print("I have reached the goal sire")

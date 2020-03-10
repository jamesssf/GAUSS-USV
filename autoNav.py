#James Cathey
#Gauss USV 2020
#This module uses the thrusters, compass and GAUSS' GPS Coordinates as well as a goal GPS goal coordinates
#to navigate within a small radius of the goal location.

import DistancetoGoal as Dist
import Thrust
import GPStest as gps
from time import sleep
TargetRadius = 10                       #Target radius in meters for the moving to end.

#Must Initialize GPS in test module**
def autoNav(targetLat, targetLong):
    while True:
        latLong = gps.GPSrun()
        gaussLat = latLong[0]
        gaussLong = latLong[1]
       #### gaussHead = Compass.getHead() Still need to finish this up...
        goalHead = Dist.getGoalHeading(gaussLat, gaussLong, targetLat, targetLong)
        distError = Dist.getGoalDistance(gaussLat, gaussLong, targetLat, targetLong)
        headError = gaussHead - goalHead             #If this value is negative, Gauss needs to turn RIGHT
        if(distError < TargetRadius):
            break
	print("Distance to goal: "+distError+" Meters")
	print("Goal Heading: "+goalHead+" deg")
	print("Gauss Heading: "+gaussHead+"deg")
	print("Heading Error: "+headError+"deg")
        #Autonav algorithm
        #
        #
        #
    Thrust.stop(3)
    print("I have reached the goal sire")

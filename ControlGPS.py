#James Cathey
#Gauss USV 2020

#This file is a test of  the GPS functionality for GAUSS as well as test the distance 
#function and in radius function
import GPIS

import DistancetoGoal as goal
from micropyGPS import MicropyGPS
from time import sleep
from time import time

initialtargetRadius = 20		#first target radius in meters
secondarytargetRadius = 100		#second target radius in meters
goalLat = .001			#target latitude 
goalLong = .001			#target logitude



file = open("GPS_log2.txt","w")

myI2CGPS = GPIS.I2CGPS()

print("GTOP Read Example")

myI2CGPS.begin()

x = 0

loc = " "

gps = MicropyGPS(8, "dd")

lat = 0
lon = 0

def userConfig():
        print("Type 0 to skip configuration")
        intin = input("PTMK Number: ")
        intin = int(intin)
        if intin == 0:
                return
        din = raw_input("PTMK Datastream: ")
        writeToGPS(intin, din)
        print("Press 0 to enter another input, 1 to continue")
        intint = input("Input: ")
        if int(intin) == 0:
                userConfig()


def writeToGPS(PMTK, datastream):
        configString = myI2CGPS.createMTKpacket(PMTK, datastream)
        print("Config String: " + configString)
        myI2CGPS.sendMTKpacket(configString)
        sleep(1)

# Initialize by setting to $GPGLL
print("Initializing TITAN X1\n\nSetting NMEA to GPS")
writeToGPS(353, ",1,0,0,0,0")
print("Setting NMEA to RMC")
writeToGPS(314, ",1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# userConfig()



startTime = time()
for i in range(400):
	while myI2CGPS.available() != 0:
                incoming = myI2CGPS.read()
                if (incoming == 36):
                        break
                loc += chr(incoming)
	locs = loc.splitlines()
	for y in locs:
		if(len(y) > 1):
	                if y[0] == " ":
	                        y= y[1:]
	                y = "$" +y
#			print(y)
			file.write(str(y) + "\n")
	                for x in y:
	                        gps.update(x)
        if time() > startTime + 1:
	       print(gps.date)
	       print(gps.timestamp)
	       print(gps.latitude[0])
	       print(gps.longitude[0])
	       distance = goal.getGoalDistance( gps.latitude[0], gps.longitude[0], goalLat, goalLong)
               print("Distance to goal", distance)
	       print("In pump radius? ", goal.inRadius(distance, initialtargetRadius))
               print("Is GPS point valid?",gps.valid)
               print("Goal heading is", goal.getGoalHeading(gps.latitude[0], gps.longitude[0], goalLat, goalLong))
               startTime = time()



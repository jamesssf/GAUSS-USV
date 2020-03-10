#James Cathey
#Gauss USV 2020
#1/30/2020

#This file will test the autonomous capabilities of GAUSS as well as the pumping of water at various coordinates
#This requires a valid KML file and valid "PumpLocations.txt" file  in the same directory to operate

import MoveToCoordinate as Movement
from time import sleep
import GaussFileTranslator as Translate
import Suck_it as Suck
import GPStest as gps
#names of the files used for storing path to follow and pump locations

pumpFile = "PumpLocations.txt"
waypointFile = "GaussTest.kml"
def autonomousTest():
    gps.GPSinit()			#initialize the GPS
    coordArray = Translate.dataTranslator(waypointFile, pumpFile)        ##Need to upload file from PI
    p = 0
    i = 0
    sampleCount = 0
    while i + 3 <= (len(coordArray)):
        targetLat = coordArray[i]
        targetLong = coordArray[i+1]
        pumpWater = coordArray[i+2]
        print(targetLat)
        print(targetLong)
	#autoNav.autona
        Movement.Move(targetLat, targetLong)	##only need to add compass
	#auto.autoNav(targetLat, targetLong)
        if pumpWater:
            Suck.suck_it(p)
            p +=1;
        i+=3

    print("That's one small step for man..... One, giant leap for mankind")

autonomousTest()

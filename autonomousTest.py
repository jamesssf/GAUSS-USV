#James Cathey
#Gauss USV 2020
#1/30/2020

#This file will test the autonomous capabilities of GAUSS as well as the pumping of water at various coordinates
#This requires a valid KML file and valid "PumpLocations.txt" file  in the same directory to operate.

from MoveToCoordinate import MoveToCoordinate
from time import sleep
import GaussFileTranslator as Translate
import Suck_it as Suck

def autonomousTest():
    coordArray = Translate.DoYourThang()        ##Need to upload file from PI
    i = 0
    sampleCount = 0
    while i + 3 <= (len(coordArray)):
        targetLat = coordArray[i]
        targetLong = coordArray[i+1]
        pumpWater = coordArray[i+2]
        MoveToCoordinate(targetLat, targetLong)
        if pumpWater:
            Suck.suck_it(p)
            p +=1;
        i+=3
    print("Assuming direct control :D")
    print("That's one small step for man..... One, giant leap for mankind")
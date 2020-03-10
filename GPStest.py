import GPIS

from micropyGPS import MicropyGPS

from time import sleep
from time import time

file = open("gps_log.csv","w")

myI2CGPS = GPIS.I2CGPS()

print("GTOP Read Example")

myI2CGPS.begin()

x = 0

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
def GPSinit():
    # Initialize by setting to $GPGLL
    print("Initializing TITAN X1\n\nSetting NMEA to GPS")
    writeToGPS(353, ",1,0,0,0,0")
    print("Setting NMEA to RMC")
    writeToGPS(314, ",0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
def GPSrun(scans = 1):
    try:
        latLong = [0,0]
        loc =" "
        i = 0
        lat = []			#stores
        long = []
        while i < scans:
            print(i)
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
    #				print(y)
    #                    print(y)
                    for x in y:
                        gps.update(x)
            #print(gps.valid)
            #print(gps.latitude)
           #print(gps.longitude)
            if(gps.valid == True):					#only takes GPS values if GPS coord is valid
                lat.append(float(gps.latitude[0]))
                long.append(float(gps.longitude[0]))
                if gps.longitude[1] =='W':
                    long[i] *= -1
                i += 1
            else:
           #     print("NO GPS")
           #     print(gps.latitude)
                continue

            lat.sort()				#sorted latitude
            long.sort()				#sorted longitude
            latLong[0] = lat[i//2]
            latLong[1] = long[i//2]
            #print(lat)
            #print(long)
            #print(latLong)
    
        file.write(str(latLong[0]) + "," + str(latLong[1]) + "," + str(time()) + "\n")
        return latLong

    except IOError:
        print("NO GPS")
        return {0,0}


GPSinit()

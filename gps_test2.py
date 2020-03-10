import GPIS

from micropyGPS import MicropyGPS

from time import sleep
from time import time

file = open("GPS_log2.txt","w")

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
    writeToGPS(314, ",1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
def GPSrun():
    latLong = [0,0]
    loc =" "
    i = 0
    lat = []			#stores
    long = []
    while i < 11:
        while myI2CGPS.available() != 0:
            incoming = myI2CGPS.read()
            #if (incoming == 36):
             #    break
            loc += chr(incoming)
            locs = loc.splitlines()
            for y in locs:
                if(len(y) > 1):
                    if y[0] == " ":
                        y= y[1:]
                        y = "$" +y
#				print(y)
                        file.write(str(y) + "\n")
                        for x in y:
                            gps.update(x)
        if(gps.valid == True):					#only takes GPS values if GPS coord is valid
            i +=1
            print(gps.latitude[0])
            lat.append(gps.latitude[0])
            if gps.longitude[1] == 'W':
                long.append((-1)*gps.longitude[0])
            else:
                long.append(gps.longitude[0])
                print(gps.longitude)
                print(gps.latitude)

        print(lat)
        print(long)
        latLong[0] = lat
        latLong[1] = long
#        Slat = lat #.sort()				#sorted latitude
 #       Slong = long #.sort()				#sorted longitude
 #       print(Slat)
 #       print(Slong)
 #       latLong[0] = Slat[5]		#takes the median of latitude
 #       latLong[1] = Slong[5]		#takes the median of longitude
#        print(Slat)
#        print(Slong)
#        print(latLong)
        return latLong
GPSinit()
while True:
    GPSrun()

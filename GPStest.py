import GPIS

from micropyGPS import MicropyGPS

from time import sleep

myI2CGPS = GPIS.I2CGPS()

print("GTOP Read Example")

myI2CGPS.begin()

x = 0

loc = " "

my_gps = MicropyGPS()


def writeToGPS():
        print("Type 0 to skip configuration")
        intin = input("PTMK Number: ")
        intin = int(intin)
        if intin == 0:
                return
        din = raw_input("PTMK Datastream: ")
        configString = myI2CGPS.createMTKpacket(intin, din)
        print(configString);
        myI2CGPS.sendMTKpacket(configString)
        sleep(1)
        print("Press 0 to enter another input, 1 to continue")
        intint = input("Input: ")
        if int(intin) == 0:
                writeToGPS()

writeToGPS()



while True:

        while myI2CGPS.available() != 0:
                incoming = myI2CGPS.read()
                if (incoming == 36):
                        break
                loc += chr(incoming)
        locs = loc.splitlines()
        for y in locs:
                if y[0] == " ":
                        y= y[1:]
                y = "$" +y
                print(y)
                for x in y:
                        my_gps.update(x)
                print(my_gps.latitude)
                print(my_gps.longitude)
        sleep(1)

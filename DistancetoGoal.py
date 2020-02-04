##James Cathey 2020##
##Gauss_USV##
#Movement.py
#Start of a file to do some movement and distance calculations for GAUSS


import math as Math
from time import sleep

#SmallTargetRadius = 15		#target radius sizes in meters
#LargeTargetRadius = 100



def getGoalDistance(gLat,gLong,targetLat,targetLong):
    R = 6378.137 # Radius of earth in KM
    dLat = targetLat * Math.pi / 180 - gLat * Math.pi / 180
    dLon = targetLong * Math.pi / 180 - gLong * Math.pi / 180
    a = Math.sin(dLat/2) * Math.sin(dLat/2) +  Math.cos(gLat * Math.pi / 180) * Math.cos(targetLat * Math.pi / 180) *  Math.sin(dLon/2) * Math.sin(dLon/2)
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
    d = R * c
    distance = d*1000			#distance from target to Gauss in meters
    return distance


def inRadius(dist, targetRadius):
	if dist < targetRadius:
		return True
	else :
		return False

def getGoalHeading(gaussLat, gaussLong, targetLat, targetLong):
	X = Math.cos(targetLat) * Math.sin(targetLong-gaussLong)
	Y = Math.cos(gaussLat)*Math.sin(targetLat) - Math.sin(gaussLat) * Math.cos(targetLat)*Math.cos(targetLong-gaussLong)
	radHeading = Math.atan2(X,Y)
	goalDegrees = radHeading*180/Math.pi
	return goalDegrees

##Testing  functions

dist = getGoalDistance(47.262114, -122.438085, 47.262118, -122.437940)
print('Distance from  goal = ', dist , 'Meters');

done = inRadius(dist, 30);
print('Gauss is in  the radius', done)


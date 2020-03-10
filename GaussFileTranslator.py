#James Cathey
#Gauss USV
#1/24/2020

#This program translates information obtained from the .kml and .txt files uploaded by the user
import GaussFileReader as readStuff

def dataTranslator(CoordinateFile, WaypointFile):
	Coordinate_Array = readStuff.ReadKML(CoordinateFile)
	PumpWaypointArray = readStuff.ReadTXT(WaypointFile)
	NumWaypoints =int( len(Coordinate_Array)/2)
	Final_Array = []
	print(NumWaypoints)
	j = 0
	for i in range(NumWaypoints):
		Flag = False
		Final_Array.append(Coordinate_Array[i+1])		#Sets the longitude second in the sequence of 3
		Final_Array.append(Coordinate_Array[i])			#Sets the latitude first i the sequence of 3
		#If else block sets the third element in the array to pump or not

		for j in range(4):
			if PumpWaypointArray[j+1] == i:
				Flag = True
		Final_Array.append(Flag)
	return Final_Array
#For testing purposes
#print(dataTranslator())

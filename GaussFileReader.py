#James Cathey
#Gauss USV
#1/24/202

#ReadFromKML can read the data from a KML file obtained by plotting a course on google earth.
#If you create a path in Google Earth with any number of points, this program will collect the lat/long along the path and put them in an array.
#This will be used to plot our courses and get a CSV containing inteded travel points.
#As long as the path is written out in the correct order, Gauss should be able to navigate the coordinates.

##***Still need to verify this is the best solution***

def ReadKML(fileDirectory):
    File_object = open(fileDirectory, "r")                         #KML file from google earth directory
    line =  File_object.readline()                                  #grabs the first line in the KML file
    for line in File_object:
        if line.__contains__('<LineString>'):                       #searches for '<LineString>' in the KML file from google earth
            line = File_object.readline()			    #Skips the the <Coordinates> line
            line = File_object.readline()			    #This line contains all the coordinates
            i = 0
            coordinates = []
            line = line +'~'
            r = 0
            p = len(line)
            line= line +'~'
            while True:
                while line[i] != ',':
                    if line[i] == '~':
                        break
                    elif line[i] != '\t':
                        coordinates.append(line[i])
                        i += 1
                    else:
                        i+=1
                if line[i] == '~':
                    break
                i+=1
                r+=1
                if r%2 == 0:
                    coordinates.append('*')     #Appends a star between the relevant data (long) and irrelevant data (altitude)
                else:
                    coordinates.append('$')     #Appends a money sign between the relevant data (lat and long)
                if line[i] == '~':
                    break
            pp = []        		        #PP will store the comma separated list of lat and long
            rr = ''
            for a in  range(len(coordinates)):
                    if coordinates[a] == '$':
                        pp.append(float(rr))
                        rr = ''
                    elif coordinates[a] == '*':
                        pp.append(float(rr))
                        rr = ''
                    elif coordinates[a] == ' ':
                        rr = ''

                    else:
                        rr = rr + coordinates[a]
    return pp


#Reads the  file for pumping locations
def ReadTXT(FileDirectory):
	pumpLoc = open(FileDirectory, 'r')
	Locations = []
	i = 0
	for j in range(5):
		Lines = pumpLoc.readline()
		Lines = pumpLoc.readline()
		Locations.append(int(Lines))
		i = i+1
	return Locations




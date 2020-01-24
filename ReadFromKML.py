#James Cathey
#Gauss USV
#1/24/202

#ReadFromKML can read the data from a KML file obtained by plotting a course on google earth.
#If you create a path in Google Earth with any number of points, this program will collect the lat/long along the path and put them in an array.
#This will be used to plot our courses and get a CSV containing inteded travel points.
#As long as the path is written out in the correct order, Gauss should be able to navigate the coordinates.

##***Still Need to remove the altitude coordinate from the data (in meters)*** ******DONE*********
##***Still need to turn this into a CSV file or something we can read
##***Still need to verify this is the best solution.
#import csv
def ReadFromKML(fileDirectory):
    #eventually to store coordinates as CSV? Unsure how to do that with my array of characters.... Or at least, i don't really want to right now
    #with open('Coords.csv', newline='') as csvfile:
    #coord = csv.writer(csvfile, delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    File_object = open(fileDirectory , "r")                     #KML file from google earth directory
    line =  File_object.readline()                                  #grabs the first line in the KML file
    for line in File_object:
 #       if line.__contains__(<range>)              #Can also use a range inside the KML file to see how long GAUSS' journey would be.
 #           for k in range len(line):
 #               if type(line[i] == "int")
 #                   range
        if line.__contains__('<LineString>'):                       #searches for '<LineString>' in the KML file from google earth
            line = File_object.readline()
            line = File_object.readline()
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
            pp = []         #PP will store the comma separated list of lat and long
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
            
            print(pp)
            print(type(pp[0]))
ReadFromKML("D:\\UntitledProject.kml")
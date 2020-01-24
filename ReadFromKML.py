#James Cathey
#Gauss USV
#1/24/202

#ReadFromKML can read the data from a KML file obtained by plotting a course on google earth.
#This will be used to plot our courses and get a CSV containing inteded travel points.
#As long as the path is written out in the correct order, Gauss should be able to navigate the coordinates.

##***Still Need to remove the altitude coordinate from the data (in meters)***
##***Still need to turn this into a CSV file or something we can read
##***Still need to verify this is the best solution.


#import csv

def ReadFromKML(fileDirectory):
    #eventually to store coordinates as CSV? Unsure how to do that with my array of characters.... Or at least, i don't really want to right now
    #with open('Coords.csv', newline='') as csvfile:
    #coord = csv.writer(csvfile, delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    File_object = open(fileDirectory,"r")                     #KML file from google earth directory
    line =  File_object.readline()                                  #grabs the first line in the KML file
    for line in File_object:
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
                    coordinates.append('*')
                else:
                    coordinates.append('$')
                if line[i] == '~':
                    break

            print(coordinates)

ReadFromKML("D:\Gauss try.kml")
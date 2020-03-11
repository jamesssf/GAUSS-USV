# Nick Purcell - UW Tacoma - 2020
# Basic PID Controller
# Will travel along a path of GPS coordinates
import math
import time
#import Thrust
#import GPStest
#import mag
import csv
import datetime

# Slope and intercept of trajectory line (eg y = s(x) + i)
trajectory_slope = 0
trajectory_intercept = 0

# Starting time
s_time = time.time()
time_struct = datetime.datetime.now().timetuple()

# Initial Point in trajectory
position_start = [0,0]
 
# Hold onto the current goal in the waypoint list, start at -1 so it goes to zero at first increment
waypoint_counter = -1
 
# True when it is time to move to the next waypoint, start true to find the first waypoint as soon as loop starts
next_waypoint = True
 
# List of waypoints
waypoints = [[47.19402,-122.4573],[47.194606, -122.455653]]
 
# Control variables
distance_gain = 100
max_speed = 90
max_turn_speed = 150
gain_trajectory = 30
gain_trajectory_derivative = 0
 
goal_radius = 5
 
# Hold last error and time for derivative and integral control
error_trajectory_last = 0
time_last = 0
 
gps = [0, 0]
get_head = 0
 
# Find the trajectory by using input position_now
# And the position_goal as the ending position.
# Position vectors ([0] - lat) ([1] - lon)
def set_trajectory(position_now, position_goal):
    global trajectory_intercept, trajectory_slope, position_start
    position_start = list.copy(position_now)
    trajectory_slope = (position_goal[0] - position_now[0])/(position_goal[1] - position_now[1])  # Rise over run
    trajectory_intercept = position_now[0] - position_now[1] * trajectory_slope  # y = sx + i -> i = y - sx
   
def point_degree_to_rad(P):
    Q = [0, 0]
    Q[0] = P[0]*math.pi/180
    Q[1] = P[1]*math.pi/180
    return Q
   
def run_loop(debug = False):
    global gps, get_head, waypoints
    # Convert waypoints from Degree to Radians
    while waypoint_counter < len(waypoints):
        if debug == True:
            gps[0] = float(input("Enter Latitude: "))
            gps[1] = float(input("Enter Longitude: "))
            get_head = float(input("Heading: "))
            control_loop(debug)
 #           if time.time() > s_time + 120:
 #               Thrust.stop(3)
 #               return
 
 
# Find Distance between two coordinates
def get_dist_coords(a, b):
    # Convert a and b from radians to degrees
    a = point_degree_to_rad(a)
    b = point_degree_to_rad(b)
    return 6371000*math.sqrt((a[0] - b[0])**2 + math.cos(a[0])*math.cos(b[0])*(a[1]-b[1])**2)
 
# PID Control Loop
def control_loop(debug):
    global waypoint_counter, trajectory_slope, trajectory_intercept, next_waypoint, gps
    #position_now = GPStest.GPSrun()  # REPLACE WITH CODE TO GET THE CURRENT POSITION/HEADING
    #heading = mag.get_head()     # Must be -180 < H < 180
    position_now = list.copy(gps)
    heading = get_head
    position_goal = [0,0]
    # Increment waypoint counter and find new trajectory if time to move to next waypoint
    if next_waypoint:
        waypoint_counter += 1
        position_goal = waypoints[waypoint_counter]
        set_trajectory(position_now, position_goal)
        next_waypoint = False
    else:
        position_goal = waypoints[waypoint_counter]
    # Calculate goal heading relative to the position of the Rover
    goal_heading = math.atan2(position_goal[1] - position_now[1],
                              position_goal[0] - position_now[0])
 
    # Calculate the error in terms of position (Slows down rover as it closes in on goal)
    distance_error = get_dist_coords(position_now, position_goal)

   # Move on to the next goal if the distance is smaller than the goal distance
    if distance_error < goal_radius:
        next_waypoint = True
 
    # Multiply distance error by distance gain (Distance gain is purely proportional)
    speed = distance_error * distance_gain
 
    # Saturate this error based on the maximum speed of the rover
    if abs(speed) > max_speed:
        speed = math.copysign(max_speed, speed)
 
    # Find the distance between rover and trajectory (+ if traj is to the right of rover, - if traj is left of rover)
    closest_point = [0, 0]
    # Find the closest point on the line (in terms of longitude) (x' = (x+m(y-b))/(1+m^2)
    closest_point[1] = ((position_now[1]
                         + trajectory_slope * (position_now[0] - trajectory_intercept))
                        / (1 + trajectory_slope**2))
    # Limit the closest point on the line to a point between the goal position and the starting position
    if ((closest_point[1] < position_start[1] < position_goal[1]) or
            (closest_point[1] > position_start[1] > position_goal[1])):
        closest_point[1] = position_start[1]
    elif ((closest_point[1] > position_goal[1] > position_start[1]) or
            (closest_point[1] < position_start[1] < position_goal[1])):
        closest_point[1] = position_start[1]
    # Plug longitude into trajectory equation
    closest_point[0] = closest_point[1] * trajectory_slope + trajectory_intercept
    # Find the trajectory error by finding the distance between the current position and the closest trajectory point
    error_trajectory = get_dist_coords(closest_point, position_now)
    # Set error negative if the rover must turn left to return to the trajectory
    if((trajectory_slope < 0 and (position_now[0] - closest_point[0] > 0) == (position_goal[0] - position_start[0] > 0)) or
       (trajectory_slope > 0 and (position_now[0] - closest_point[0] > 0) != (position_goal[0] - position_start[0] > 0))):
        error_trajectory *= -1
 
    # Save time of error measurement for derivative and integral control
    time_now = time.time()
 
    # Find the instantaneous derivative of the trajectory error
    derivative_error_trajectory = (error_trajectory - error_trajectory_last) / (time_now - time_last)
 
    # Calculate proportional term
    proportional_control = error_trajectory * gain_trajectory
    # Calculate Derivative Term
    derivative_control = derivative_error_trajectory * gain_trajectory_derivative
    # Calculate turn speed
    turn_speed = (proportional_control)
 
    # Saturate turn speed
    if abs(turn_speed) > max_turn_speed:
        turn_speed = math.copysign(max_turn_speed, turn_speed)
#    speed = speed - abs(turn_speed)
#    if speed < 0:
#        speed = 0

    if debug:
        print("Latitude: " + str(position_now[0]) + " Longitude: " + str(position_now[1]))
        print("Goal Latitude: " + str(position_goal[0]) + " Goal Longitude: " + str(position_goal[1]))
        print("Distance to Goal: " + str(distance_error) + " Heading: " + str(heading) + " Goal Heading: " + str(goal_heading))
        print("Starting Latitude: " + str(position_start[0]) + " Starting Longitude " + str(position_start[1]))
        print("Trajectory Error: " + str(error_trajectory))
        print("Turn Speed: " + str(turn_speed) + " Forward Speed: " + str(speed))
        print("Trajectory Intercept: " + str(trajectory_intercept) + " Trajectory Slope: " + str(trajectory_slope))
        print("Trajectory Latitude: " + str(closest_point[0]) + " Trajectory Longitude: " + str(closest_point[1]))
    with open("GAUSS_Log_" + str(time_struct[1]) + "_" + str(time_struct[2]) + "_" + str(time_struct[0]) + "_" + str(time_struct[3]) + ":" + str(time_struct[4]) + ".csv", mode='w+') as gpsdata:
        gpswriter = csv.writer(gpsdata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        gpswriter.writerow([position_now[0], position_now[1], position_start[0], position_start[1],position_goal[0],position_goal[1],error_trajectory, heading])

    # Set the speed of front thruster based on the turn speed
    #Thrust.ramp(0, turn_speed + 1900)
    # Set the speed of the rear thruster based on the turn speed
    #Thrust.ramp(3, speed + 1900)
    #Thrust.set_speed(turn_speed + 1900, speed + 1900, speed_1900)
    #Thrust.set_speed(turn_speed + 1900, speed + 1900, speed_1900)
    time.sleep(.01)

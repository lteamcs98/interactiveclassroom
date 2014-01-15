# robot_dance.py
# CS 1 class example by THC based on code by Devin Balkcom.
# The robot does a little dance.

from robotsim import *

def robot_dance():
    place_robot(200, 200, 0)    # put the robot on the floor
    
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    right()                     # turn right 90 degrees
    
    stop()                      # done dancing
        
start_simulator(robot_dance)
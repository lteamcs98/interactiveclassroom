# one_square.py
# CS 1 class example by THC based on code by Devin Balkcom.
# The robot moves in a square.

from robotsim import *

def make_square():
    place_robot(200, 200, 0)    # put the robot on the floor
    
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    
    stop()                      # done dancing
        
start_simulator(make_square)
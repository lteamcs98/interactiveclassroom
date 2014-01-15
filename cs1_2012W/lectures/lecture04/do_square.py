# do_square.py
# CS 1 class example by THC based on code by Devin Balkcom.
# The robot moves in a square forever.

from robotsim import *

def do_square():
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees
    straight()                  # go straight a few feet
    left()                      # turn left 90 degrees

def make_square():
    place_robot(200, 200, 0)    # put the robot on the floor
    
    while True:
        do_square()
         
start_simulator(make_square)
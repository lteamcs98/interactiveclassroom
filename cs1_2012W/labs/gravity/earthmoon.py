# earthmoon.py
# Example for CS 1 Lab Assignment 2.
# Original solution by Aaron Watanabe, July 2011
#  Updated by Devin Balkcom, October 2011
#  Further modifications by THC, January 2012.

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # how many real seconds for each second of simulation
PIXELS_PER_METER = 3 / 1e7  # distance scale for the simulation

FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

def main():
    earth = Body(5.9736e24, 0, 0, 0, 0, 24, 0, 0, 1)            # blue earth
    moon = Body(7.3477e22, 3.84403e8, 0, 0, 1022, 4, 1, 1, 1)   # white moon
    earth_moon = System([earth, moon])
    
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    while not window_closed(): 
        clear()
        
        # Draw the system in its current state.
        earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    
        # Update the system for its next state.
        earth_moon.update(TIMESTEP * TIME_SCALE)
    
        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Earth-moon simulation", WINDOW_WIDTH, WINDOW_HEIGHT)

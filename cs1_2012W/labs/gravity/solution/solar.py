# solar.py
# Solution for CS 1 Lab Assignment 2.
# Original solution by Aaron Watanabe, July 2011
#  Updated by Devin Balkcom, October 2011
#  Further modifications by THC, January 2012.

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

AU = 1.49598e11 # number of meters per astronomical unit
EM = 5.9736e24  # mass of the Earth in kilograms

TIME_SCALE = 3.0e6              # how many real seconds for each second of simulation
PIXELS_PER_METER = 120. / AU    # distance scale for the simulation

FRAME_RATE = 30
TIMESTEP = 1.0 / FRAME_RATE     # time between drawing each frame

def main():
    # Solar system data comes from
    #   http://hyperphysics.phy-astr.gsu.edu/hbase/solar/soldata2.html
    sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
    mercury = Body(.06 * EM, -.3871 * AU, 0, 0, 47890, 3, 1, .4, 0)
    venus = Body(.82 * EM, -.7233 * AU, 0, 0, 35040, 6, 0, .6, .2)
    earth = Body(1.0 * EM, -1.0 * AU, 0, 0, 29790, 7, 0, .4, 1)
    mars = Body(.11 * EM, -1.524 * AU, 0, 0, 24140, 4, .8, .2, 0)
    
    solar_system = System([sun, mercury, venus, earth, mars])

    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()
    
    while not window_closed():
        clear()

        # Draw the system in its current state.   
        solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # Update the system for its next state.
        solar_system.update(TIMESTEP * TIME_SCALE)

        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Solar system simulation", WINDOW_WIDTH, WINDOW_HEIGHT)


# ball_example3.py
# Devin Balkcom
# August 2011
# Modified by THC.

from random import uniform
from cs1lib import *
from ball import Ball

# Scaling used for drawing the ball and computing
# the position (in meters) of the mouse click.
PIXELS_PER_METER = 10

FRAME_RATE = 40
TIMESTEP = 1.0 / FRAME_RATE

# Remove any ball that is off the screen from the list.
# We loop over the list in reverse, because when an item is removed from the list,
# all of the items after the item have their location in the list reduced by one.
# By looping in reverse, we make sure that the next index the loop looks at
# is the correct one.
    
def remove_offscreen(blist):
    i = len(blist) - 1
    while i >= 0:
        if blist[i].y < 2:
            del blist[i]
        i -= 1
    
def main():
    ball_list = []

    enable_smoothing()
    set_clear_color(0, 0, 0)

    while not window_closed():
        clear()
        
        # Draw every ball in the list.
        for ball in ball_list:
            ball.draw(PIXELS_PER_METER)
            
        # If the mouse button has been pressed, add a new ball.
        if mouse_down():    
            r = uniform(.5, 1)
            g = uniform(.5, 1)
            b = uniform(.5, 1)
            
            new_ball = Ball(mouse_x() / PIXELS_PER_METER,
                            mouse_y() / PIXELS_PER_METER,
                            0, 0,
                            r, g, b)
            ball_list.append(new_ball)
    
        # Delete any ball from the list that has fallen off the screen.
        remove_offscreen(ball_list)
    
        # Update the state of every ball in the list.
        for ball in ball_list:
            ball.animate_step(TIMESTEP)
            
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, flipped_y = True)

# growing_circle.py
# CS 1 example by Devin Balkcom to animate a circle that grows to fill the window.

from cs1lib import *
from time import sleep

def animate_circle():
    # initial setup can be done just once
    enable_smoothing()
    set_fill_color(1, 0, 0)    

    # Set a variable that will keep information about the current
    # state of the circle.  As this variable changes values in
    # the loop, the way the circle will be drawn will change in each
    # frame.
    radius = 1

    while radius < 200 and not window_closed():
        # draw the current frame
        #    (drawing is hidden, and will not
        #    actually appear on screen until requested later)
        
        clear()
        draw_circle(200, 200, radius)

        # tell the graphics library to actually display the frame
        request_redraw()

        # wait .02 seconds on this frame of the animation, so
        #  the person watching the animation can see it before we
        #  move to the next frame.
        sleep(.02)

        # change the state for the next frame
        radius = radius + 1 
    
start_graphics(animate_circle)
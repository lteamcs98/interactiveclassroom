#  Draw random pastel circles on the screen. 
#  Based on an example by Fabio Pellacini
#  Python version by Devin Balkcom, Feb 2011

from cs1lib import *
from random import uniform, randint

def random_circles():
    
    # Clear the screen and set the pen color to black before we start
    # the animation loop.  These functions will only be called once.
    
    clear()
    set_stroke_color(0, 0, 0)

    enable_smoothing()

    while not window_closed():

        # fade-out effect
        set_fill_color(1, 1, 1, .05)  # white, with opacity .05
        draw_rectangle(0, 0, 400, 400) # draw a semi-transparent rectangle

        # Pick random red, green, and blue color components
        
        r = uniform(.5, 1)    
        g = uniform(.5, 1)    
        b = uniform(.5, 1)    
        
        # set the fill color using the random color components  
        set_fill_color(r, g, b)    
    
        # pick random pixel coordinates 
        x = randint(0, 400)
        y = randint(0, 400)
        
        # draw a circle of radius 50 at the random coordinates
        draw_circle(x, y, 50)
    
        request_redraw()
        sleep(.02)
    
# Run the start_graphics function to open up a graphics window,
# and tell the graphics library to run the random_circles function:
start_graphics(random_circles)

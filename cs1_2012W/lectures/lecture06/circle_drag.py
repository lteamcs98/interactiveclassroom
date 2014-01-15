# circle_drag.py
# Class example by Devin Balkcom, minor changes by THC.
# Drags out a circle with the mouse.

from cs1lib import *
from math import sqrt

# Compute the distance between points x1, y1 and x2, y2
def point_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx * dx + dy * dy)

def main():
    enable_smoothing()
    
    set_clear_color(0, 0, 0)    # black
    set_stroke_color(1, 1, 1)   # white
    set_fill_color(1, 0.5, 0)   # orange
    set_stroke_width(2)
    
    # State variable that keeps track of whether a circle
    # is currently being drawn.
    drawing_circle = False

    clear()
    request_redraw()

    while not window_closed():
        if mouse_down():
            if not drawing_circle: 
                # If a circle is not currently being drawn, and
                # the mouse button is pressed, save the current 
                # mouse location in state variables to use as
                # the center of the circle.
                center_x = mouse_x()
                center_y = mouse_y()
                drawing_circle = True
       
            clear()     # erase whatever we drew before
    
            # Determine the distance from the center to the current mouse location.
            radius = point_distance(center_x, center_y, mouse_x(), mouse_y()) 
    
            # Now we have what we need to draw the circle.
            draw_circle(center_x, center_y, radius)
        
            request_redraw()
            sleep(.02)
        
        # But if the mouse button is not pressed, we are not drawing a circle.
        else:
            drawing_circle = False

start_graphics(main)

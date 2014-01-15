## pulse_circle.py
## A program to demonstrate the use of if statements inside the graphics loop
## Devin Balkcom
## July, 2011

from cs1lib import *

def pulse_circle():
    radius= 1
    growing = True

    disable_stroke()
    enable_smoothing()

    while not window_closed():
        # draw current frame onto a "hidden" background image
        
        clear()
    
        set_fill_color(1, 0, 0)  # set the fill color to red
        draw_circle(200, 200, radius)
    
        set_fill_color(0, 0, 1)  # blue
        draw_circle(200, 200, radius / 2)
    
        set_fill_color(1, 1, 0)  # yellow
        draw_circle(200, 200, radius / 4)
    
        # copy the hidden image into the window
        request_redraw()
        
        # Wait before drawing the next frame,
        #  so the user can see the frame just drawn
        sleep(.02)
        
        # update the state for the next frame
        if growing:
            radius = radius + 2
        else:
            radius = radius - 2
            
        if radius >= 200 or radius <=1:
            growing = not growing

        sleep(.02)

start_graphics(pulse_circle)

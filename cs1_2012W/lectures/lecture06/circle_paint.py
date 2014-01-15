# circle_paint.py
# Devin Balkcom
# September 2011

from cs1lib import *
from random import uniform

def main():
    enable_smoothing()
    clear()

    while not window_closed():
        if mouse_down():
            # Pick a circle color at random
            r = uniform(.5, 1)
            g = uniform(.5, 1)
            b = uniform(.5, 1)
            set_fill_color(r, g, b)

            # Draw the circle.
            draw_circle(mouse_x(), mouse_y(), 20)

            # Update the window.
            request_redraw()
            sleep(.02)

start_graphics(main)
# point_in_rect3.py
# Class example to show one way to determine whether a point is in a rectangle.

from cs1lib import *

# Determine whether the point (x, y) is in a rectangle with upper left corner
# (rx, ry), width rw, and height rh.
def point_in_rectangle(x, y, rx, ry, rw, rh):
    return x >= rx and x < rx + rw and y >= ry and y < ry + rh

def main():
    set_fill_color(1, 0, 0)     # red
    draw_rectangle(100, 100, 60, 30)
    
    while not window_closed():
        if point_in_rectangle(mouse_x(), mouse_y(), 100, 100, 60, 30):
            print "I'm in a box!"
        else:
            print "Not in the box."

start_graphics(main)
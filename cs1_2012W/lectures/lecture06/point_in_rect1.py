# point_in_rect1.py
# Class example to show one way to determine whether a point is in a rectangle.

from cs1lib import *

def main():
    while not window_closed():
        if mouse_x() >= 100 and mouse_x() < 160 and mouse_y() >= 100 and mouse_y() < 130:
            print "I'm in a box!"

start_graphics(main)
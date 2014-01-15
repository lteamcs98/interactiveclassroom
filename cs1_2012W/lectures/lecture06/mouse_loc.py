# mouse_loc.py
# Class example by Devin Balkcom to show the mouse location.

from cs1lib import *

def main():
    while not window_closed():
        print mouse_x(), mouse_y()

start_graphics(main)

# cs1 example:  A simple function to draw a square
# Devin Balkcom
# September, 2011

from cs1lib import *

# Draw a square with upper left x, y and side length s (all ints),
# using only draw_line.
def draw_square(x, y, s):
    draw_line(x, y, x + s, y)
    draw_line(x + s, y, x + s, y + s)
    draw_line(x + s, y + s, x, y + s)
    draw_line(x, y + s, x, y)

# The main function, which will be called when start_graphics is called.
def main():
    clear()
    draw_square(100, 120, 50)

start_graphics(main)

# sierpinsky.py
# Draws a Sierpinksy Gasket.

from cs1lib import *

# Draw a Sierpinsky Gasket of width and height d,
# with upper left at (x, y).
def draw_sierpinsky(x, y, d):
    if d <= 1:
        draw_point(x, y)
    else:
        draw_sierpinsky(x + d/2, y, d/2)
        draw_sierpinsky(x + d/2, y + d/2, d/2)    
        draw_sierpinsky(x, y, d/2)

def main():
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 0)
    
    draw_sierpinsky(0, 0, 400)
    
start_graphics(main)
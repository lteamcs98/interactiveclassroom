# filename: mystery.py
# author:   Zachary Marois
# date:     September 2011
#
# purpose:  Welcomes the user to CS1
# Modeled after the Mystery.java program for CS5
# and roll_over_button.py by Kelsey Harris

# imports
from cs1lib import *
import random
from time import sleep

# display function
def display():
    clear()

    while not window_closed():
        
        welcome()
        
        request_redraw()
        sleep(.05)
    
def welcome():    
    
    # Draw a random ellipse
    r = random.randint(0, 255)/255.0
    g = random.randint(0, 255)/255.0
    b = random.randint(0, 255)/255.0
    set_fill_color( r, g, b, .75)
    
    x = random.randint(0, 400)
    y = random.randint(0, 300)
    disable_stroke()
    draw_ellipse(x, y, 50, 40)
    
    # Draw Welcome messages
    enable_stroke()
    set_stroke_color(0, 0, 0, 1)
    draw_text("Welcome", x - 30, y - 5)
    draw_text("To CS1", x - 25, y + 15)
    

start_graphics(display, "Welcome to CS1", 400, 300)

# Program to draw a simple house
# cs1 example of use of commenting and whitespace
# author Devin Balkcom
# July, 2011

# Program to draw a simple house
# cs1 example of use of commenting and whitespace
# author Devin Balkcom
# July, 2011

from cs1lib import *

# Function to draw a house.
def draw_house():

    clear()
    disable_stroke()

    # draw the lawn
    set_fill_color(0, .5, 0) # dark green
    draw_rectangle(0, 300, 400, 100)

    # draw the main square part of the house
    set_fill_color(.5, .4, .2) # brown
    draw_rectangle(200, 250, 130, 100)  

    # draw the roof
    set_fill_color(.3, .3, .3)  # gray
    draw_triangle(200, 250, 330, 250, 265, 200)

    # draw the door
    set_fill_color(.6, .5, .3)  # light brown
    draw_rectangle(280, 310, 25, 40)

    # draw the doorknob
    set_fill_color(.9, .8, .2) # gold
    draw_circle(300, 330, 3)

start_graphics(draw_house)

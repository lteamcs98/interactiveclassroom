# geh.py
# Solution to CS 1 Short Assignment #2 by THC
# Draws green eggs and ham, with a fork and my name.

from cs1lib import *

# Set the fill color to white.
def set_fill_white():
    set_fill_color(1, 1, 1) # white
    
# Set the fill color to green.
def set_fill_green():
    set_fill_color(0, 1, 0) # green
    
# Set the stroke color to blue.
def set_stroke_blue():
    set_stroke_color(0, 0, 1)   # blue
    
# Set the stroke color to black.
def set_stroke_black():
    set_stroke_color(0, 0, 0)   # black
 
# Make a red background.
def make_background_red():
    set_clear_color(1, 0, 0)    # red
    clear()

# Draws green eggs and ham, along with my name
def draw_green_eggs_and_ham():
    make_background_red()
    
    # Use slightly heavy strokes
    set_stroke_black()  # not really necessary, since black is the default
    set_stroke_width(2)
    
    # Draw a plate as a white triangle
    set_fill_white()
    draw_triangle(50, 200, 320, 100, 300, 325)
    
    # Draw the whites of two eggs as ellipses
    draw_ellipse(130, 210, 28, 18)
    draw_ellipse(200, 240, 28, 18)
 
    # Draw the egg yolks in green
    set_fill_green()
    disable_stroke()        # no outline for the yolks
    draw_circle(130, 210, 10)
    draw_circle(200, 240, 10)
    
    # Draw green ham as a green ellipse with no outline
    draw_ellipse(250, 170, 50, 25)
    # Add the little white center bone
    set_fill_white()
    draw_circle(250, 170, 5)
    
    # Draw the fork.
    enable_stroke()
    set_stroke_blue()
    fork_center = 225   # x-coordinate of fork center
    fork_top = 100      # y-coordinate of fork top
    tine_pitch = 4      # 4 pixels between tine centers
    tine_base = 155     # y-coordinate of base of tines
    tine_point = 170    # y-coordinate of point of tines
    
    # Draw the fork handle.
    draw_line(fork_center, fork_top, fork_center, tine_base)
    
    # Draw the base of the tines.
    draw_line(fork_center - 1.5 * tine_pitch, tine_base,
              fork_center + 1.5 * tine_pitch, tine_base)
    
    # Draw the four tines, horizontally centered at the fork handle.
    draw_line(fork_center - 1.5 * tine_pitch, tine_base,
              fork_center - 1.5 * tine_pitch, tine_point)
    draw_line(fork_center - 0.5 * tine_pitch, tine_base,
              fork_center - 0.5 * tine_pitch, tine_point)
    draw_line(fork_center + 0.5 * tine_pitch, tine_base,
              fork_center + 0.5 * tine_pitch, tine_point)
    draw_line(fork_center + 1.5 * tine_pitch, tine_base,
              fork_center + 1.5 * tine_pitch, tine_point)

    # Sign my work
    set_stroke_black()
    draw_text("Tom Cormen", 20, 380)
    
start_graphics(draw_green_eggs_and_ham)

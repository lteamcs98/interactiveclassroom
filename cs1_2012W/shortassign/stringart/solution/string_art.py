from cs1lib import *

# Function to make string art with two sticks, A and B.  Stick A
# has endpoints (x1a, y1a) and (x2a, y2a).  Stick B has endpoints
# (x1b, y1b), (x2a, y2b).  The parameter strings says how many
# strings to put between the two sticks.
def make_string_art(x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b, strings):
    # Start by making the background black.
    set_clear_color(0, 0, 0)
    clear()
    
    enable_smoothing()
    
    # Draw the sticks in red, 3 pixels wide.
    set_stroke_color(1, 0, 0)
    set_stroke_width(3)
    draw_line(x1a, y1a, x2a, y2a)   # draw stick A
    draw_line(x1b, y1b, x2b, y2b)   # draw stick B
    
    set_stroke_width(1)             # strings should be thin
    
    # Variables red, green, and blue give the color combination for each string.     
    red = 0
    green = 0
    blue = 1
    
    # The variable s indicates which string.  It runs from 0 to strings-1, so
    # that it takes on strings different values.
    s = 0
    while s < strings:
        fraction = float(s) / float(strings - 1)    # how far from (x1a, y1a) on stick A
        reverse_fraction = 1.0 - fraction           # how far from (x1b, y1b) on stick B
        
        # Compute the points where the strings attach on sticks A and B.
        attach1_x = x1a + fraction * (x2a - x1a)
        attach1_y = y1a + fraction * (y2a - y1a)
        attach2_x = x1b + reverse_fraction * (x2b - x1b)
        attach2_y = y1b + reverse_fraction * (y2b - y1b)
        
        # The string color changes as the strings progress down the sticks.
        # It always has no red.  It starts with no green and all blue, and
        # each string has a little more green and a little less blue than the
        # string before it.  By the time we draw the last string, it has all
        # green and no blue.
        green = fraction
        blue = reverse_fraction
        set_stroke_color(red, green, blue)
        
        # Now that we have the attachment points and the color set, draw
        # the string.
        draw_line(attach1_x, attach1_y, attach2_x, attach2_y)
        
        # Go on to the next string.
        s = s + 1    
    
# Main function.  Just calls make_string_art with parameters.
def main():
    make_string_art(25, 50, 50, 200, 350, 180, 200, 350, 25)
    
start_graphics(main)

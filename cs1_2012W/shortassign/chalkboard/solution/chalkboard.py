# chalkboard.py
# Solution to CS 1 Short Assignment 5 by Devin Balkcom with minor changes by THC.
# Allows the user to drag the mouse to draw on a black chalkboard.
# The chalk is initially white.
# Pressing the w key makes the chalk color white.
# Pressing the r key makes the chalk color red.
# Pressing the g key makes the chalk color green.
# Pressing the b key makes the chalk color blue.
# Pressing the y key makes the chalk color yellow.
# Pressing the e key erases by making the chalk color black.
# Pressing the o key makes the chalk color orange (not required).
# Pressing the p key makes the chalk color purple (not required).
# Pressing the E key erases the chalkboard and makes the chalk color white (not required).

from cs1lib import *	

def main():
    old_x = mouse_x()           # initialize old_x, old_y; probably unnecessary
    old_y = mouse_y()
    
    set_stroke_color(1, 1, 1)   # white chalk
    set_stroke_width(2)         # 2 pixels wide
    
    set_clear_color(0, 0, 0)    # black background
    clear()                     # show the black background
    
    enable_smoothing()          # it looks a little better this way

    while not window_closed():    
        if mouse_down():        # draw only if the mouse button is pressed
            draw_line(old_x, old_y, mouse_x(), mouse_y())
    
        if is_key_pressed("r"):
            set_stroke_color(1, 0, 0)   # draw in red
        elif is_key_pressed("g"):
            set_stroke_color(0, 1, 0)   # draw in green
        elif is_key_pressed("b"):
            set_stroke_color(0, 0, 1)   # draw in blue
        elif is_key_pressed("w"):
            set_stroke_color(1, 1, 1)   # draw in white
        elif is_key_pressed("y"):
            set_stroke_color(1, 1, 0)   # draw in yellow
        elif is_key_pressed("o"):
            set_stroke_color(1, 0.5, 0) # draw in orange
        elif is_key_pressed("p"):
            set_stroke_color(0.25, 0, 0.5)  # draw in purple
        elif is_key_pressed("e"):
            set_stroke_color(0, 0, 0)   # draw in black (erase)
        elif is_key_pressed("E"):
            clear()                     # erase the board
            set_stroke_color(1, 1, 1)   # draw in white
    
        # Remember where the mouse is now for the next time we draw.
        # If the button is not pressed, then when it is first pressed,
        # it'll probably be here, so it's OK to draw a line from here
        # to where the mouse is when the button is first pressed.
        old_x = mouse_x()
        old_y = mouse_y()
        
        request_redraw()    # show what we've done
        sleep(.02)          # and wait 1/50 second

start_graphics(main)

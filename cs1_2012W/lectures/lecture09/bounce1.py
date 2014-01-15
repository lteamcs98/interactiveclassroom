# CS 1 example: Simple animation of a bouncing ball
# Devin Balkcom
# August, 2011
# Modified by THC.

from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# For convenience, this program treats the bottom of the
# screen as having y coordinate 0, so that y increases
# in the upwards direction for all calculations.
# start_graphics is passed a special parameter that
# indicates that all frames are to be drawn upside down.

FLOOR_Y = 100
CEILING_Y = WINDOW_HEIGHT - FLOOR_Y
BALL_RADIUS = 10

def main():
    # Initial coordinates for the ball.
    x = WINDOW_WIDTH / 2
    y = CEILING_Y - BALL_RADIUS
    
    # x and y velocities for the ball, in pixels per frame.
    v_x = 0
    v_y = -4

    set_clear_color(1, 1, 1)    # white background
    set_fill_color(.3, .5, 1)   # blue ball
    
    set_stroke_width(2)
    set_stroke_color(0, 0, 0) # black floor   

    while not window_closed():
        # Draw the current frame.
        clear()
    
        # Draw the ball.
        disable_stroke()
        draw_circle(x, y, BALL_RADIUS)
    
        # Draw the floor and the ceiling.
        enable_stroke()
        draw_line(0, FLOOR_Y, WINDOW_WIDTH, FLOOR_Y)
        draw_line(0, CEILING_Y, WINDOW_WIDTH, CEILING_Y)

        # Check whether the next y location would cause a bounce.
        next_y = y + v_y
        if next_y - BALL_RADIUS < FLOOR_Y or next_y + BALL_RADIUS > CEILING_Y:
            v_y = -v_y  # reverse the y velocity

        # Update the x and y positions using the velocities.
        x = x + v_x
        y = y + v_y

        # Update the display and wait for the next frame.
        request_redraw()
        sleep(.05)

# The last parameter of start_graphics, with the value True, indicates
# that all graphics should be drawn upside down.  Therefore, 0, 0 is the
# *bottom* left of the graphics window.  This view is convenient for
# physical simulations.
start_graphics(main, "Bouncing ball", WINDOW_WIDTH, WINDOW_HEIGHT, True)

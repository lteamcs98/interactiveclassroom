# CS 1 example: Simple animation of a bouncing ball
# Devin Balkcom
# August, 2011
# Modified by THC.

from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

FLOOR_Y = 100
CEILING_Y = WINDOW_HEIGHT - FLOOR_Y
BALL_RADIUS = 10

FRAME_RATE = 60     # how many frames to display per second
TIMESTEP = 1.0 / FRAME_RATE    # how often to refresh the frame    

def draw_ball(x, y):
    disable_stroke()
    set_fill_color(.3, .5, 1)   # blue ball
    draw_circle(x, y, BALL_RADIUS)

def draw_boundaries():
    set_stroke_width(2)
    set_stroke_color(0, 0, 0) # black floor and ceiling
    enable_stroke()
    draw_line(0, FLOOR_Y, WINDOW_WIDTH, FLOOR_Y)
    draw_line(0, CEILING_Y, WINDOW_WIDTH, CEILING_Y)

def compute_next_position(position, velocity, timestep):
    return position + velocity * timestep

def main():
    # Initial coordinates for the ball.
    x = WINDOW_WIDTH / 2
    y = CEILING_Y - BALL_RADIUS
    
    # x and y velocities for the ball, now in pixels per second.
    v_x = 0
    v_y = -80

    set_clear_color(1, 1, 1)    # white background
    enable_smoothing()

    while not window_closed():
        # Draw the current frame.
        clear()
        draw_ball(x, y)
        draw_boundaries()

        # Check whether the next y location would cause a bounce.
        next_y = compute_next_position(y, v_y, TIMESTEP)
        if next_y - BALL_RADIUS < FLOOR_Y or next_y + BALL_RADIUS > CEILING_Y:
            v_y = -v_y  # reverse the y velocity

        # Update the x and y positions using the velocities.
        x = compute_next_position(x, v_x, TIMESTEP)
        y = compute_next_position(y, v_y, TIMESTEP)
    
        # Update the display and wait for the next frame.
        request_redraw()
        sleep(TIMESTEP)

# The last parameter of start_graphics, with the value True, indicates
# that all graphics should be drawn upside down.  Therefore, 0, 0 is the
# *bottom* left of the graphics window.  This view is convenient for
# physical simulations.
start_graphics(main, "Bouncing ball", WINDOW_WIDTH, WINDOW_HEIGHT, True)

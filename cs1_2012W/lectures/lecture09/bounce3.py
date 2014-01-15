# CS 1 example: Simple animation of a bouncing ball
# Devin Balkcom
# August, 2011
# Modified by THC.

from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

FRAME_RATE = 60     # how many frames to display per second
TIMESTEP = 1.0 / FRAME_RATE    # how often to refresh the frame    

# Computations will now use meters, and we'll convert meters to
# pixels with a scaling factor during drawing:
PIXELS_PER_METER = 10.0

FLOOR_Y = 4.0       # location now in meters

INITIAL_X = 5.0     # locations are now measured in meters
INITIAL_Y = 25.0
INITIAL_V_X = 4.0
INITIAL_V_Y = 0.0   # velocity is now measured in meters/second

EARTH_GRAVITY_ACCELERATION = -9.8   # Earth acceleration due to gravity, m/sec^2

BALL_RADIUS = 10  # radius of the ball in pixels, not used in velocity computations

def draw_ball(x, y):
    disable_stroke()
    set_fill_color(.3, .5, 1)   # blue ball
    draw_circle(x * PIXELS_PER_METER, y * PIXELS_PER_METER, BALL_RADIUS)

def draw_floor():
    set_stroke_width(2)
    set_stroke_color(0, 0, 0) # black floor   
    enable_stroke()
    draw_line(0, FLOOR_Y * PIXELS_PER_METER, WINDOW_WIDTH, FLOOR_Y * PIXELS_PER_METER)

# Computation of position uses meters, not pixels.
def compute_next_position(position, velocity, timestep):
    return position + velocity * timestep

def compute_next_velocity(velocity, acceleration, timestep):
    return velocity + acceleration * timestep

def main():
    # Initial coordinates for the ball.
    x = INITIAL_X
    y = INITIAL_Y
    
    # x and y velocities for the ball.
    v_x = INITIAL_V_X
    v_y = INITIAL_V_Y

    set_clear_color(1, 1, 1)    # white background
    enable_smoothing()

    while not window_closed():
        # Draw the current frame.
        clear()
        draw_ball(x, y)
        draw_floor()

        # Update the state for the next frame.
        # See where the ball will be at its current velocity.
        next_y = compute_next_position(y, v_y, TIMESTEP)
        next_x = compute_next_position(x, v_x, TIMESTEP)
        
        # Will the ball bounce off the floor?
        if next_y - (BALL_RADIUS / PIXELS_PER_METER) < FLOOR_Y:
            v_y = -v_y
    
        # Will the ball bounce off a side wall?
        if next_x * PIXELS_PER_METER + BALL_RADIUS > WINDOW_WIDTH or \
                next_x * PIXELS_PER_METER - BALL_RADIUS < 0:
            v_x = -v_x

        # Now compute the real next position and next velocity.
        x = compute_next_position(x, v_x, TIMESTEP)
        y = compute_next_position(y, v_y, TIMESTEP)
        v_y = compute_next_velocity(v_y, EARTH_GRAVITY_ACCELERATION, TIMESTEP)

        # Update the display and wait for the next frame.
        request_redraw()
        sleep(TIMESTEP)

# The last parameter of start_graphics, with the value True, indicates
# that all graphics should be drawn upside down.  Therefore, 0, 0 is the
# *bottom* left of the graphics window.  This view is convenient for
# physical simulations.
start_graphics(main, "Bouncing ball", WINDOW_WIDTH, WINDOW_HEIGHT, True)

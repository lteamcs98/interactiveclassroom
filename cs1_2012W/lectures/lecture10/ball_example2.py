from cs1lib import *
from ball import Ball

WINDOW_HEIGHT = 400
FRAME_RATE = 40
TIMESTEP = 1.0 / FRAME_RATE
PIXELS_PER_METER = 10.0

def main():
    set_clear_color(1, 1, 1)
    enable_smoothing()
    
    ball = Ball(20, 20, 0, 0, .3, .3, 1.)

    while not window_closed():
        clear()
    
        ball.draw(PIXELS_PER_METER)

        ball.update_position(TIMESTEP)
        ball.update_velocity(TIMESTEP)
   
        request_redraw()
        sleep(TIMESTEP)
 
start_graphics(main, flipped_y = True)

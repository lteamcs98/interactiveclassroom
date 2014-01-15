from cs1lib import *

EARTH_GRAVITY_ACCELERATION = -9.8   # Earth acceleration due to gravity, m/sec^2
BALL_RADIUS = 10  # radius of the ball in pixels, not used in velocity computations

class Ball:
    def __init__(self, start_x, start_y, start_v_x, start_v_y, r = 0.5, g = 0.5, b = 0.5):
        # Location and velocities of the ball.
        self.x = start_x
        self.y = start_y
        self.v_x = start_v_x
        self.v_y = start_v_y

        # Color of the ball, for drawing purposes.
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x = self.x + timestep * self.v_x
        self.y = self.y + timestep * self.v_y 

    def update_velocity(self, timestep):
        self.v_y = self.v_y + timestep * EARTH_GRAVITY_ACCELERATION

    def animate_step(self, timestep):
        self.update_position(timestep)
        self.update_velocity(timestep)

    def draw(self, pixels_per_unit):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * pixels_per_unit, self.y * pixels_per_unit, BALL_RADIUS)

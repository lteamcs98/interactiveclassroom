## Robot simulator for Dartmouth cs1
## Devin Balkcom
## July, 2011


## This means that student code that uses the simulator must run in a separate thread.  The design is therefore that a student writes a function robot_control, and passes that function as an argument to the start_simulator function.  This isn't quite the same way that the actual robot control programs are written.


#from cs1graphics import *
from cs1lib import *
from math import *

import threading
from time import sleep

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

ROBOT_RADIUS = 50

__FRAME_RATE = 20

CLIFF_SENSOR_LOC_LEFT = (40, 10)
CLIFF_SENSOR_LOC_RIGHT = (40, -10)



# Location of image files for robot and floor (hardcoded)
IMAGE_ROBOT = "create_robot.png"
IMAGE_FLOOR = "robotsim_floor01.png"

# Kludge suggested by Devin.
robot = None

class SimRobot:
    def __init__(self, floor_filename):
        self.x = WINDOW_WIDTH/2
        self.y = WINDOW_HEIGHT - ROBOT_RADIUS
        self.theta = 0    # theta is in radians
        self.image = load_image(IMAGE_ROBOT)

        self.floor_image = load_image(floor_filename)

        self.velocity = 0
        self.angular_velocity = 0
        self.dt = .05;

    def draw(self):

        # draw the floor
        draw_image(self.floor_image, 0, 0)

        # draw the robot
        draw_image(self.image, self.x, self.y, self.image.width()/2, self.image.height()/2, degrees(self.theta))

        # draw the cliff sensor values on top of the robot
        disable_stroke()
        set_fill_color(self.get_ir_left(), 0, 0)
        left_cliff = self.__left_cliff_loc()
        draw_circle(left_cliff[0], left_cliff[1], 3)

        set_fill_color(self.get_ir_right(), 0, 0)
        right_cliff = self.__right_cliff_loc()
        draw_circle(right_cliff[0], right_cliff[1], 3)

       # print self.get_ir_left(), self.get_ir_right()

    # return the location of the left cliff sensor in world coords
    def __left_cliff_loc(self):
        return self.world_coords(CLIFF_SENSOR_LOC_LEFT)
        #return self.world_coords((20, 0))

    def __right_cliff_loc(self):
        return self.world_coords(CLIFF_SENSOR_LOC_RIGHT)

    def __get_ir(self, loc):
        (x, y) = loc
        (r, g, b, a) = self.floor_image.get_pixel(x, WINDOW_HEIGHT - y)
        intensity = (r + g + b) / 3.0
        return intensity
        
    
    # returns the average intensity of the pixel color under the left ir sensor
    def get_ir_left(self):
        return self.__get_ir(self.__left_cliff_loc())

    def get_ir_right(self):
        return self.__get_ir(self.__right_cliff_loc())

    def world_coords(self, loc):
        x, y = loc
        world_x = self.x + x * cos(self.theta) - y * sin(self.theta) 
        world_y = self.y + x * sin(self.theta) + y * cos(self.theta)

        return (world_x, world_y)
        

    def update_location(self):
        self.x = self.x + self.velocity * cos(self.theta) * self.dt
        # because pixel y coordinates are reversed from cartesian, subtract
        # y when moving
        self.y = self.y + self.velocity * sin(self.theta) * self.dt  
        self.theta = self.theta + self.angular_velocity * self.dt

    def update(self):
        while(True):
            #print "Robot update"
            self.update_location()
            #print self.theta, self.angular_velocity
            sleep(self.dt)

    def turn(self, angular_velocity):
        "Turn called"
        self.velocity = 0
        self.angular_velocity = angular_velocity

    def drive(self, velocity):
        self.velocity = velocity
        self.angular_velocity = 0

def draw_robot():
    enable_smoothing()
    while not window_closed():
        robot.draw()
        request_redraw()
        sleep(1.0 / __FRAME_RATE)
    
def start_simulator(robot_control_fn):
    global robot
    
    robot = SimRobot(IMAGE_FLOOR)

    robot_thread = threading.Thread(target = robot.update)
    robot_thread.daemon = True
    robot_thread.start()

    control_thread = threading.Thread(target = robot_control_fn)
    control_thread.daemon = True
    control_thread.start()

    start_graphics(draw_robot, "Robot simulator", WINDOW_WIDTH, WINDOW_HEIGHT, flipped_y = True)

# turn at `angular velocity` radians per second
def turn(angular_velocity):
    robot.turn(angular_velocity)

# drive at `velocity` pixels per second
def drive(velocity):
    robot.drive(velocity)

# stop the robot
def stop():
    turn(0)

# turn left approximately rad radians.  Just as on the real robot, this
# is not an exact turn!

def left(rad = pi/2):
    turn(1)
    sleep(rad)

def right(rad = pi/2):
    turn(-1)
    sleep(rad)

# drive an approximate number of pixels forwards.  This is not an exact distance!
def straight(pixels = 100):
    if pixels > 0:
        drive(20)
        sleep(pixels / 20.0)
    else:
        drive(-20)
        sleep(-pixels / 20.0)

def get_ir_left():
    return robot.get_ir_left()

def get_ir_right():
    return robot.get_ir_right()

def place_robot(x, y, theta):
    global robot
    robot.x = x
    robot.y = y
    robot.theta = theta
  
## test program for simulator
if __name__== "__main__":
  
  
    def robot_control():
        print "Robot control function started."
        place_robot(200, 200, 0)
        while True:
            straight()
            straight()
            left()

    start_simulator(robot_control)

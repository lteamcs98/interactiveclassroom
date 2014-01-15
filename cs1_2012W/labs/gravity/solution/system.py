# system.py
# Solution for CS 1 Lab Assignment 2.
# Definition of the System class for gravity simulation.
# A System represents several Body objects.
# Based on code written by Aaron Watanabe and Devin Balkcom.

UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.67384e-11 

from math import sqrt
from body import Body

class System:
    # To initialize a System, just save the body list.
    def __init__(self, body_list):
        self.__body_list = body_list

    # Draw a System by drawing each body in the body list.
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.__body_list:
            body.draw(cx, cy, pixels_per_meter)

    # Compute the distance between bodies n1 and n2.
    def __dist(self, n1, n2):
        dx = self.__body_list[n2].get_x() - self.__body_list[n1].get_x()
        dy = self.__body_list[n2].get_y() - self.__body_list[n1].get_y()
        return sqrt(dx * dx + dy * dy)
        
    # Compute the acceleration of all other bodies on body n.
    def __compute_acceleration(self, n):
        total_ax = 0
        total_ay = 0
        
        for i in range(len(self.__body_list)):
            if i != n:  # don't compute the acceleration of body n on itself!
                r = self.__dist(i, n)
                a = UNIVERSAL_GRAVITATIONAL_CONSTANT * self.__body_list[i].get_mass() / (r * r)
 
                # a is the magnitude of the acceleration.
                # Break it into its x and y components ax and ay,
                # and add them into the running sums total_ax and total_ay.
                dx = self.__body_list[i].get_x() - self.__body_list[n].get_x()
                ax = a * dx / r
                total_ax += ax
                dy = self.__body_list[i].get_y() - self.__body_list[n].get_y()
                ay = a * dy / r
                total_ay += ay
        
        # To return two values, use a tuple.
        return (total_ax, total_ay)

    # Compute the acceleration on each body, and use the acceleration
    # to update the velocity and then the position of each body.
    def update(self, timestep):
        for n in range(len(self.__body_list)):
            (ax, ay) = self.__compute_acceleration(n)
            self.__body_list[n].update_velocity(ax, ay, timestep)
            self.__body_list[n].update_position(timestep)

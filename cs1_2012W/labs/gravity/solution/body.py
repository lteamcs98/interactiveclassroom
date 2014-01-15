# body.py
# Solution for CS 1 Lab Assignment 2.
# Definition of the Body class for gravity simulation.
# Based on code written by Aaron Watanabe and Devin Balkcom.

from cs1lib import *

class Body:
    # Initialize a Body object.
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.__mass = mass
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy

        self.__pixel_radius = pixel_radius
        self.__r = r
        self.__g = g
        self.__b = b

    # Return the mass of a Body object.
    def get_mass(self):
        return self.__mass

    # Return the x position of a Body object.
    def get_x(self):
        return self.__x
    
    # Return the y position of a Body object.
    def get_y(self):
        return self.__y
    
    # Update the position of a Body object for a given timestep.
    def update_position(self, timestep):
        self.__x += self.__vx * timestep
        self.__y += self.__vy * timestep

    # Update the velocity of a Body object for a given timestep by
    # given accelerations ax in x and ay in y.
    def update_velocity(self, ax, ay, timestep):
        self.__vx += ax * timestep
        self.__vy += ay * timestep

    # Have a Body object draw itself.__
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.__r, self.__g, self.__b)
        disable_stroke()
        enable_fill()
        draw_circle(cx + self.__x * pixels_per_meter,
                    cy + self.__y * pixels_per_meter,
                    self.__pixel_radius)

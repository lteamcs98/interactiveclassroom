# tuples.py
# CS 1 class examples to show how to use tuples.

# creating a tuple
pixel_coordinates = (200, 100)

# parentheses are optional when obvious from context
another_tuple = 18, 20.5, 6, "Hello"

print pixel_coordinates
print another_tuple

color = (1., 0., 1.)

# unpack the color tuple into red, green, and blue variables
red, green, blue = color
print blue

location = 12, 6   # (parentheses optional)
x, y = location
print x

def compute_square_and_cube(x):
    return x * x, x * x * x

print compute_square_and_cube(3)

# Unpacking results of a function call:
four2, four3 = compute_square_and_cube(4)
print four2
print four3

# exploding a tuple for use in a function call
color = 1.0, 0, 1.0  # purple

def print_rgb(r, g, b):
    print r
    print g
    print b

print_rgb(*color)


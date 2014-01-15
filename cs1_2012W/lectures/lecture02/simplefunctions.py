# This module contains simple example of functions that print a few things on the screen,
# used as examples in the first lecture of cs1.

# Devin Balkcom, June 2011

from datetime import datetime
from math import sqrt

# print the current date and time
def print_date_and_time():
    print datetime.now()
    
# print the square root of a number
# (as an example of parameters)

def print_sqrt(x):
    print sqrt(x)

# counter.py
# Solution to CS 1 Short Assignment 7 by THC.
# Defines a class for a Counter object, which counts down to 0.
# Then it wraps back to limit-1.

class Counter:
    # Initialize a Counter with a required limit and an optional
    # minimum number of digits to display.
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        if 0 <= initial < limit:
            self.value = initial
        else:
            print "Bad initial value, using " + str(limit - 1)
            self.value = limit - 1
        self.min_digits = min_digits
        
    # Return the value of this Counter.
    def get_value(self):
        return self.value
    
    # Return a string giving the value of this Counter, but
    # padded with zeros so that at least min_digits are included.
    def __str__(self):
        s = str(self.value)
        string_rep = ""
        i = 0
        while i < self.min_digits - len(s):
            string_rep += "0"
            i += 1
        return string_rep + s
    
    # Decrement this Counter, wrapping around to limit-1 if it hits 0
    # Return a boolean indicating whether it hit 0.
    def tick(self):
        self.value -= 1
        if self.value < 0:
            self.value = self.limit - 1
            return True
        else:
            return False
from math import pi

def compute_circle_area(r):
    global pi
    pi = 3      # changes the value of pi, now and forever.  Scary!
    return pi * r * r

compute_circle_area(10)
print pi

from math import sqrt

def compute_four():
    print "Your wish is my command!  I compute four!"
    return 24 / 4 - 2

def calculate_four():
    print "Your wish is my command!  I compute four!"
    return sqrt(4.0) + 2

print "Result of compute_four():", compute_four()
print "Result of calculate_four():", calculate_four()
print 33 / compute_four()    # prints 8
print 33 / calculate_four()  # prints 8.25

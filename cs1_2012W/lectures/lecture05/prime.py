## Program to check if a number is prime
## Devin Balkcom
## July 2011

from math import sqrt

# Check if a value is prime, and return True or False.
def is_prime(possible_prime): 
    # Check if the input to the function is reasonable.
    assert type(possible_prime) == int
    assert possible_prime > 0

    # A number is prime if it has no integer divisors
    # greater than the square root of the number.

    max_factor = int(sqrt(possible_prime)) 

    # Loop over all possible factors less than or equal to
    # the max that we need to check.
    factor = 2
    while factor <= max_factor:
        if possible_prime % factor == 0:
            # It's divisible by factor, and therefore is not prime.
            return False
        factor = factor + 1

    # The while loop completed, so no integer factors were found.
    # It's a prime!
    return True

value = 22
if is_prime(value):
    print str(value) + " is prime!"
else:
    print str(value) + " is not prime!"

# This call should cause an assertion error.
print is_prime("rib")

# So should this call.
print is_prime(-3)

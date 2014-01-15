# list_comp.py
# CS 1 class examples to show list comprehensions.

from math import sqrt

fresh_fruit = ["  banana", "  loganberry ", "passion fruit  "]
stripped_fruit = []
for fruit in fresh_fruit:
    stripped_fruit.append(fruit.strip())
print stripped_fruit

stripped_fruit = [fruit.strip() for fruit in fresh_fruit]
print stripped_fruit

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print [x*y for x in vec1 for y in vec2]

# An example with filtering.
def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        limit = sqrt(n)
        i = 3
        while i <= limit:
            if n % i == 0:
                return False
            else:
                i += 2
        return True
    
primes_100 = [x for x in range(1, 101) if is_prime(x)]
print primes_100

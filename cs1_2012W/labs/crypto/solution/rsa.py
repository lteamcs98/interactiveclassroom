# rsa.py
# Written by THC for CS 1 Lab Assignment 5.
# Contains functions to generate RSA public and secret keys.

from random import randint
from mod_exp import modular_exponentiation

# Return an odd number with d decimal digits.
def generate_odd_number(d):
    return randint(10**(d-1), (10**d)-1) | 1
    
# Return true if m passes the Fermat test for primality: m is
# declared to be prime if (2**(m-1)) % m equals 1. 
def fermat_test(m):
    return modular_exponentiation(2, m-1, m) == 1

# Return a random prime number with d decimal digits.
def generate_prime(d):
    while True:
        m = generate_odd_number(d)
        if fermat_test(m):
            return m
        
# Perform Euclid's greatest common divisor algorithm.
# Given integers a and b, not both 0, return a triple (g, i, j)
# such that g is the gcd of a and b, and g = a*i + b*j.
def euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (g, i_prime, j_prime) = euclid(b, a % b)
        return (g, j_prime, i_prime - (a / b) * j_prime)
    
# Given the parameter r in RSA, compute the exponents e and d.
# e is a small odd integer that is relatively prime to r, and
# d is the multiplicative inverse of e, modulo r.
def compute_e_d(r):
    # Start with e = 5, and continue trying odd integers until
    # finding one that is relatively prime to r.
    e = 5
    while True:
        (g, i, j) = euclid(r, e)
        if g == 1:
            # e is relatively prime to r.  The value of j returned
            # by euclid, taken modulo r, is e's multiplicative inverse,
            # modulo r.
            return (e, j % r)
        else:
            e += 2

# Generate randomly chosen public and secret RSA keys, and return them as
# a list [ [e, n], [d, n] ], where [e, n] is the public key and [d, n] is
# the secret key.  The parameter d is the number of decimal digits in the
# RSA parameters p and q, so that n should have 2d decimal digits.
def generate_RSA_keys(d):
    p = generate_prime(d)
    q = generate_prime(d)
    while q == p:
        q = generate_prime(d)
    n = p * q
    r = (p-1) * (q-1)
    (e, d) = compute_e_d(r)
    return [ [e, n], [d, n]]

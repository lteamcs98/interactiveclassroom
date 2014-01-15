# mod_exp.py
# Written by THC.
# Provides a modular exponentiation function.

# Return (x**d) % n.
def modular_exponentiation(x, d, n):
    result = 1
    multiplier = x
    
    # Invariant: If d_k is the k least significant bits of d,
    # then at the start of each iteration, result = (x**d_k) % n.
    while d > 0:
        if d % 2 == 1:
            result = (result * multiplier) % n
        multiplier = (multiplier * multiplier) % n
        d /= 2
        
    return result

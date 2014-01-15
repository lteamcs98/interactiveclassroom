# fact_iterative.py
# Computes n! iteratively.

def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

print factorial(5)
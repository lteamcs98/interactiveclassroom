# fib_recursive.py
# Recursively computes the nth Fibonacci number.

def fib(n):    
    if n == 1 or n == 2:
        return 1    # base case
    else:    
        return fib(n - 1) + fib(n - 2)
    
print fib(7)

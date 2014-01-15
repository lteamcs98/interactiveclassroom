# how_rich.py
# Solution to CS 1 Short Assignment #3, Problem 1 by THC.
# Computes the balance of a bank account that started with $1.00 in year 0
# and had interest compounded annually through 2012.

INITIAL_BALANCE = 1.0       # how much the account starts with
INTEREST_RATE = 5.0         # interest rate, as a percent
CURRENT_YEAR = 2012         # when to stop compounding interest
balance = INITIAL_BALANCE   # current balance, will be updated annually
year = 1                    # which year

# Update the balance once per year, up to and including CURRENT_YEAR.
while year <= CURRENT_YEAR:
    year = year + 1
    balance = balance + (INTEREST_RATE / 100.0) * balance

# All done.  Print the result, nicely formatted.    
print "At year " + str(CURRENT_YEAR) + ", the balance is " + str(balance) + "."

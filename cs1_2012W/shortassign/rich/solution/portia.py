# portia.py
# Solution to CS 1 Short Assignment #3, Problem 2 by THC.
# Computes the balances of two bank accounts:
#    Brutus's account starts with $1 in year 0, compounded at 5% annually.
#    Portia's account starts with $100,000 in year 0, compounded at 4% annually.
# Computes the first year in which Brutus's balance exceeds Portia's balance.


BRUTUS_INITIAL_BALANCE = 1.0       # how much Brutus's account starts with
BRUTUS_INTEREST_RATE = 5.0         # Brutus's interest rate, as a percent
PORTIA_INITIAL_BALANCE = 100000.0  # how much Portia's account starts with
PORTIA_INTEREST_RATE = 4.0         # Portia's interest rate, as a percent
brutus_balance = BRUTUS_INITIAL_BALANCE   # Brutus's balance, will be updated annually
portia_balance = PORTIA_INITIAL_BALANCE   # Portia's balance, will be updated annually
year = 0                           # which year

# Update the balance once per year, until Brutus's balance exceeds Portia's.
while brutus_balance <= portia_balance:
    year = year + 1
    brutus_balance = brutus_balance + (BRUTUS_INTEREST_RATE / 100.0) * brutus_balance
    portia_balance = portia_balance + (PORTIA_INTEREST_RATE / 100.0) * portia_balance
    
# All done.  Print the result, nicely formatted.
print "At year " + str(year) + ", Brutus's balance of " + str(brutus_balance) + \
    " exceeds Portia's balance of " + str(portia_balance) + "."

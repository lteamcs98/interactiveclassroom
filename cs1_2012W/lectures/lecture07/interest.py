RATE = 1.05
YEAR = 2012
balance = 1.0

for year in range(0, YEAR):
    balance = balance *  RATE

print "The balance is " + str(balance) + "."

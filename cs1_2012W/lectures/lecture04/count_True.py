# count_True.py
# By THC.  Shows how a while-loop can count using a boolean variable.

from time import sleep

x = True
print x
sleep(3)    # so we can see the value of x before all heck breaks loose

n = 1

while x:
    print n
    n = n + 1

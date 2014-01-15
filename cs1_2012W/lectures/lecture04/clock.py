# clock.py
# By THC.  Counts out one number per second.

from time import sleep

n = 1

while True:
    print n
    n = n + 1
    sleep(1)    # sleep for 1 second

# timer_driver.py
# Driver to test the Timer class.
# Written by THC.

from timer import Timer

timer = Timer(1, 30, 0)

while not timer.is_zero():
    print timer
    timer.tick()

print timer

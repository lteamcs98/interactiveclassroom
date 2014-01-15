# timer.py
# Class for an hours:minutes:seconds timer.
# Solution to Short Assignment 7 by THC.

from counter import Counter

class Timer:
    # Initialize a Timer with a given number of hours, minutes, seconds.
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)
        
    # Return a string giving this Timer's state.
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
    
    # Tick down a Timer.
    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()
                
    # Return whether the Timer is at 00:00:00.
    def is_zero(self):
        return self.hours.get_value() == 0 and \
            self.minutes.get_value() == 0 and \
            self.seconds.get_value() == 0

# josephus.py
# Solution to CS 1 Short Assignment 11 by THC
# Solves the Josephus problem.
# We start with a circle of n soldiers.  We go around the circle, killing every
# kth remaining soldier until none are left.  The goal is to print out the order
# in which soldiers die off, which is a permutation of the numbers 1 to n.
# victim solution uses a circular, doubly linked list without a sentinel
# to represent the circle of soldiers.

# A class to represent each soldier.
class Soldier:
    # Initialize a Soldier, given his number.
    def __init__(self, number):
        self.number = number    # this soldier's number
        self.next = None        # reference to the next soldier in the circle
        self.prev = None        # reference to the previous soldier in the circle
     
    # Kill off a soldier.   
    def kill(self, prefix, suffix):
        # Tell the world that I'm dead.
        if prefix != None:
            print prefix,
        print self.number,
        if suffix != None:
            print suffix,
        print ""
        
        # Splice myself out of the circle.
        self.prev.next = self.next
        self.next.prev = self.prev

# Class for a circle of Soldier objects.
class Army:
    # Initialize an Army of n Soldier objects.  When this method is done,
    # self.victim references the last Soldier created, i.e., the Soldier numbered n.
    def __init__(self, n):
        self.remaining = n  # how many Soldier objects remain in the circle
        
        # Create the first Soldier, referencing itself in both directions.
        self.victim = Soldier(1)
        self.victim.next = self.victim
        self.victim.prev = self.victim
        
        # Create each succeeding Soldier and link him in.
        # At the start of each iteration of this for-loop, self.victim references
        # the Soldier numbered i-1, i.e., the last Soldier created so far.
        for i in range(2, n+1):
            new = Soldier(i)
            new.next = self.victim.next
            new.prev = self.victim
            self.victim.next.prev = new
            self.victim.next = new
            self.victim = new
    
    # Advance self.victim by k Soldiers in the circle.        
    def advance(self, k):
        for i in range(k):
            self.victim = self.victim.next
    
    # Kill all the Soldiers in the Army, given a skip amount.
    # Assumes that self.victim starts as a reference to Soldier number n.       
    def kill_all(self, skip):
        while self.remaining > 1:
            self.advance(skip)          # go further around the circle
            previous = self.victim.prev # victim's predecessor
            self.victim.kill("Soldier", "buys the farm")  # kill off this victim
            self.victim = previous      # and back up by 1 in the circle
            self.remaining -= 1         # one fewer remaining
            
        # There is just one Soldier left.
        self.victim.kill("The last remaining soldier is", "")

# Ask the user for how many soldiers.        
n = int(raw_input("Enter number n of soliders, at least 2: "))
while n < 2:
    n = int(raw_input("Enter number n of soliders, at least 2: "))

# And for the spacing.
k = int(raw_input("Enter spacing between victims, between 1 and n: "))
while k < 1 or k > n:
    k = int(raw_input("Enter spacing between victims, between 1 and n: "))

army = Army(n)      # create an Army
army.kill_all(k)    # and kill it off
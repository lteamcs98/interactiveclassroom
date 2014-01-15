# counter_driver.py
# Driver to test the Counter class.
# Written by THC.

from counter import Counter

c1 = Counter(10, 9)
c2 = Counter(20, 15, 4)
c3 = Counter(10, 10)

print c3

for i in range(30):
    print c1
    print c2
    print "c1.get_value returns ", c1.get_value()
    print "c2.get_value returns ", c2.get_value()
    if c1.tick():
        print "c1 wraps"
    if c2.tick():
        print "c2 wraps"

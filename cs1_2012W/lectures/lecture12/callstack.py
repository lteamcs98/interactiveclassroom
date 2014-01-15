
def functionA():
    print "A called.  x =", 
    x = 5
    functionC()
    print x
    
def functionB():
    y = 10
    print "B called."    
    
def functionC():
    x = 2
    k = 6
    print "C called.  x =",
    functionB()
    functionD()
    print x
    
def functionD():
    z = 12
    print "D called."

functionA()
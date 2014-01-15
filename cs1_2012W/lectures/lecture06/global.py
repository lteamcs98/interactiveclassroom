def print_x():
    global x      # print_x will use the global variable x
    x = x + 1
    print x      

x = 5             # x is a global variable
print_x()
print x

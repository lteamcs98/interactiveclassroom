row = 1

while row < 10:     # the header for the outer loop
    column = 1
    while column < 10:   # the header for the inner loop
        print str(row * column).rjust(2),
        column += 1

    print ""

    row += 1

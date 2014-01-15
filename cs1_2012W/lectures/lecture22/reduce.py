# reduce.py
# CS 1 class example by THC.
# Demonstrates how to reduce in parallel, using parallelizable for-loops.

# Return the sum of all values in an n-item list a, using parallelizable
# for-loops and recursion.  Takes O(log n) time in parallel with p processors,
# assuming that n <= p.
def parallel_reduce(a):
    n = len(a)
    
    if n == 1:
        return a[0]     # base case: only one value
    else:
        # Create a new list, sums, of half the size, rounding up if n is odd.
        half = (n+1) / 2
        sums = [None] * half
        
        # Using a parallelizable for-loop, add pairs of values in a into sums.
        for i in range(half-1):
            sums[i] = a[2*i] + a[2*i+1]
            
        # Need special code to handle the last one or two values in a, in
        # case n is odd.
        if n % 2 == 0:
            sums[half-1] = a[2*half-2] + a[2*half-1]
        else:
            sums[half-1] = a[2*half-2]
            
        # Having created sums of pairs, return the +-reduction of the sums.
        # This recursive call is on a problem of half the size.
        return parallel_reduce(sums)
    
# Return the sum of all values in an (m*p-1)-item list a, using parallelizable
# for-loops and a call to reduce.  Assumes that processor i works on a[i*m]
# through a[i*m + m-1].  Takes O(m + log p) time in parallel with p processors.
def parallel_reduce_many(a, p, m):
    # Create a list for summing the values in each processor.
    sums = [0] * p
    
    # Using a parallelizable outer for-loop, sum up the values in each processor's
    # portion of a.  With p processors, this loop takes O(m) time.
    for i in range(p):
        for j in range(m):
            sums[i] += a[i*m + j]
            
    # Now we have a list of p sums, so just return what the recursive reduce
    # function returns.  This call takes O(log p) time in parallel with p processors.
    return parallel_reduce(sums)

if __name__ == "__main__":
    my_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print "parallel_reduce:", parallel_reduce(my_list)
    print "parallel_reduce_many:", parallel_reduce_many(my_list, 5, 3)
    print "built-in sum:", sum(my_list)
# binary_search.py
# By THC, based on solution to Short Assignment 8.

def binary_search(the_list, key, left, right):
    if left > right:
        return None
    else:
        midpoint = (left + right) / 2
        
        if the_list[midpoint] == key:
            return midpoint
        elif the_list[midpoint] > key:
            return binary_search(the_list, key, left, midpoint-1)
        else:
            return binary_search(the_list, key, midpoint+1, right)


countries = ["Afghanistan", "Albania", "Algeria", "Andorra", \
             "Angola", "Anguila", "Argentina", "Armenia", "Aruba"]

index = binary_search(countries, "Algeria", 0, len(countries)-1)
print index     # prints 2

index = binary_search(countries, "Florin", 0, len(countries)-1)
print index     # prints None

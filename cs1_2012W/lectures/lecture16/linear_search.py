## Linear search class example
## Devin Balkcom, modified by THC
## October 2011

def linear_search(the_list, key):
    index = 0
    while index < len(the_list):
        if key == the_list[index]:
            return index
        else:
            index += 1
        
    return None

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", \
             "Angola", "Anguila", "Argentina", "Armenia", "Aruba"]

index = linear_search(countries, "Algeria")
print index     # prints 2

index = linear_search(countries, "Florin")
print index     # prints None

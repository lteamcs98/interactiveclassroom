## Linear search class example
## Devin Balkcom
## October 2011

def linear_search(thelist, key):
    for index in range(len(thelist)):
        if key == thelist[index]:
            return index
        
    return None

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguila", "Antartica", "Argentina", "Armenia", "Aruba"]

index = linear_search(countries, "Algeria")

print index


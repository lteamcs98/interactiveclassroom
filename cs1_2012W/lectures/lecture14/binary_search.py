

def binary_search(thelist, key):

    left = 0
    right = len(thelist) - 1

    while left <= right:
        mid = (left + right) / 2

        if thelist[mid] == key:
            return mid
        elif thelist[mid] < key:
            left = mid + 1
        elif thelist[mid] > key:
            right = mid - 1

    return None


countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguila", "Antartica", "Argentina", "Armenia", "Aruba"]


index = binary_search(countries, "Algeria")

print index




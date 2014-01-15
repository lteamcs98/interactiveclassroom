# find.py
# CS 1 class example by THC.
# Shows a simple implementation of the Python find function.

## Return the index of the first occurrence of the pattern in the text.
def my_find(text, pattern):
    index = 0
    while index <= len(text) - len(pattern):
        j = 0
        while j < len(pattern):
            if text[index + j] == pattern[j]:
                j += 1
            else:
                break
        if j == len(pattern):
            return index
        else:
            index += 1
    return -1

from string import find

text = "bananas"
print find(text, "na")
print my_find(text, "na")
print find(text, "nas")
print my_find(text, "nas")
print find(text, "bon")
print my_find(text, "bon")

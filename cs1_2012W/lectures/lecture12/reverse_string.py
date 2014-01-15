# reverse_string.py
# Recursively reverses a string.

def reverse(s):
    if s == "":
        return s    # an empty string is its own reverse
    else:
        # Recursively reverse the tail and concatenate the first character.
        return reverse(s[1:]) + s[0]
    
print reverse("ward")

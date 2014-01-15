# simple_dict.py
# CS 1 class example to show how to use a dictionary.

my_dictionary = {}

my_dictionary["blue"] = 460
print my_dictionary["blue"]

my_dictionary["blue"] = "A color with wavelength of approximately 460 nm."
print my_dictionary["blue"]

# Create a new dictionary to store wavelengths of visible light.
wavelength_dictionary = {}
wavelength_dictionary["blue"] = 450
wavelength_dictionary["orange"] = 600
wavelength_dictionary["green"] = 530
wavelength_dictionary["yellow"] = 580

# Print all key, value pairs in the dictionary.
for key in wavelength_dictionary:
    print key, wavelength_dictionary[key]

print "blue" in wavelength_dictionary  # prints True
print "purple" in wavelength_dictionary # prints False

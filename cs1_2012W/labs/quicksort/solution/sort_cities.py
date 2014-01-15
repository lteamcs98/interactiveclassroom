# sort_cities.py
# Solution to CS 1 Lab Assignment #3 by THC.
# Reads in a file of information about world cities and sorts
# it according to various criteria.
# Each line of the file has the following fields, separated by commas:
#    1. A two-letter country code.
#    2. The name of the city.
#    3. A two-character region code.  The characters might be numeric,
#        alphabetical, or a combination.
#    4. The city's population, an integer.
#    5. The city's latitude, in degrees, a float.
#    6. The city's longitude, in degrees, a float.
# The format of the output file has the following fields, separated by commas:
#    1. The name of the city.
#    2. The city's population, an integer.
#    3. The city's latitude, in degrees, a float.
#    4. The city's longitude, in degrees, a float.

from city import City
from quicksort import sort
from string import lower

# Return True if city1 has a higher population than city2.
def compare_population(city1, city2):
    return city1.population > city2.population

# Return True if city1 comes at or before city2 alphbetically.
def compare_name(city1, city2):
    return lower(city1.city) <= lower(city2.city)

# Return True if city1's latitude is less than or equal to city2's latitude.
def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude

# Load a csv file and return a list of City objects.
def load_cities(filename):
    cities = []     # start with an empty list
    f = open(filename, 'r') # get ready to read

    for line in f:  # read each line
        fields = line.strip().split(',')    # separate its contents
        cities.append(City(fields[0], fields[1], fields[2], int(fields[3]),
                      float(fields[4]), float(fields[5])))

    f.close()   # done with the file
    return cities

# Write information about City objects to a file.
def write_cities(cities, filename):
    outfile = open(filename, "w")   # get ready to write
    i = 0
    while i < len(cities):
        outfile.write(str(cities[i]) + "\n")    # write the next City object
        i += 1

    outfile.close()     # done writing   

cities = load_cities("world_cities.txt")

# Sort by name.
sort(cities, compare_name)
write_cities(cities, "cities_alpha.txt")

# Sort by population.
sort(cities, compare_population)
write_cities(cities, "cities_population.txt")

# Sort by latitude
sort(cities, compare_latitude)
write_cities(cities, "cities_latitude.txt")

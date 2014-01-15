# city.py
# Class for information about a world city.
# Written by THC for CS 1 Lab Assignment #3.

class City:
    # Initialize all the instance variables for a City object.
    def __init__(self, country, city, region, population, latitude, longitude):
        self.country = country
        self.city = city
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    # Convert a City object to a string with the format
    # name,population,latitude,longitude
    def __str__(self):
        return self.city + "," + str(self.population) + \
            "," + str(self.latitude) + "," + str(self.longitude)

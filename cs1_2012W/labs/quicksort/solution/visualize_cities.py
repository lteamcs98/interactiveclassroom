# visualize_cities.py
# Written by THC visualize the 50 largest cities by population.
# Each city is drawn with a blinking red square and its name.
# After four rounds of blinks, the square turns solid orange.
# The name disappears when the next city is displayed.

from cs1lib import *
from math import *

WINDOW_WIDTH = 720      # world map image width, in pixels
WINDOW_HEIGHT = 360     # world map image height, in pixels
DOT_SIZE = 7            # size of each dot, in pixels
FONT_SIZE = 18          # font size for city names
X_CORRECTION = 4        # horizontal correction amount to display names
Y_CORRECTION = 10       # vertical correction amount to display names

# Make a red square blink four times at the given pixel location, specified
# by its center.
def blink_city(center_x, center_y):
    disable_stroke()    # no outline for the square
    for i in range(4):
            set_fill_color(1, 0, 0)     # red square
            draw_rectangle(center_x - (DOT_SIZE / 2), center_y - (DOT_SIZE / 2), DOT_SIZE, DOT_SIZE)
            request_redraw()
            sleep(0.1)
            set_fill_color(1, 1, 1)     # white square, erases the red square
            draw_rectangle(center_x - (DOT_SIZE / 2), center_y - (DOT_SIZE / 2), DOT_SIZE, DOT_SIZE)
            request_redraw()
            sleep(0.1)

# Draw an orange square at the given pixel location, specified by its center.
def draw_city(center_x, center_y):
    disable_stroke()
    set_fill_color(1, 0.5, 0)   # orange square
    draw_rectangle(center_x - (DOT_SIZE / 2), center_y - (DOT_SIZE / 2), DOT_SIZE, DOT_SIZE)

# Convert a latitude and longitude to pixel locations.
def longlat_to_pixel(latitude, longitude):
    center_x = int(round((WINDOW_WIDTH / 2) + (WINDOW_WIDTH / 2) * (longitude / 180)))
    center_y = int(round((WINDOW_HEIGHT / 2) + (WINDOW_HEIGHT / 2) * (latitude / 90)))
    return (center_x, center_y)

# Visualize the first n cities from a file.
def visualize_cities(filename, n, img):
    f = open(filename, 'r')     # open the file for reading
    set_stroke_color(0.5, 0, 1) # purple text
    set_font_size(FONT_SIZE)    # larger font than usual
    set_font_bold()             # and bold so that I can see it

    already_shown = []      # keep track of the cities shown so far
    for line in f:
        if len(already_shown) > n:
            break           # we've already shown n cities
        fields = line.strip().split(',')    # parse this line of input
        
        # Draw all cities that we've already shown.
        clear()
        draw_image(img, 0, 0)   # draw the map
        for city in already_shown:
            draw_city(city[0], city[1])
        
        # Now show the next city.  First, where in the image does it go?
        (center_x, center_y) = longlat_to_pixel(float(fields[2]), float(fields[3]))
        
        # Next, display the city name.
        enable_stroke()
        text_width = get_text_width(fields[0])
        draw_text(fields[0], center_x - (text_width / 2) - X_CORRECTION,
                   center_y + Y_CORRECTION)
        
        # Blink the city's square in red and then turn it solid orange. 
        blink_city(center_x, center_y)
        draw_city(center_x, center_y)
        
        request_redraw()
        sleep(0.25)

        # This city is now one that has already been shown.
        already_shown.append([center_x, center_y])

    f.close()   # done with the file
    
    # Redraw just the orange squares for all the cities.
    clear()
    draw_image(img, 0, 0)
    for city in already_shown:
        draw_city(city[0], city[1])
        
def main():
    img = load_image("world.png")
    visualize_cities("cities_population.txt", 50, img)
    request_redraw()
    
start_graphics(main, "The World", WINDOW_WIDTH, WINDOW_HEIGHT, True)

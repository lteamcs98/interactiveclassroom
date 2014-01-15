#  Simple photo display screensaver.
#  Devin Balkcom, March 2011.
#  Modified by THC.

from cs1lib import *
from random import randint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAME_CYCLE_LENGTH = 100
DELAY = 0.02
IMAGE_DURATION = 0.6    # fraction of time to display each image

def main():
    set_clear_color(0, 0, 0)    # black background
    clear()
    
    # Filenames for images.
    image_names = ["photo1.png", "photo2.png", "photo3.png",  "photo4.png"]
    
    # A list to store the addresses of loaded images.
    images = []
    
    for image_name in image_names:
        # Store the address of the loaded image object in img.
        img = load_image(image_name)
        images.append(img)
    
    # Keep track of how many frames have been drawn
    frame_counter = 0
    image_index = 0     # index of most recently displayed image

    while not window_closed():
        # Draw a new image every cycle.   
        if frame_counter == 0:
            clear()
            
            # Pick random pixel coordinates.
            x = randint(0, WINDOW_WIDTH / 2)
            y = randint(0, WINDOW_HEIGHT / 2) 
            
            # Draw the next image in the list, wrapping around.
            image_index = (image_index + 1) % len(images)
            draw_image(images[image_index], x, y)
            
        elif frame_counter < 0.6 * FRAME_CYCLE_LENGTH:
            # Redisplay the most recent image.
            draw_image(images[image_index], x, y)
            
        else:
            # Draw a black, nearly transparent rectangle to fade
            # the previous pictures out.
            set_fill_color(0, 0, 0, .05)
            draw_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        request_redraw()
        sleep(DELAY)
    
        frame_counter = (frame_counter + 1) % FRAME_CYCLE_LENGTH

start_graphics(main, "Photo screen saver", WINDOW_WIDTH, WINDOW_HEIGHT)

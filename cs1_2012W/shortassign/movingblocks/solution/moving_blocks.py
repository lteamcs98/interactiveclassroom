# moving_blocks.py
# Solution to CS 1 Short Assignment 6 by THC.
# Draws a window with dark red blocks on either side.
# Pressing the "a" key moves the left block up; "z" moves it down.
# Pressing the "k" key moves the right block up; "m" moves it down.
# No block is allowed to move above the top or below the bottom of
# the window.

from cs1lib import *

WINDOW_WIDTH = 400  # window width, in pixels
WINDOW_HEIGHT = 400 # window height, in pixels
    
def main():
    BLOCK_HEIGHT = 80   # block height, in pixels
    BLOCK_WIDTH = 20    # block width, in pixels
    
    # Key codes:
    LEFT_UP_KEY = "a"
    LEFT_DOWN_KEY = "z"
    RIGHT_UP_KEY = "k"
    RIGHT_DOWN_KEY = "m"
    
    BLOCK_MOVE_SPEED = 10   # how much a block moves per refresh cycle
    DELAY = 0.02            # how long each refresh cycle lasts
    
    # Initial locations of blocks.
    left_block_x = 0
    left_block_y = 0
    right_block_x = WINDOW_WIDTH - BLOCK_WIDTH
    right_block_y = WINDOW_HEIGHT - BLOCK_HEIGHT
    
    set_clear_color(1, 1, 0)    # yellow
    
    # Blocks are dark red, no outline.
    set_fill_color(0.5, 0, 0)
    disable_stroke()
    
    while not window_closed():
        # If "a" key is pressed and left block is not already at the top, move it up.
        if is_key_pressed(LEFT_UP_KEY) and left_block_y >= BLOCK_MOVE_SPEED:
            left_block_y = left_block_y - BLOCK_MOVE_SPEED
    
        # If "z" key is pressed and left block is not already at the bottom, move it down.
        if is_key_pressed(LEFT_DOWN_KEY) and left_block_y + BLOCK_HEIGHT <= WINDOW_HEIGHT - BLOCK_MOVE_SPEED:
            left_block_y = left_block_y + BLOCK_MOVE_SPEED
    
        # If "k" key is pressed and right block is not already at the top, move it up.
        if is_key_pressed(RIGHT_UP_KEY) and right_block_y >= BLOCK_MOVE_SPEED:
            right_block_y = right_block_y - BLOCK_MOVE_SPEED
    
        # If "m" key is pressed and right block is not already at the bottom, move it down.
        if is_key_pressed(RIGHT_DOWN_KEY) and right_block_y + BLOCK_HEIGHT <= WINDOW_HEIGHT - BLOCK_MOVE_SPEED:
            right_block_y = right_block_y + BLOCK_MOVE_SPEED
    
        # Draw the blocks.
        clear()
        draw_rectangle(right_block_x, right_block_y, BLOCK_WIDTH, BLOCK_HEIGHT)
        draw_rectangle(left_block_x, left_block_y, BLOCK_WIDTH, BLOCK_HEIGHT)
        
        # Refresh and take a brief nap.
        request_redraw()
        sleep(DELAY)

start_graphics(main, "Moving blocks", WINDOW_WIDTH, WINDOW_HEIGHT)

'''
Created on Sep 23, 2011

@author: devin
'''

from cs1lib import *

def draw_eyes():
    
    clear()
    
    # soften edges of lines
    enable_smoothing()

    # eyes (outside)
    disable_fill()
    enable_stroke()
    
    draw_circle(125, 100, 50)
    draw_circle(275, 100, 50)
  
    # eyes (iris)
    disable_stroke()  
    enable_fill()
    set_fill_color(0, 0, 0)
    
    draw_circle(135, 110, 20)
    draw_circle(265, 110, 20)

    # nose
    disable_fill()
    enable_stroke()
    set_stroke_width(2)
    set_stroke_color(0, 0, 0)

    draw_line(210, 175, 170, 250)
    draw_line(170, 250, 200, 250)
    
    # mouth
    disable_fill()
    enable_stroke()
    draw_rectangle(50, 320, 300, 20)
    

start_graphics(draw_eyes)

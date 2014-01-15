
# author:   Devin Balkcom
# credits:   Library design and initial opengl version of library
#            by Kelsey Harris, Zach Marois, Devin Balkcom
# date:     September 2011
#
# purpose:  procedural drawing, mouse, keyboard input library for CS 1 instruction

# Design note:  This file was originally split into cs1qt and cs1lib modules; that was probably a cleaner design, but I have combined the files for simplicity of installation.  (DJB)

# library version number
__version__ = 2.1

from PySide.QtCore import *
from PySide.QtGui import *
from time import time, sleep
from threading import Lock
from sys import exit, argv
import sys

from threading import Thread

class CS1Canvas(QWidget):
    
    def __init__(self, parent = None, width = 400, height = 400, flipped_y = True):
        QWidget.__init__(self, parent)
       
        self.width = width
        self.height = height
        self.setFixedSize(width, height)
        
        self.image = QImage(self.size(), QImage.Format_ARGB32_Premultiplied)
        self.image_painter = QPainter(self.image)
        #self.clear()
        
        self.lock_screen = Lock()
        self.lock_image = Lock()

        # keep track of a user thread.  If thread is stopped when window
        #  closed, terminate program
        self.user_thread = None
    
        self.window_closed = False
    
        self.flipped_y = flipped_y
        if flipped_y:
            self.scale(1, -1)
            self.translate(0, -self.height)
        
        self.font_name = "Arial"
        self.font_size = 14
        
        self.set_clear_color(1, 1, 1, 1)

        self.fill_enabled = True
        self.stroke_enabled = True

        self.stroke_width = 1
        self.set_stroke_color(0, 0, 0)
        self.set_fill_color(.7, .7, .7)
        
        self.setMouseTracking ( True )
        self.mousex = -1
        self.mousey = -1
        self.mouse_buttons = 0

        self.keys_down = {}
        self.last_keypress = ""

        # function to do nothing set as default user callback for mouse motion, button, keypress
        def nothing():
            pass

        self.mouse_motion_function = nothing
        self.mouse_button_function = nothing
        self.keypress_function = nothing
        

    def paintEvent(self, event):
        self.lock_screen.acquire()
        screen_painter = QPainter(self)

        screen_painter.drawImage(0, 0, self.image);

        screen_painter.end()
        self.lock_screen.release()
    
    def mouse_x(self):
        return self.mousex
        
    def mouse_y(self):
        if self.flipped_y:
            return self.height - self.mousey
        return self.mousey
        
    
    def set_clear_color(self, r, g, b, alpha = 1.0):
        self.clear_color = (r, g, b, alpha)

    def get_image_painter(self):
        self.lock_image.acquire()
        return self.image_painter

    def clear(self):
        with self.lock_image: 
            #imagePainter.setBackgroundMode(Qt.OpaqueMode)
            r = int(self.clear_color[0] * 255)
            g = int(self.clear_color[1] * 255)
            b = int(self.clear_color[2] * 255)
            a = int(self.clear_color[3] * 255)
            
            self.image_painter.setBackground( QBrush( QColor(r, g, b, a)))
            self.image_painter.eraseRect(self.image.rect());

    def draw_ellipse(self, x, y, rx, ry):
        with self.lock_image:
            self.image_painter.drawEllipse(QRectF(x - rx, y - ry, rx * 2, ry * 2)) 

    def enable_smoothing(self):
        with self.lock_image:
            self.image_painter.setRenderHint(QPainter.Antialiasing, True)
            self.image_painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

    def disable_smoothing(self):
        with self.lock_image:
            self.image_painter.setRenderHint(QPainter.Antialiasing, False)
            self.image_painter.setRenderHint(QPainter.SmoothPixmapTransform, False)

    def set_stroke_color(self, r, g, b, alpha = 1.0):
        self.pen_color = (r, g, b, alpha)
        if self.stroke_enabled:
            self.enable_stroke()

    def set_stroke_width(self, width):
        self.stroke_width = width
        if self.stroke_enabled:
            self.enable_stroke()

    def set_fill_color(self, r, g, b, alpha = 1.0):
        self.fill_color = (r, g, b, alpha)
        if self.fill_enabled:
            self.enable_fill()
 
    def enable_fill(self):
        self.fill_enabled = True
        with self.lock_image:
            r = int(self.fill_color[0] * 255)
            g = int(self.fill_color[1] * 255)
            b = int(self.fill_color[2] * 255)
            a = int(self.fill_color[3] * 255)
            self.image_painter.setBrush( QBrush( QColor(r, g, b, a)) ) 
    
    def disable_fill(self):
        self.fill_enabled = False
        with self.lock_image:
            self.image_painter.setBrush(Qt.NoBrush)

    def enable_stroke(self):
        self.stroke_enabled = True
        with self.lock_image:
            r = int(self.pen_color[0] * 255)
            g = int(self.pen_color[1] * 255)
            b = int(self.pen_color[2] * 255)
            a = int(self.pen_color[3] * 255)
            pen = QPen( QColor(r, g, b, a))
            pen.setWidth(self.stroke_width)
            self.image_painter.setPen( pen )
    
    def disable_stroke(self):
        self.stroke_enabled = False
        with self.lock_image:
            self.image_painter.setPen(Qt.NoPen)

    
    def set_font(self, font_name):
        self.font_name = font_name
        f = QFont(self.font_name, self.font_size, QFont.Normal)
        
        with self.lock_image:
            self.image_painter.setFont(f)

    def set_font_size(self, size):
        self.font_size = size
        f = QFont(self.font_name, self.font_size, QFont.Normal)
        
        with self.lock_image:
            self.image_painter.setFont(f)
            
    def set_font_bold(self):
        f = QFont(self.font_name, self.font_size, QFont.Bold)
        
        with self.lock_image:
            self.image_painter.setFont(f)
        
    
    def disable_smoothing(self):
        self.image_painter.setRenderHint(QPainter.Antialiasing, True)


    def rotate(self, angle):
        with self.lock_image:
            self.image_painter.rotate(angle)
        
    def translate(self, x, y):
        with self.lock_image:
            self.image_painter.translate(x, y)
        
    def scale(self, sx, sy):
        with self.lock_image:
            self.image_painter.scale(sx, sy)
        
    def save(self):
        with self.lock_image:
            self.image_painter.save()
    
    def restore(self):
        with self.lock_image:
            self.image_painter.restore()

       
    def draw_point(self, x, y):
        with self.lock_image:
            self.image_painter.drawPoint(x, y)

    def draw_polygon(self, vertices):
        with self.lock_image:
            qpoints = []
       
            for vertex in vertices:
                qpoints.append(QPoint(vertex[0], vertex[1]) )

            poly = QPolygonF(qpoints)
            self.image_painter.drawPolygon(poly)

    def draw_line(self, x1, y1, x2, y2):
        with self.lock_image:
            self.image_painter.drawLine(x1, y1, x2, y2)
     

    def draw_rectangle(self, x, y, w, h):
        with self.lock_image:    
            self.image_painter.drawRect(x, y, w, h)

    def draw_text(self, s, x, y):

        with self.lock_image:

            if self.flipped_y:
                self.image_painter.save()
                self.image_painter.translate(0, self.height)
                self.image_painter.scale(1, -1)
                self.image_painter.drawText(x, self.height - y, s)
                self.image_painter.restore()       

            else:
                self.image_painter.drawText(x, y, s)

    
    def draw_image(self, image, x, y):
        with self.lock_image:
         
            if self.flipped_y:
                self.image_painter.save()
                self.image_painter.translate(0, self.height)
                self.image_painter.scale(1, -1)
           
  #              self.image_painter.drawImage(x, self.height - y, image)
                self.image_painter.drawImage(x, self.height - y - image.height(), image)
                self.image_painter.restore()
            else:
                self.image_painter.drawImage(x, y, image)
            
         

    def get_text_width(self, str):
        f = QFont(self.font_name, self.font_size, QFont.Normal)
        fmetric = QFontMetrics(f)
        #return fmetric.boundingRect(str).width()
        return fmetric.width(str)

    def get_text_height(self):
        f = QFont(self.font_name, self.font_size, QFont.Normal)
        fmetric = QFontMetrics(f)
        #return fmetric.boundingRect(str).height()
        return fmetric.height()


    # Mouse and keyboard functions
        
    def set_mouse_button_function(self, func):
        self.mouse_button_function = func

    def set_mouse_motion_function(self, func):
        self.mouse_motion_function = func

    def set_keypress_function(self, func):
        self.keypress_function = func

    def mousePressEvent(self, event):
        self.mouse_buttons = event.buttons()
        self.mouse_button_function()

    def mouseReleaseEvent(self, event):
        self.mouse_buttons = event.buttons() 
        #print "Release", self.mouse_buttons

    def mouseMoveEvent(self, event):
        self.mousex = event.x()
        self.mousey = event.y()
        self.mouse_motion_function()
      
    def keyPressEvent(self, event):
        #print event.text()
        self.keys_down[event.text()] = True
        self.last_keypress = event.text()
        self.keypress_function()
        
    

    def start_thread(self, user_fn):
 
        user_thread = Thread(target = user_fn)
        user_thread.daemon = True
        self.user_thread = user_thread

        user_thread.start()
        
    def closeEvent(self, QCloseEvent):
        if self.user_thread.isAlive():
            #self.close_window.emit()
        
            QCloseEvent.ignore()
        
        self.window_closed = True
      #  print "window closed"
      
        
    def keyReleaseEvent(self, event):
        #print "released", event.text()
        self.keys_down[event.text()] = False

    def key_down(self, key_text):
        if not key_text in self.keys_down:
            return False
        return self.keys_down[key_text]

    def get_last_keypress(self):
        return self.last_keypress

    

class CS1Image(QImage):
    def get_pixel(self, x, y):
        p = self.pixel(x, y)
       
        r = qRed(p) / 255.0
        g = qGreen(p) / 255.0
        b = qBlue(p) / 255.0
        a = qAlpha(p) / 255.0
        
        return (r, g, b, a)

    def set_pixel(self, x, y, r, g, b, a = 1.0):
        ri  = int(r * 255)
        gi  = int(g * 255)
        bi  = int(b * 255)
        ai  = int(a * 255)
        
        qrgba = qRgba ( ri, gi, bi, ai )
        self.setPixel(x, y, qrgba)
        




# Global app and canvas 

app = QApplication(sys.argv)  
canvas = None

####

## transformations and canvas state functions

def push_state():
    canvas.save()
    
def pop_state():
    canvas.restore()
    
def rotate(degrees):
    canvas.rotate(degrees)
    
def translate(x, y):
    canvas.translate(x, y)

## Utility functions

def degrees(rad):
    return 180 * rad/ pi

## Setting state for drawing

def enable_smoothing():
    canvas.enable_smoothing()

def disable_smoothing():
    canvas.disable_smoothing()

def enable_fill():
    canvas.enable_fill()

def disable_fill():
    canvas.disable_fill()

def set_fill_color(r, g, b, alpha = 1.0):
    canvas.set_fill_color(r, g, b, alpha)

def set_clear_color(r, g, b, alpha = 1.0):
    canvas.set_clear_color(r, g, b, alpha)

def enable_stroke():
    canvas.enable_stroke()

def disable_stroke():
    canvas.disable_stroke()

def set_stroke_color(r, g, b, alpha = 1.0):
    canvas.set_stroke_color(r, g, b, alpha)

def set_stroke_width(width):
    canvas.set_stroke_width(width)

def set_font(font_name):
    canvas.set_font(font_name)

def set_font_size(font_size):
    canvas.set_font_size(font_size)
    
def set_font_bold():
    canvas.set_font_bold()


## Drawing commands ##

def clear():
    canvas.clear()

def draw_point(x, y):
    canvas.draw_point(x, y)

def draw_line(x1, y1, x2, y2):
    canvas.draw_line(x1, y1, x2, y2)

def draw_polygon(vertices):
    canvas.draw_polygon(vertices)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    draw_polygon([(x1, y1), (x2, y2), (x3, y3)])

def draw_circle(x, y, r):
    draw_ellipse(x, y, r, r)

def draw_ellipse(x, y, rx, ry):
    assert rx >= 0
    assert ry >= 0

    canvas.draw_ellipse(x, y, rx, ry)

def draw_rectangle(x, y, w, h):
    canvas.draw_rectangle(x, y, w, h)

def draw_text(string, x, y, centered = False, centered_x = False, centered_y = False):
    if centered:
        centered_x = True
        centered_y = True
        
    if centered_x:
        w = get_text_width(string)
        x -= int(w / 2.0 + .5)
    
    if centered_y:
        h = get_text_height(string)
        y += int(h / 2.0) - 2
            
    canvas.draw_text(string, x, y)

def get_text_width(string):
    return canvas.get_text_width(string)

def get_text_height(string = None):
    return canvas.get_text_height()

   
## Images

def draw_image(image, x, y, cx = 0, cy = 0, theta = 0):
    push_state()
    translate(x - cx, y - cy)
     
    if theta != 0:
    
        translate(cx, cy)
        rotate(theta)
        translate(-cx, -cy)     
        
    canvas.draw_image(image, 0, 0)
        
    pop_state()
 

def load_image(filename):
    img = CS1Image()
    img.load(filename)
    return img

## Mouse events

def mouse_x():
    return canvas.mouse_x()

def mouse_y():
    return canvas.mouse_y()

def mouse_down():
    return canvas.mouse_buttons != 0

def mouse_button_pressed(buttons):
    return canvas.mouse_buttons

# Set up a callback function for mouse clicks
def set_mouse_button_function(func):
    canvas.set_mouse_button_function(func)

def set_mouse_motion_function(func):
    canvas.set_mouse_motion_function(func)
    
def set_keypress_function(func):
    canvas.set_keypress_function(func)

# Returns true if the key passed (as a string) is currently pressed
def is_key_pressed(key_text):
    return canvas.key_down(key_text)

def get_last_keypress():
    return canvas.get_last_keypress()
    
    
def set_frame_rate(frame_rate):
    canvas.set_frame_rate(frame_rate)

# request a redraw.  Required to force graphics to display 
def request_redraw():
    canvas.update()



# cs1_create_canvas can only be called in the main thread; i.e, before
#  start_graphics is called.  cs1_create_canvas should not be called directly.

def create_canvas(title = "cs1", width = 400, height = 400, flipped_y = False):
   
    c = CS1Canvas(None, width, height, flipped_y)
    c.setWindowTitle(title)
    c.show()
    c.raise_()

    global canvas
    canvas = c
    
    return c

def window_closed():
    return canvas.window_closed


 

def start_graphics(user_fn = None, title = "cs1", width = 400, height = 400, flipped_y = False):
    
    if canvas is None:
        create_canvas(title, width, height, flipped_y)  
    

    # make sure that when the user function has finished, the program
    #  quits, if the graphics window has also been closed
    def wrapped_user_fn():
        user_fn()
        request_redraw()
        
        if window_closed():
            cs1_quit()


    canvas.start_thread(wrapped_user_fn)
    exit(app.exec_())


def cs1_quit():
    app.quit()
    exit()

if __name__ == "__main__":
    from time import sleep
    
    def test_fn():

        x = 5
    
        robot_img = load_image("create_robot.png")
    
        enable_smoothing()
        
        while not window_closed():
            
            if is_key_pressed(" "):
                print "space pressed"
            
            # do the drawing for the current frame
            clear()
         
            draw_image(robot_img, 200, 200, robot_img.width()/2, robot_img.height()/ 2, x)
        
            draw_circle(x, 30, 20)
            draw_text("Test", 30, 10)
        
            # change the state for the next frame
            x += 1
            
            # move the current frame to the screen
            request_redraw()
            sleep(.02)
        

    start_graphics(test_fn, "cs1", 600, 600, flipped_y = True)


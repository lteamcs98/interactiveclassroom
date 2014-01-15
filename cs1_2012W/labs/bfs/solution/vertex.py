# vertex.py
# Emily Freebairn
# November 17, 2011
# Minor changes by THC.
# The Vertex class represents a vertex in a graph.  It stores the vertex's location,
# and a list of the vertices that are adjacent to it.  It also stores the vertex's
# name, so that it can be displayed (extra-credit feature).

from cs1lib import *

RADIUS = 8      # RADIUS of the drawn vertices
LINE_WIDTH = 3  # line width of the drawn edges
X_CORRECTION = 4        # horizontal correction amount to display names
Y_CORRECTION = 10       # vertical correction amount to display names

class Vertex:
    # Initialize a Vertex, given its location.
    def __init__(self, name, x, y):
        self.name = name    # name of this vertex (for extra credit)
        self.x = x          # x location of the vertex in pixels
        self.y = y          # y location of the vertex in pixels
        self.adjacent = []  # list of adjacent vertices
    
    # Draw the vertex with the color parameters given.
    def draw(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        draw_circle(self.x, self.y, RADIUS)
    
    # Draw the edge between self and the vertex given as a parameter,
    # in the color determined by the parameters.
    def draw_edge(self, vertex, r, g, b):
        enable_stroke()
        set_stroke_width(LINE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)
    
    # Draw all the edges between a vertex and the vertices in its adjacency list,
    # in the color determined by the parameters.
    def draw_neighbor_edges(self, r, g, b):
        for adjacent_vertex in self.adjacent:
            self.draw_edge(adjacent_vertex, r, g, b)
            
    # Display this vertex's name in the color determined by the parameters.
    # (Extra-credit feature.)
    def show_name(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_font_size(18)
        set_font_bold()
        text_width = get_text_width(self.name)
        draw_text(self.name, self.x - text_width/2 - X_CORRECTION,
                  self.y - Y_CORRECTION)
    
    # Determine whether the point (x, y) is in the box inscribing the vertex's circle.
    def is_point_near_vertex(self, x, y):
        return abs(self.x - x) <= RADIUS and abs(self.y - y) <= RADIUS

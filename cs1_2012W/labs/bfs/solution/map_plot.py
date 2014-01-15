# map_plot.py
# Emily Freebairn
# November 17, 2011
# Minor changes by THC.
# Creates an interactive map of Dartmouth campus so that you can find a short path
# between common locations.  Uses breadth-first-search.  
#
# To use: Click on a vertex on the map.  That will become your start vertex.  Hover your mouse
# over any other vertex in the map and you will see a red path from the start to the vertex you
# are hovering over.  To pick a different start, click somewhere else.

from cs1lib import *
from graph_load import load_graph
from bfs import bfs

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

def main():
    # Start and goal vertices for BFS.
    start = None
    goal = None
    
    vertex_dict = load_graph("dartmouth_graph.txt") # dictionary of vertices
    image = load_image("dartmouth_map.png")         # image of map_plot
    
    enable_smoothing()
    
    while not window_closed():
        draw_image(image, 0, 0)     # draw the map
        
        # Draw each vertex and the edges between each vertex and its neighbors.
        for key in vertex_dict:
            vertex_dict[key].draw_neighbor_edges(0, 0, 1)   # draw in blue
            vertex_dict[key].draw(0, 0, 1)
                  
        # Find a vertex near the current mouse location.
        found = None 
        for key in vertex_dict:
            if vertex_dict[key].is_point_near_vertex(mouse_x(), mouse_y()):
                found = vertex_dict[key]
                break # we've found the vertex, so we don't need to keep going through the loop
        
        # If the mouse button is down, change the start vertex to whatever is found;
        # could be None.
        if mouse_down(): 
            start = found
        
        # If there is a start vertex has a value, draw it in red, and set the goal
        # (goal could be None!)  
        if start != None:
            start.draw(1, 0, 0)     # draw in red
            goal = found
    
        if start != None and goal != None:  # we have a genuine search!
            path = bfs(start, goal)
            
            # Draw the path from the goal back to the start in blue.
            previous = goal
            for vertex in path:
                vertex.draw(1, 0, 0)
                vertex.draw_edge(previous, 1, 0, 0) 
                previous = vertex
                
            # Show the names of the start and goal vertices in purple.
            # (Extra-credit feature.)
            start.show_name(0.5, 0, 1)
            goal.show_name(0.5, 0, 1)
                
        request_redraw()
        sleep(.02)
      
start_graphics(main, "Map of Dartmouth", WINDOW_WIDTH, WINDOW_HEIGHT)
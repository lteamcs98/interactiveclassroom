# graph_load.py
# Emily Freebairn
# November 17, 2011
# Minor changes by THC.
# Defines the function load_graph, which loads a graph from the information
# stored in a file into a dictionary for further use.
from vertex import Vertex

# Parse the file containing vertex information, construct the graph, and 
# return a dictionary containing all the vertices keyed with their names.     
def load_graph(file_name):
    graph_file = open(file_name, 'r')   # open the file for reading

    # Put the lines from the file into a list for easy access.
    graph_info = []
    for line in graph_file:
        graph_info.append(line)
    
    graph_file.close()
    
    vertex_dict = {}    # dictionary storing the vertices
    
    # First pass through the file: make the vertices and save their locations.
    for line in graph_info:
        semi_list = line.split(";") 
        key = semi_list[0].strip()  # key is the name of the vertex
        
        location = semi_list[2].split(",")  # get the x and y location
        
        # Location is a list of two strings.  Strip the strings and then
        # convert them to integers for the vertex.
        vertex_dict[key] = Vertex(key, int(location[0].strip()), int(location[1].strip()))
        
    # Second pass through the file: set up the adjacency lists for the vertices.
    for line in graph_info:
        semi_list = line.split(";")
        key = semi_list[0].strip()  # get the name of the vertex
        
        # Split the adjacency part into a list of strings, where each string
        # is the name of a vertex adjacent to the vertex named by the key.
        adj_key_list = semi_list[1].split(",")
        for adj_key in adj_key_list:
            # Add the vertex named by the adj_key to the key vertex's adjacency list.
            vertex_dict[key].adjacent.append(vertex_dict[adj_key.strip()])
    
    return vertex_dict

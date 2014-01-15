# bfs.py
# Emily Freebairn
# November 17, 2011
# Minor changes by THC.
# Runs breadth-first-search using the Vertex class.

from vertex import Vertex
from collections import deque

# Run bfs and finds the path from the Vertex start to the Vertex goal.
# Return that path as a list of vertices. If there is no path, return None.
def bfs(start, goal):
    visited = {}        # the dictionary of vertices we've visited so far
    frontier = deque()  # the queue of vertices we're going to visit next
    
    frontier.append(start)  # put the start vertex in our list of those to visit
    
    backpointer = {}
    backpointer[start] = None   # the start vertex has no backpointer

    # Keep going while there's at least one visited vertex that we have not
    # explored from yet.
    while len(frontier) > 0: 
        vertex = frontier.popleft()
        visited[vertex] = True  # mark that we've visited the vertex
        
        if vertex == goal: 
            # If we're done, retrace the path from the goal to the start.
            path = []        
            while vertex != None: # only our start should have a None backpointer along our path
                path.append(vertex)
                vertex = backpointer[vertex]
            return path
        
        else:   # keep exploring
            for neighbor in vertex.adjacent:
                # Visit the vertex only if it hasn't been visited yet and if
                # it's not already in the frontier.
                if not neighbor in visited and not neighbor in frontier:
                    # Set up the backpointer.  This will only happen once for each vertex, 
                    # since a vertex is put in the frontier and visited only once.
                    backpointer[neighbor] = vertex
                    frontier.append(neighbor) 
                    
    # If we get here, we've run out of vertices to explore before reaching the goal.
    return None
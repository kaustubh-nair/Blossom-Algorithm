import networkx as nx
import time

from .helpers import update, update_colors

def find_free_vertices(g):
    free_vertices = []
    return free_vertices

def pick_random(free_vertices):
    return random_vertex

def BFS(g, random_vertex):
    return next_free_vertex, vertices #all the vertices in between the random vertex and the final free vertex

def augmenting_path(g, random_vertex, vertices, next_free_vertex):
    return    

def invert_augmenting_path(g, random_vertex, vertices, next_free_vertex):
    return edges

def update_graph(g, matching):
    return g #To update the new matches vertices

# Algorithm goes here
def run(g, colors, animation_data):
    matching = []
    free_vertices = find_free_vertices(g)

    while(len(free_vertices) != 0):

        #start with displaying the graph g 
        update(animation_data, g, colors)

        free_vertices = find_free_vertices(g)
        # color all free vertices
        update(animation_data, g, colors)

        random_vertex = pick_random(free_vertices)
        # highlight the chosen random vertex
        update(animation_data, g, colors)

        next_free_vertex, vertices = BFS(g, random_vertex)
        # highlight the next free vertex
        # this step can be further subdivided -- showing all animations till finding the next free vertex
        # also add the blossom part in this
        update(animation_data, g, colors)

        augmenting_path(g, random_vertex, vertices, next_free_vertex)
        # highlight the entire augmenting path
        update(animation_data, g, colors)

        edges = invert_augmenting_path(g, random_vertex, vertices, next_free_vertex)
        matching.append(edges)
        # highlight the inverted augmenting path
        update(animation_data, g, colors)

        g = update_graph(g, matching)
        free_vertices = find_free_vertices(g)

    #display final matching
    update(animation_data, g, colors)

    return animation_data

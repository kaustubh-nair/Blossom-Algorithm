import networkx as nx
import time, random
import numpy as np

from .helpers import (
    update, update_vertex_color, update_edge_color,
    update_multiple_vertex_color,
    update_multiple_edge_color, get_index
)

def find_free_vertices(g):
    free_vertices = []
    for n in g.nodes():
        if g.nodes[n]["matched"] is False:
            free_vertices.append(n)
    return free_vertices

def pick_random(free_vertices):
    random_vertex = random.choice(free_vertices)
    return random_vertex

def bfs(g, root):
    visited = [False] * (max(g.nodes) + 1)
    queue = []
    queue.append(root)
    visited[root] = True
    visit_arr = []

    while queue:
        root = queue.pop(0)
        visit_arr.append(root)
        for i in g.neighbors(root):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return visit_arr

def find_next_free_node(g, bfs_arr):
    for i in range(1, len(bfs_arr)-1):
        index = get_index(g, bfs_arr[i])
        if g.nodes[index]["matched"] is False:
            g.nodes[index]["matched"] = True
            return [None], index

        if g.nodes[index]["matched"] is True:
            # Add its other matched vertex
            index1 = get_index(g, bfs_arr[i+1])
            if g.nodes[index1]["matched"] is False:
                g.nodes[index1]["matched"] = True
                return [None], index1
            
def blossom(g, index0, vertices, index2):
    g.nodes[index0]["blossom"] = True
    g.nodes[index2]["blossom"] = True
    for vertex in vertices:
        index = get_index(g, vertex)
        g.nodes[index]["blossom"] = True
    node_list = []
    for node in g.nodes():
        index = get_index(g, node)
        if g.nodes[index]["blossom"] == False :
            node_list.append(index)
    node_list.append(index0) #Node subsuming blossom
    g_new = g.subgraph(node_list)
    return g_new

def get_aug_path(g, random_vertex, next_free_node):
    index1 = get_index(g, random_vertex)
    index2 = get_index(g, next_free_node)
    node_list = [index1, index2]
    aug_path = g.subgraph(node_list)
    return aug_path

def get_invert_aug_path(g, aug_path):
    if len(aug_path) == 1: return aug_path
    else: return aug_path 

def update_nodes(g, invert_aug_path):
    for edge in invert_aug_path.edges():
        node1, node2 = edge 
        index1 = get_index(g, node1)
        g.nodes[index1]["matched"] = True
        index2 = get_index(g, node2)
        g.nodes[index2]["matched"] = True
        return

def run(g, colors, animation_data):
    max_matching = []
    free_vertices = find_free_vertices(g)

    while len(free_vertices) > 0:
        update_multiple_vertex_color(colors, g.nodes(), "blue")
        free_vertices = find_free_vertices(g)
        update_multiple_vertex_color(colors, free_vertices, "yellow")
        update(animation_data, g, colors)
        # Yellow is the color of free vertices

        random_vertex = pick_random(free_vertices)
        update_multiple_vertex_color(colors, g.nodes(), "blue")
        update_vertex_color(colors, random_vertex, "red")
        update(animation_data, g, colors)
        # Red is the color of randomly chosen vertex among free vertices

        bfs_arr = bfs(g, random_vertex)
        ret = find_next_free_node(g, bfs_arr)
        _, next_free_node = ret
        update_vertex_color(colors, next_free_node, "red")
        update(animation_data, g, colors)
        # Red is also the color of next unmatched vertex closest to random vertex

        aug_path = get_aug_path(g, random_vertex, next_free_node)
        update_multiple_edge_color(colors, aug_path.edges(), "yellow")
        update(animation_data, g, colors)
        # Yellow is the color of initial augmenting path

        invert_aug_path = get_invert_aug_path(g, aug_path)
        update_multiple_edge_color(colors, invert_aug_path.edges(), "green")
        update(animation_data, g, colors)
        # Green is the color of final augmenting path

        update_nodes(g, invert_aug_path)
        max_matching.append(invert_aug_path.edges())
        free_vertices = find_free_vertices(g)

    update(animation_data, g, colors)
    # Red is the color of final augmenting path

    return animation_data

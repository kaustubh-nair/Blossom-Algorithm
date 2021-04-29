from copy import deepcopy

def get_vertex_colors(c, g):
    return [c[e] for e in g.nodes()]

def get_edge_colors(c, g):
    return [c[e] for e in g.edges()]

def update(animation_data,  g, colors):
    animation_data['interim_graphs'].append(g.copy())
    animation_data['interim_colors'].append(deepcopy(colors))

def update_edge_color(colors, u, v, color):
    colors['edges'][tuple(sorted([u, v]))] = color

def update_vertex_color(colors, u, color):
    colors['vertices'][u] = color

def update_multiple_edge_color(colors, edges, color):
    for u, v in edges:
        colors['edges'][tuple(sorted([u, v]))] = color

def update_multiple_vertex_color(colors, verts, color):
    for u in verts:
        colors['vertices'][u] = color

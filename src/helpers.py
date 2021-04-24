from copy import deepcopy

def get_colors(c, g):
    return [c[e] for e in g.edges()]

def update(animation_data,  g, colors):
    animation_data['interim_graphs'].append(g.copy())
    animation_data['interim_colors'].append(deepcopy(colors))

def update_colors(colors, u, v, color):
    colors[tuple(sorted([u, v]))] = color

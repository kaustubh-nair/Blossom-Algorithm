import networkx as nx
import time

from .helpers import update, update_colors

# Algorithm goes here
def run(g, colors, animation_data):

    # Make sure to update graph after every important step, which should be shown in animation.
    g.remove_edge(1, 2)
    update(animation_data, g, colors)

    g.remove_edge(3, 2)
    update(animation_data, g, colors)

    g.remove_edge(3, 1)
    update(animation_data, g, colors)

    g.remove_edge(4, 5)
    update(animation_data, g, colors)

    update_colors(colors, 3, 4, 'green')
    update(animation_data, g, colors)

    update_colors(colors, 1, 4, 'red')
    update(animation_data, g, colors)

    update_colors(colors, 2, 4, 'yellow')
    update(animation_data, g, colors)

    update_colors(colors, 8, 9, 'blue')
    update(animation_data, g, colors)

    return animation_data

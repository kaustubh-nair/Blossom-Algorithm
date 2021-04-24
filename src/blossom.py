import networkx as nx
from copy import deepcopy
import time

# Algorithm goes here
def run(g, interim_graphs):
    update(interim_graphs, g)

    # Make sure to update graph after every important step, which should be shown in animation.
    g.remove_edge(1, 2)
    update(interim_graphs, g)

    g.remove_edge(3, 2)
    update(interim_graphs, g)

    g.remove_edge(3, 1)
    update(interim_graphs, g)

    g.remove_edge(4, 5)
    update(interim_graphs, g)


    return interim_graphs


def update(interim_graphs, g):
    interim_graphs.append(g.copy())

import networkx as nx
from copy import deepcopy
import matplotlib.pyplot as plt

from src import blossom, sample_graphs, helpers


g = sample_graphs.complete()
pos = nx.spring_layout(g)
c = {}

for edge in g.edges():
    c[tuple(sorted(edge))] = 'grey'


animation_data = {
            'interim_graphs': [g.copy()],
            'interim_colors': [deepcopy(c)],
    }
blossom.run(g, c, animation_data)


index = 1
def press(event):
    global index
    graphs = animation_data['interim_graphs']
    if event.key == 'enter' and index < len(graphs):
        fig.clear()
        nx.draw(graphs[index],
                pos=pos,
                edge_color=helpers.get_colors(animation_data['interim_colors'][index],
                                              graphs[index]),
                width=2.0,
        )
        index += 1
        fig.canvas.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', press)
fig.clear()
nx.draw(animation_data['interim_graphs'][0],
        pos=pos,
        edge_color=helpers.get_colors(animation_data['interim_colors'][0],
                                      animation_data['interim_graphs'][0]),
        width=2.0,
)
plt.show()

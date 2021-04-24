import matplotlib.pyplot as plt
import networkx as nx

from src import sample_graphs

g = sample_graphs.diamond()
g1 = sample_graphs.peterson()


def press(event):
    print('[DEBUG] pressed', event.key)
    if event.key == 'enter':
        fig.clear()
        nx.draw(g1)
        fig.canvas.draw()

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)

nx.draw(g)
plt.show()

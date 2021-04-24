import matplotlib.pyplot as plt
import networkx as nx

from src import sample_graphs

g = sample_graphs.diamond()

nx.draw(g)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt


from src import blossom, sample_graphs

g = sample_graphs.complete()
pos = nx.spring_layout(g)

interim_graphs = blossom.run(g, [])

index = 1
def press(event):
    global index
    if event.key == 'enter' and index < len(interim_graphs):
        fig.clear()
        nx.draw(interim_graphs[index], pos=pos)
        index += 1
        fig.canvas.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', press)
fig.clear()
nx.draw(interim_graphs[0], pos=pos)
plt.show()

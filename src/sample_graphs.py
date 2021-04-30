import networkx as nx

def random():
    return nx.random_geometric_graph(100, 0.120)

def graph1():
    return nx.erdos_renyi_graph(20, 0.4)

def peterson():
    return nx.petersen_graph()

def diamond():
    return nx.diamond_graph()

def empty():
    return nx.empty_graph(10)

def path():
    return nx.path_graph(8)

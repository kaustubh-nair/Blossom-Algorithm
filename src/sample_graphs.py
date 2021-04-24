import networkx as nx

def random():
    return nx.random_geometric_graph(100, 0.120)

def complete():
    return nx.complete_graph(30)

def graph1():
    return nx.erdos_renyi_graph(20, 0.4)

def peterson():
    return nx.petersen_graph()

def diamond():
    return nx.diamond_graph()

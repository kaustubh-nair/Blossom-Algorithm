import networkx as nx
import time

from .helpers import update, update_colors


class Node:

    def __init__(self):
        self.neighbors = []
        self.is_visited = False
        self.parent = None
        self.mate = None
        self.index = Node.index
        Node.index += 1

    def __repr__(self):
        return str(self.index)


class SuperNode(Node):

    def __init__(self):
        Node.__init__(self)
        self.subnodes = []
        self.original_edges = []

    def cycle(self, node):
        for i, v in enumerate(self.subnodes):
            if v == node:
                break

        if (i > 0 and self.subnodes[i].mate == self.subnodes[i - 1] or i == 0 and self.subnodes[i].mate ==
                self.subnodes[-1]):
            return self.subnodes[i::-1] + self.subnodes[:i:-1]
        else:
            return self.subnodes[i::] + self.subnodes[:i]


class Match:

    def __init__(self, nodes):
        self.nodes = nodes
        self.unmarked_nodes = []
        for node in nodes:
            self.unmarked_nodes.append(node)
        self.supernodes = []

    # Make a super node, 2 arrays for the original edges(original_edges) and blossom edges(subnodes) are created.
    # Necessary Manipulation are made for the neighbours of blossom
    @staticmethod
    def shrink_blossom(blossom):
        snode = SuperNode()
        for node in blossom:
            snode.subnodes.append(node)
            for adj_node in node.neighbors:
                if adj_node not in blossom:
                    snode.original_edges.append((node, adj_node))

        for node1, node2 in snode.original_edges:
            node1.neighbors.remove(node2)
            node2.neighbors.remove(node1)
            node2.neighbors.append(snode)
            snode.neighbors.append(node2)

        return snode

    # expands the blossom with necessary manipulation on the neighbours
    @staticmethod
    def expand_blossom(snode):
        for node1, node2 in snode.original_edges:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
            node2.neighbors.remove(snode)
            snode.neighbors.remove(node2)

    @staticmethod
    def ancestors(node):
        ancestors_list = [node]
        while node.parent is not None:
            node = node.parent
            ancestors_list.append(node)
        return ancestors_list

    @staticmethod
    def find_cycles(self, node_a, node_b):
        list_ancestor_node_a = self.ancestors(node_a)
        list_ancestor_node_b = self.ancestors(node_b)
        i = len(list_ancestor_node_a) - 1
        j = len(list_ancestor_node_b) - 1

        while list_ancestor_node_b[i] == list_ancestor_node_b[j]:
            i -= 1
            j -= 1
        return list_ancestor_node_a[:i + 1] + list_ancestor_node_b[j + 1::-1]

    # def construct_augmenting_path(self, node):

    def bfs_blossom(self, root):
        queue = [root]
        while len(queue) != 0:
            cur_node = queue.pop(0)
            cur_node.is_Visited = True
            for v in cur_node.neighbors:
                if v.is_Visited is False and v.mate is not None:
                    v.is_Visited = True
                    v.mate.is_Visited = True
                    v.parent = cur_node
                    v.mate.parent = v
                    queue.append(v.mate)
                elif v.is_Visited:
                    cycle = self.find_cycles(v, cur_node)
                    if len(cycle) % 2 != 1:
                        continue
                    else:
                        snode = self.shrink_blossom(cycle)
                        self.supernodes.append(snode)
                        for node in cycle:
                            if node in queue:
                                queue.remove(node)
                            if node.is_Visited:
                                snode.is_visited = True
                                snode.parent = node.parent
                        queue.append(snode)
                        break
                else:
                    if v.mate is None:
                        v.parent = cur_node
                        return self.construct_augmenting_path(v)




def find_free_vertices(g):
    free_vertices = []
    return free_vertices

def pick_random(free_vertices):
    return random_vertex

def BFS(g, random_vertex):
    return next_free_vertex, vertices #all the vertices in between the random vertex and the final free vertex

def augmenting_path(g, random_vertex, vertices, next_free_vertex):
    return

def invert_augmenting_path(g, random_vertex, vertices, next_free_vertex):
    return edges

def update_graph(g, matching):
    return g #To update the new matches vertices

# Algorithm goes here
def run(g, colors, animation_data):
    matching = []
    free_vertices = find_free_vertices(g)

    while(len(free_vertices) != 0):

        #start with displaying the graph g 
        update(animation_data, g, colors)

        free_vertices = find_free_vertices(g)
        # color all free vertices
        update(animation_data, g, colors)

        random_vertex = pick_random(free_vertices)
        # highlight the chosen random vertex
        update(animation_data, g, colors)

        next_free_vertex, vertices = BFS(g, random_vertex)
        # highlight the next free vertex
        # this step can be further subdivided -- showing all animations till finding the next free vertex
        # also add the blossom part in this
        update(animation_data, g, colors)

        augmenting_path(g, random_vertex, vertices, next_free_vertex)
        # highlight the entire augmenting path
        update(animation_data, g, colors)

        edges = invert_augmenting_path(g, random_vertex, vertices, next_free_vertex)
        matching.append(edges)
        # highlight the inverted augmenting path
        update(animation_data, g, colors)

        g = update_graph(g, matching)
        free_vertices = find_free_vertices(g)

    #display final matching
    update(animation_data, g, colors)

    return animation_data

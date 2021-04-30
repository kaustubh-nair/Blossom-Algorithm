import networkx as nx
import time, random

from .helpers import (
    update, update_vertex_color, update_edge_color,
    update_multiple_vertex_color,
    update_multiple_edge_color,
)


class Match:

    def __init__(self, g, free_vertices, colors, animation_data):
        self.g = g
        self.colors = colors
        self.animation_data = animation_data
        self.nodes = free_vertices
        # self.unmarked_nodes = []
        # for node in nodes:
        #     self.unmarked_nodes.append(node)
        self.supernodes = []

    def replace_head(self, node_list):
        # assert isinstance(self.nodes[0], SuperNode)
        su_node = node_list.pop(0)
        for node in su_node.subnodes:
            if node_list[0] in self.g.neighbors(node):
                if self.g.nodes[node]["mate"] is None:
                    node_list.insert(0, node)
                else:
                    for v in su_node.circle(node):
                        node_list.insert(0, v)

                return "cannot replace head node."

    def replace_tail(self, node_list):
        # assert isinstance(self.nodes[-1], SuperNode)
        su_node = node_list.pop()
        for node in g.nodes[su_node].subnodes:
            if node_list[-1] in self.g.neighbors(node):
                if self.g.nodes[node]["mate"] is None:
                    node_list.append(node)
                else:
                    for v in su_node.circle(node):
                        node_list.append(v)
                return "cannot replace tail node."

    def clear_nodes(self):
        for node in self.nodes:
            self.g.nodes[node]["is_Visited"] = False
            self.g.nodes[node]["parent"] = None

    def construct_augmenting_path(self, node):
        # self.clear_nodes()
        node_list = [node, self.g.nodes[node]["parent"]]
        while self.g.nodes[node]["mate"] is not None:
            node = self.g.nodes[node]["parent"]
            node_list.append(node)

        while len(self.supernodes) > 0:
            su_node = self.supernodes.pop()
            if su_node == node_list[0]:
                self.replace_head()
            elif su_node == node[-1]:
                self.replace_tail()
        while self.g.nodes[node_list[0]]["mate"] is not None:
            node_list.insert(self.g.node[node_list[0]]["parent"], 0)
        while self.g.nodes[node_list[-1]]["mate"] is not None:
            node_list.append(self.g.nodes[node_list[-1]]["parent"])
        # aug_path_subgraph = self.g.subgraph(node_list)

        return node_list

    def bfs_blossom(self, root):
        queue = [root]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            self.g.nodes[cur_node]["is_Visited"] = True

            if self.g.nodes[cur_node]["parent"] is not None:
                update_edge_color(self.colors, self.g.nodes[cur_node]["parent"], cur_node, "blue")
            update_vertex_color(self.colors, cur_node, "red")
            update(self.animation_data, self.g, self.colors)
            # cur_node.is_Visited = True
            for v in [x for x in self.g.neighbors(cur_node)]:
                print(cur_node)
                print([x for x in self.g.neighbors(cur_node)])
                if v == self.g.nodes[cur_node]["parent"]:
                    continue
                if self.g.nodes[v]["is_Visited"] is False and self.g.nodes[v]["mate"] is not None:
                    self.g.nodes[v]["is_Visited"] = True
                    self.g.nodes[self.g.nodes[v]["mate"]]["is_Visited"] = True
                    self.g.nodes[v]["parent"] = cur_node
                    self.g.nodes[self.g.nodes[v]["mate"]]["parent"] = v
                    queue.append(self.g.nodes[v]["mate"])

                elif self.g.nodes[v]["is_Visited"]:
                    # cycle = self.find_cycles(v, cur_node)
                    try:
                        cycle = list(nx.find_cycle(self.g, v))
                    except Exception as e:
                        print("NO CYCLE FOUND!!!")
                        break
                    blossom = self.g.subgraph(cycle)
                    update_multiple_edge_color(self.colors, cycle, "red")
                    update(self.animation_data, self.g, self.colors)
                    if len(cycle) % 2 != 1:
                        continue
                    else:
                        su_node = max(self.g.nodes) + 1
                        subnodes = []
                        original_edges = []
                        su_node_attr = {su_node: {"is_Visited": False, "mate": None, "parent": None,
                                                  "subnodes": subnodes, "original_edges": original_edges}}

                        self.g.add_node(su_node)
                        nx.set_node_attributes(self.g, su_node_attr)

                        for n in blossom.nodes:
                            self.g.nodes[su_node]["subnodes"].append(n)
                            nbrs = set(self.g.neighbors(n))
                            queue.remove(n)
                            if self.g.nodes[n]["is_Visited"]:
                                self.g.nodes[su_node]["is_Visited "] = True
                                self.g.nodes[su_node]["parent"] = self.g.nodes[n]["parent"]
                            for nbr in nbrs - {blossom.nodes}:
                                self.g.add_edge(su_node, nbr)
                                update_edge_color(self.colors, su_node, nbr, "black")
                            self.g.remove_node(n)
                        update_vertex_color(self.colors, su_node, "black")
                        update(self.animation_data, self.g, self.colors)
                        self.supernodes.append(su_node)
                        queue.append(su_node)
                        break
                else:
                    if self.g.nodes[v]["mate"] is None:
                        self.g.nodes[v]["parent"] = cur_node
                        node_list = self.construct_augmenting_path(v)
                        aug_path_subgraph = self.g.subgraph(node_list)
                        return aug_path_subgraph

    def invert_aug_path(self, aug_path):
        assert len(aug_path.nodes) % 2 == 0
        inv_aug_path = list(aug_path.nodes)
        inv_aug_path_edge = []
        for i in range(0, len(inv_aug_path), 2):
            self.g.nodes[i]["mate"] = i+1
            self.g.nodes[i + 1]["mate"] = i
            inv_aug_path_edge.append([i, i + 1])
        return inv_aug_path_edge


def find_free_vertices(g):
    free_vertices = []
    for n in g.nodes():
        if g.nodes[n]["mate"] is None:
            free_vertices.append(n)
    return free_vertices


def pick_random(free_vertices):
    random_vertex = random.choice(free_vertices)
    return random_vertex


# Algorithm goes here
def run(g, colors, animation_data):
    # max_matching = []
    free_vertices = find_free_vertices(g)

    matching = Match(g, free_vertices, colors, animation_data)
    while len(free_vertices) != 0:
        # start with displaying the graph g
        update(animation_data, g, colors)

        free_vertices = find_free_vertices(g)
        update_multiple_vertex_color(colors, free_vertices, "yellow")
        update(animation_data, g, colors)

        # random_vertex = pick_random(free_vertices)
        for node in free_vertices:
            update_vertex_color(colors, node, "red")
            update(animation_data, g, colors)
            aug_path = matching.bfs_blossom(node)
            update_multiple_edge_color(colors, aug_path.edges, "red")
            path = [x for x in aug_path.nodes]
            # free_vertices.remove(path[0])
            # free_vertices.remove(path[-1])
            break
        else:
            break
        # next_free_vertex, vertices = BFS(g, random_vertex)
        # highlight the next free vertex
        # this step can be further subdivided -- showing all animations till finding the next free vertex
        # also add the blossom part in this
        update(animation_data, g, colors)
        #
        max_matching = matching.invert_aug_path(aug_path)
        update_multiple_edge_color(colors, max_matching, "blue")
        count = 0
        for node in free_vertices:
            if g.nodes[node]["mate"] is not None:
                count += 1

        # highlight the inverted augmenting path
        update(animation_data, g, colors)
        #
        # g = update_graph(g, matching)
        # free_vertices = find_free_vertices(g)

    # display final matching

    update(animation_data, g, colors)
    return animation_data

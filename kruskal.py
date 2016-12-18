import math
import networkx as grapher
import random as random


class ufds:  # class for union-find data structure
    def __init__(self, nodes):
        self._set = dict((node, node) for node in nodes)  # the set id
        self.length = dict((node, 1) for node in nodes)  # size of the set
        self.items = dict((node, [node]) for node in nodes)  # number of nodes
                                                                # in each set


def newuf(nodes):  # create union-find data structure
    return ufds(nodes)


def find(ufds, x):
    return ufds._set[x]  # return which set x belongs to


def union(ufds, x, y):  # join two sets using union by size principle where you
                        # merge the smaller set into the larger one
    assert x in ufds.items and y in ufds.items
    if ufds.length[x] > ufds.length[y]:  # check if x is greater than y,
        x, y = y, x  # if true, switch the sets so that x is the smaller set
    for i in ufds.items[x]:
        ufds._set[i] = y
        ufds.items[y].append(i)  # iteratively put items from x into y
    ufds.length[y] += ufds.length[x]  # update size of y


# Kruskal algorithm implementation using union-find data structure
def kruskal(graph):  # Outputs the minimum spanning tree of the graph
    edges = [(x, y, graph[x][y]['length']) for x, y in graph.edges()]
    edges.sort(cmp=lambda x, y: cmp(x[2], y[2]))
    ufds = newuf(graph.nodes())
    # for edges in increasing weight
    mst = []  # list of edges in the mst
    for a, b, c in edges:
        seta = find(ufds, a)
        setb = find(ufds, b)
        if seta != setb:
            mst.append((a, b))  # if the two sets aren't the same,
            union(ufds, seta, setb)  # then join them using union function!
    return mst


def dist(x, y):  # Distance between two nodes
    return math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))


def randomgraph(n, k):
    # Function for building random graphs to test the kruskal function
    # where n is the number of nodes and k is the number of edges per node
    graph = grapher.Graph()
    for x in range(n):
        graph.add_node(x, pos=(5*random.random(), 5*random.random()))
        # add n nodes to the graph using the networkx library

    for i in graph.nodes():  # Add k edges to every node
        near = [(x, dist(graph.node[i]['pos'], graph.node[x]['pos']))
                for x in graph.nodes() if x != i]
        for x, y in near[0:k]:
            graph.add_edge(i, x, length=y)
    return graph

# If you want to see the list of edges and their lengths while debugging use
# the code below:
# print [e for e in x.edges_iter(data=True)]

# Example:Delete the hashtags to turn the comments below into code and run it
# x= randomgraph(12, 5)
# MST= kruskal(x)
# print MST

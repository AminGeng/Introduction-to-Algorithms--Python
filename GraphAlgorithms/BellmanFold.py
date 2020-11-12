from Graph_SingleSourceShortestPaths import *
from collections import deque


class NodeBellmanFold(object):
    __slots__ = ('key', 'distance', 'parent')

    def __init__(self, key, *, distance=float('inf')):
        self.distance = distance
        self.parent = None
        self.key = key


def relax(u, v, G):
    if G.edge_dict.get((u.key, v.key)) is not None:
        if u.distance + G.edge_dict[(u.key, v.key)] < v.distance:
            v.distance = u.distance + G.edge_dict[(u.key, v.key)]
            v.parent = u


def bellman_fold(G, s):
    key_dict = {}
    for vertex_i in G.vertices:
        key_dict[vertex_i] = NodeBellmanFold(vertex_i)
    key_dict[s].distance = 0
    for i in range(len(G.vertices) - 1):
        for vertex_j in G.edge_dict.keys():
            relax(key_dict[vertex_j[0]], key_dict[vertex_j[1]], G)
    for vertex_j in G.edge_dict.keys():
        if key_dict[vertex_j[1]].distance > key_dict[vertex_j[0]].distance + G.edge_dict[vertex_j]:
            return False

    def path_show(G, s):
        path_dict = {}

        def trace2source(u):
            trace = deque(u)
            u_parent = key_dict[u].parent
            while u_parent:
                trace.appendleft(u_parent.key)
                u_parent = u_parent.parent
            return trace

        for vertex_k in G.vertices:
            path_dict[vertex_k] = trace2source(vertex_k)

        return path_dict

    return path_show(G, s)




from Graph_SingleSourceShortestPaths import *
from collections import deque


class NodeTopologicalSort(object):
    __slots__ = ('key', 'color', 'discover', 'finish')

    def __init__(self, key):
        self.key = key
        self.color = 'white'


class NodeSingleSourceShortestPaths(object):
    __slots__ = ('key', 'distance', 'parent')

    def __init__(self, key, *, distance=float('inf')):
        self.distance = distance
        self.parent = None
        self.key = key


def dfs(G, key_dict):
    for i in key_dict.values():
        i.color = 'white'
    time = 0

    def dfs_visit(G, node_v):
        nonlocal time
        node_v.discover = time
        time += 1
        node_v.color = 'black'
        for i in G.adj_v[node_v.key]:
            i = key_dict[i]
            if i.color == 'white':
                dfs_visit(G, i)
        node_v.finish = time
        time += 1

    for i in key_dict.values():
        if i.color == 'white':
            dfs_visit(G, i)


class GetOutOfRecursion(Exception):
    pass


def is_cyclic(G, key_dict):
    def dfs_visit(G, node_v):
        node_v.color = 'gray'
        for node_i in G.adj_v[node_v.key]:
            node_i = key_dict[node_i]
            if node_i.color == 'gray':
                raise GetOutOfRecursion
            elif node_i.color == 'white':
                dfs_visit(G, node_i)
        node_v.color = 'black'

    for i in key_dict.values():
        i.color = 'white'
    try:
        for i in key_dict.values():
            if i.color == 'white':
                dfs_visit(G, i)
    except GetOutOfRecursion:
        return True
    return False


def relax(node_u, node_v, G):
    if G.edge_dict.get((node_u.key, node_v.key)):
        if node_u.distance + G.edge_dict[(node_u.key, node_v.key)] < node_v.distance:
            node_v.distance = node_u.distance + G.edge_dict[(node_u.key, node_v.key)]
            node_v.parent = node_u


def topological_sort2single_source_shortest_paths(G, s):
    topology_key_dict = {s: NodeTopologicalSort(s)}
    for vertex_i in G.vertices:
        topology_key_dict[vertex_i] = NodeTopologicalSort(vertex_i)
    if is_cyclic(G, topology_key_dict):
        return False
    dfs(G, topology_key_dict)
    vertex_list = [i for i in G.vertices]
    vertex_list.sort(key=lambda x: topology_key_dict[x].finish, reverse=True)
    path_key_dict = {}
    for vertex_i in vertex_list:
        path_key_dict[vertex_i] = NodeSingleSourceShortestPaths(vertex_i)
    n = vertex_list.index(s)
    path_key_dict[s].distance = 0
    for vertex_i in vertex_list[n:]:
        for vertex_j in G.adj_v[vertex_i]:
            relax(path_key_dict[vertex_i], path_key_dict[vertex_j], G)

    def show(G):
        path_list = []
        for vertex_k in G.vertices:
            i_deque = deque(vertex_k)
            i_parent = path_key_dict[vertex_k].parent
            while i_parent:
                i_deque.appendleft(i_parent.key)
                i_parent = i_parent.parent
            path_list.append((vertex_k, i_deque))
        return path_list

    return show(G)


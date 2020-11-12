#  通过重新赋值来生成非负权重, 从而运行dijkstra算法.
#  插入新的源节点s, (s, v)=0, 对于所有的v. h(v)=distance(s, v), w_new(v1, v2)=w(v1, v2)+h(v1)-h(v2).
#  主要用于稀疏图, 按照BellmanFold和Dijkstra算法的要求的邻接链表图.
from Graph_SingleSourceShortestPaths import *
from FibonacciHeap import *
from copy import deepcopy
import numpy as np


def bellman_fold(G, s):
    class NodeBellmanFold(object):
        __slots__ = ('key', 'distance')

        def __init__(self, key, *, distance=float('inf')):
            self.distance = distance
            self.key = key

    def relax(u, v, G):
        if G.edge_dict.get((u.key, v.key)) is not None:
            if u.distance + G.edge_dict[(u.key, v.key)] < v.distance:
                v.distance = u.distance + G.edge_dict[(u.key, v.key)]

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
    return dict((v, key_dict[v].distance) for v in key_dict.keys())


def dijkstra(G, s):
    fib_key_dict = {}
    fib_heap = FibonacciHeap()
    for vertex_v in G.vertices:
        fib_key_dict[vertex_v] = NodeFib(key=vertex_v)
    for vertex_v in G.adj_v[s]:
        fib_key_dict[vertex_v].value = G.edge_dict[(s, vertex_v)]
        fib_key_dict[vertex_v].par = s
    fib_key_dict[s].value = 0
    Q = G.vertices.difference({s})
    for vertex_i in Q:
        fib_heap.insert(fib_key_dict[vertex_i])

    def relax(vertex_u, vertex_v, G):
        if G.edge_dict[(vertex_u, vertex_v)] + fib_key_dict[vertex_u].value < fib_key_dict[vertex_v].value:
            fib_key_dict[vertex_v].par = vertex_u
            fib_heap.decrease_value(fib_key_dict[vertex_v],
                                    G.edge_dict[(vertex_u, vertex_v)] + fib_key_dict[vertex_u].value)

    while Q:
        node_u = fib_heap.extract_min()
        Q.remove(node_u.key)
        for vertex_i in G.adj_v[node_u.key]:
            relax(node_u.key, vertex_i, G)

    fib_key_dict.pop('source')
    return dict(((s, v), (fib_key_dict[v].value, fib_key_dict[v].par)) for v in fib_key_dict.keys())


def johnson(G):
    n_vertices = len(G.vertices)
    arr_distance = np.empty((n_vertices, n_vertices))
    arr_predecessor = np.empty((n_vertices, n_vertices), dtype=int)
    for i in range(n_vertices):
        arr_predecessor[i, i] = i
    G_new = deepcopy(G)
    for v in G_new.vertices:
        G_new.edge_dict[('source', v)] = 0
    G_new.adj_v['source'] = deepcopy(G_new.vertices)
    G_new.vertices.add('source')
    h = bellman_fold(G_new, 'source')
    if not h:
        return h
    for e in G_new.edge_dict.keys():
        G_new.edge_dict[e] = G_new.edge_dict[e] + h[e[0]] - h[e[1]]
    for v in G.vertices:
        v_dict = dijkstra(G_new, v)
        for v_key, v_value in v_dict.items():
            arr_distance[int(v_key[0]) - 1, int(v_key[1]) - 1] = v_value[0] + h[v_key[1]] - h[v_key[0]]
            if v_value[1]:
                arr_predecessor[int(v_key[0]) - 1, int(v_key[1]) - 1] = int(v_value[1]) - 1
    return arr_distance, arr_predecessor


vertices = {'1', '2', '3', '4', '5'}
edges_dict = {('1', '2'): 3, ('1', '3'): 8, ('1', '5'): -4, ('2', '5'): 7, ('2', '4'): 1,
              ('3', '2'): 4, ('4', '1'): 2, ('4', '3'): -5, ('5', '4'): 6}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)
print(johnson(G))

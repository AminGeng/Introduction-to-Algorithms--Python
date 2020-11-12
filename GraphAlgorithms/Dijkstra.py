#  不包含负权重的边
from Graph_SingleSourceShortestPaths import *
from FibonacciHeap import *
from collections import deque


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
            fib_heap.decrease_value(fib_key_dict[vertex_v], G.edge_dict[(vertex_u, vertex_v)] + fib_key_dict[vertex_u].value)

    while Q:
        node_u = fib_heap.extract_min()
        Q.remove(node_u.key)
        for vertex_i in G.adj_v[node_u.key]:
            relax(node_u.key, vertex_i, G)

    def show(G):
        path_list = []
        for v_j in G.vertices:
            i_path_deque = deque(v_j)
            i_parent = fib_key_dict[v_j].par
            while i_parent:
                i_path_deque.appendleft(i_parent)
                i_parent = fib_key_dict[i_parent].par
            path_list.append((v_j, i_path_deque))
        return path_list

    return show(G)
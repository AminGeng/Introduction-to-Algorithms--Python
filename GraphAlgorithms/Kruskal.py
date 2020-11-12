# connected undirected graph
from Graph_MinimumSpanningTree import *
from DisjointSet import *
from MinHeap import *
import copy


def min_edge(min_heap):
    e = min_heap[0][0]
    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    min_heap.pop()
    min_heapify(min_heap, 0, len(min_heap)-1)
    return e


def is_safe(e):
    if find_set(key_dict[e[0]]) == find_set(key_dict[e[1]]):
        return False
    return True


def kruskal(G):
    for vertex_v in G.vertices:
        make_set(vertex_v)
    n = len(G.vertices)
    min_heap = list(G.edge_dict.items())
    build_min_heap(min_heap)
    safe_edge = []
    i = 1
    while i < n:
        consider_edge = min_edge(min_heap)
        while not (is_safe(consider_edge)):
            consider_edge = min_edge(min_heap)
        union(key_dict[consider_edge[0]], key_dict[consider_edge[1]])
        safe_edge.append(consider_edge)
        i += 1
    return safe_edge


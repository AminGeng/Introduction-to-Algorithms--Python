from FibonacciHeap import *
from Graph_MinimumSpanningTree import *

key_dict = {}


def min_edge(edges_dict):
    edge_min_value = float('inf')
    edge_min = ()
    for i, j in edges_dict.items():
        if j < edge_min_value:
            edge_min_value = j
            edge_min = i
    return edge_min


def prim(G):
    result = []
    fib_heap = FibonacciHeap()
    aim_edge = min_edge(G.edge_dict)
    result.append(aim_edge)
    for i in G.vertices:
        key_dict[i] = NodeFib(key=i)
    for i in G.adj_v[aim_edge[0]]:
        key_dict[i].value = G.edge_dict[(aim_edge[0], i)]
        key_dict[i].par = aim_edge[0]
    for i in G.adj_v[aim_edge[1]]:
        if key_dict[i].value > G.edge_dict[(aim_edge[1], i)]:
            key_dict[i].value = G.edge_dict[(aim_edge[1], i)]
            key_dict[i].par = aim_edge[1]
    Q = G.vertices.difference({aim_edge[0], aim_edge[1]})
    print('Q=', Q)
    for i in Q:
        fib_heap.insert(key_dict[i])
    fib_heap.fib_show(fib_heap.min)
    while Q:
        print('Q=', Q)
        print('result=', result)
        u = fib_heap.extract_min()
        print('u.key=', u.key)
        print('new')
        fib_heap.fib_show(fib_heap.min)
        Q.remove(u.key)
        result.append((u.key, u.par))
        for i in G.adj_v[u.key]:
            if i in Q and G.edge_dict[(i, u.key)] < key_dict[i].value:
                print('i:', i)
                fib_heap.decrease_value(key_dict[i], G.edge_dict[(i, u.key)])
                print('new')
                fib_heap.fib_show(fib_heap.min)
                key_dict[i].par = u.key
    return result


from Kruskal import *
from Prim import *
vertices = {chr(i) for i in range(97, 97+9)}
path_dict = {('a', 'b'): 4, ('b', 'c'): 8, ('c', 'd'): 7, ('d', 'e'): 9, ('e', 'f'): 10, ('f', 'g'): 2,
             ('g', 'h'): 1, ('h', 'a'): 8, ('h', 'i'): 7, ('i', 'g'): 6, ('i', 'c'): 2, ('c', 'f'): 4,
             ('d', 'f'): 14, ('b', 'h'): 11}

G = GraphForMinimumSpanningTree(vertices=vertices, edges_dict=path_dict)


print(kruskal(G))
print(prim(G))


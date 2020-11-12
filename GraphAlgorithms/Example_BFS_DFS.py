from BFS_AdjacencyList import *
from DFS_AdjacencyList import *

vertices = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
adjacency_dict = {'s': ['r'], 'r': [], 't': ['x'], 'u': ['t', 'y'], 'v': ['r'],
                  'w': ['s', 't'], 'x': ['y', 'u', 'w'], 'y': []}
G = GraphAdjacencyList(vertices=vertices, adjacency_list=adjacency_dict)

a = 'w'
print(breath_first_search(G, a))

print(topological_sort(G))
print(strongly_connected_components(G))

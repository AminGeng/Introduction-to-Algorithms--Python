from BellmanFold import *
from TopologicalSortSingleSourceShortestPaths import *
from Dijkstra import *

vertices = {'s', 't', 'x', 'y', 'z'}
edges_dict = {('s', 't'): 6, ('s', 'y'): 7, ('t', 'x'): 5, ('t', 'y'): 8, ('t', 'z'): -4, ('x', 't'): -2,
              ('y', 'x'): -3, ('z', 's'): 2, ('z', 'x'): 7}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)

print(bellman_fold(G, 's'))

vertices = {'3', '1', '2', '4', '5', 'source'}
edges_dict = {('1', '2'): 3, ('1', '3'): 8, ('1', '5'): -4, ('2', '5'): 7, ('2', '4'): 1, ('3', '2'): 4, ('4', '1'): 2,
              ('4', '3'): -5, ('5', '4'): 6, ('source', '3'): 0, ('source', '1'): 0, ('source', '2'): 0,
              ('source', '4'): 0, ('source', '5'): 0}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)
print(bellman_fold(G, 'source'))

vertices = {'1', '2', '3', '4', '5'}
edges_dict = {('1', '2'): 3, ('1', '3'): 8, ('1', '5'): -4, ('2', '5'): 7, ('2', '4'): 1,
              ('3', '2'): 4, ('4', '1'): 2, ('4', '3'): -5, ('5', '4'): 6}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)
print(bellman_fold(G, '5'))

vertices = {'r', 's', 't', 'x', 'y', 'z'}
edges_dict = {('s', 't'): 2, ('s', 'x'): 6, ('t', 'x'): 7, ('t', 'y'): 4, ('t', 'z'): 2, ('x', 'y'): -1,
              ('x', 'z'): 1, ('y', 'z'): -2, ('r', 't'): 3, ('r', 's'): 5}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)

print(topological_sort2single_source_shortest_paths(G, 's'))

vertices = {'s', 't', 'x', 'y', 'z'}
edges_dict = {('s', 't'): 10, ('s', 'y'): 5, ('t', 'x'): 1, ('t', 'y'): 2, ('x', 'z'): 4,
              ('y', 'x'): 9, ('y', 't'): 3, ('y', 'z'): 2, ('z', 's'): 7, ('z', 'x'): 6}
G = GraphForSingleSourceShortestPaths(vertices=vertices, edge_dict=edges_dict)

print(dijkstra(G, 's'))

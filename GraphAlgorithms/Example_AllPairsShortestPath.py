from MatrixMultiplyAllParisShortestPath import *
from MatrixMultiplyAllParisShortestPath_Advanced import *


key_dict = dict((i, chr(i+97)) for i in range(5))
matrix = np.array([[0, 3, 8, float('inf'), -4],
                   [float('inf'), 0, float('inf'), 1, 7],
                   [float('inf'), 4, 0, float('inf'), float('inf')],
                   [2, float('inf'), -5, 0, float('inf')],
                   [float('inf'), float('inf'), float('inf'), 6, 0]])
G = GraphAllPairsShortestPath(key_dict=key_dict, matrix=matrix)


print(matrix_multiply_all_pairs_shortest_path(G))
print(matrix_multiply_all_pairs_shortest_path_advanced(G))
for i in [0, 1]:
    print((matrix_multiply_all_pairs_shortest_path_advanced(G)[i] == matrix_multiply_all_pairs_shortest_path(G)[i]))
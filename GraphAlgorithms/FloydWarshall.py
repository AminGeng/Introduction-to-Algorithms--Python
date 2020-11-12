import numpy as np


class GraphAllPairsShortestPath(object):
    def __init__(self, *, key_dict=None, matrix=None):
        self.key_dict = key_dict  # dict(key:矩阵的行或列int, value:名字str)
        self.matrix = matrix  # 数值代表路径长度, inf不直接相连.


def floyd_warshall(G):
    matrix_path = G.matrix.copy()
    n = matrix_path.shape[0]
    index = (np.arange(0, n).reshape(n, 1)).repeat(n, axis=1)
    matrix_predecessor = np.where(matrix_path == float('inf'), -1, index)
    for i in range(n):
        matrix_compare = np.add.outer(matrix_path[:, i], matrix_path[i])
        matrix_path_new = np.where(matrix_path < matrix_compare, matrix_path, matrix_compare)
        #  因为神奇的广播机制
        matrix_predecessor = np.where(matrix_path == matrix_path_new, matrix_predecessor, matrix_predecessor[i])
        matrix_path = matrix_path_new
    return matrix_path, matrix_predecessor


key_dict = dict([(i, chr(i + 97)) for i in range(5)])
matrix = np.array([[0, 3, 8, float('inf'), -4],
                   [float('inf'), 0, float('inf'), 1, 7],
                   [float('inf'), 4, 0, float('inf'), float('inf')],
                   [2, float('inf'), -5, 0, float('inf')],
                   [float('inf'), float('inf'), float('inf'), 6, 0]])
G = GraphAllPairsShortestPath(key_dict=key_dict, matrix=matrix)
print(floyd_warshall(G))

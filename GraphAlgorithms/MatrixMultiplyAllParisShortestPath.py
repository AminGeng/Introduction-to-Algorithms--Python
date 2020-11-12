import numpy as np


class GraphAllPairsShortestPath(object):
    def __init__(self, *, key_dict=None, matrix=None):
        self.key_dict = key_dict  # dict(key:矩阵的行或列int, value:名字str)
        self.matrix = matrix  # 数值代表路径长度, inf不直接相连.


def matrix_multiply(matrix_d, matrix_a, matrix_predecessor):
    n = matrix_d.shape[0]
    matrix_c = matrix_d.copy()
    for i in range(n):
        for j in range(n):
            array_c = matrix_d[i] + matrix_a[:, j]
            station = np.argmin(array_c)
            distance = array_c[station]
            if distance < matrix_c[i, j]:  # 路径的精髓在这里.
                matrix_predecessor[i, j] = station
                matrix_c[i, j] = distance
    return matrix_c


def matrix_multiply_all_pairs_shortest_path(G):
    matrix_a = G.matrix.copy()
    n = matrix_a.shape[0]
    matrix_distance = matrix_a.copy()
    index = (np.arange(0, n).reshape(n,1)).repeat(n, axis=1)
    matrix_predecessor = np.where(matrix_distance == float('inf'), -1, index)
    for i in range(n-1):
        matrix_distance = matrix_multiply(matrix_distance, matrix_a, matrix_predecessor)
    return matrix_distance, matrix_predecessor



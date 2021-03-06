import numpy as np


class GraphAllPairsShortestPath(object):
    def __init__(self, *, key_dict=None, matrix=None):
        self.key_dict = key_dict  # dict(key:矩阵的行或列int, value:名字str)
        self.matrix = matrix  # 数值代表路径长度, inf不直接相连.


def matrix_multiply_advanced(matrix_d, matrix_a, matrix_predecessor):
    n = matrix_d.shape[0]
    matrix_c = matrix_d.copy()
    for i in range(n):
        for j in range(n):
            array_c = matrix_d[i] + matrix_a[:, j]
            mid_station = np.argmin(array_c)
            distance = array_c[mid_station]
            if distance < matrix_c[i, j]:
                if matrix_predecessor[mid_station, j] == j:
                    matrix_predecessor[i, j] = mid_station
                else:
                    matrix_predecessor[i, j] = matrix_predecessor[mid_station, j]
                matrix_c[i, j] = distance
    return matrix_c


def matrix_multiply_all_pairs_shortest_path_advanced(G):
    matrix_distance = G.matrix.copy()
    n = matrix_distance.shape[0]
    index = (np.arange(0, n).reshape(n, 1)).repeat(n, axis=1)
    matrix_predecessor = np.where(matrix_distance == float('inf'), -1, index)
    k = 2
    n_square = n*n
    while k < n_square:
        matrix_distance = matrix_multiply_advanced(matrix_distance, matrix_distance, matrix_predecessor)
        k *= k
    return matrix_distance, matrix_predecessor




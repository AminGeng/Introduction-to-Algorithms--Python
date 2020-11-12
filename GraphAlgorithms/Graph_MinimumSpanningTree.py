# 无向图,所以需要一下对称处理.


class GraphForMinimumSpanningTree(object):
    __slots__ = ('vertices', 'edge_dict', 'adj_v')

    def __init__(self, *, vertices=None, edges_dict=None):
        self.vertices = vertices  # str类型的vertex: 'a', 'b', ...
        self.edge_dict = self.edge_dict_symmetry(edges_dict)  # {('a','b'): 3, ... }, 'a', 'b'是顶点名字, 3是'a'到'b'的距离
        self.adj_v = self.edge_dict2adj_v(edges_dict)  # key: 顶点; value:从顶点出发的边集

    def edge_dict2adj_v(self, edges_dict):
        vertex_vertices_dict = {}
        for vertex in self.vertices:
            vertex_vertices_dict[vertex] = set()
        for edge in edges_dict.keys():
            vertex_vertices_dict[edge[0]].add(edge[1])
            vertex_vertices_dict[edge[1]].add(edge[0])
        return vertex_vertices_dict

    def edge_dict_symmetry(self, edges_dict):
        d = {}
        for i, j in edges_dict.items():
            d[(i[1], i[0])] = j
            d[i] = j
        return d


class GraphForSingleSourceShortestPaths(object):
    __slots__ = ('vertices', 'edge_dict', 'adj_v')

    def __init__(self, *, vertices=None, edge_dict=None):
        self.vertices = vertices  # 集合; 集合中的元素是str类型的vertex: 'a', 'b', ...
        self.edge_dict = edge_dict
        self.adj_v = self.edges_dict2adj_v(edge_dict)  # key: 顶点; value:从顶点出发的顶点集

    def edges_dict2adj_v(self, edge_dict):
        vertex_vertices_dict = {}
        for vertex in self.vertices:
            vertex_vertices_dict[vertex] = set()
        for edge in edge_dict.keys():
            vertex_vertices_dict[edge[0]].add(edge[1])
        return vertex_vertices_dict

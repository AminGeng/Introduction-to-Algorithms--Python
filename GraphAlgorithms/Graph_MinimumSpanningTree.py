# 最小生成树所需无向图, Kruskal与Prim算法
# 邻接链表表示
# 边的权重非负
class GraphForMinimumSpanningTree(object):
    __slots__ = ('vertices', 'edge_dict', 'adj_v')

    # vertices: 顶点, 字符串形式, 将来如果需要建堆, 会作为结点的key
    # edge_dict: key:边, value:边的权重, (边全部形如(a, b): a, b都是字符串, 是ab边的起点和终点)
    # adj_v: key:顶点(字符串), value:set(set内部元素: 与顶点相邻的结点, 结点还是字符串形式).
    def __init__(self, *, vertices=None, edge_dict=None):
        self.vertices = vertices
        self.edge_dict = self.edge_dict_symmetry(edge_dict)
        self.adj_v = self.edge_dict2adj_v(self.edge_dict)

    # 重要申明
    # edge_dict作为建图时传入的数据, 形式key:边, value:权重, 由于是无向图, 为了方便一条边只会出现一次, 如(a, b)或(b, a)只出现一个
    # edge_dict_symmetry将每条边正反各出现一次
    def edge_dict_symmetry(self, edge_dict):
        symmetry_edge_dict = {}
        for i, j in edge_dict.items():
            symmetry_edge_dict[(i[1], i[0])] = j
            symmetry_edge_dict[i] = j
        return symmetry_edge_dict

    # 通过检索处理之后的edge_dict, 形成每个顶点与它多邻接的顶点的键值字典
    def edge_dict2adj_v(self, edge_dict):
        v_adj_dict = {}
        for v in self.vertices:
            v_adj_dict[v] = set()
        for edge in edge_dict.keys():
            v_adj_dict[edge[0]].add(edge[1])
        return v_adj_dict

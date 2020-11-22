# Prim算法, 时间复杂度优于kruskal算法
# 原理: 树中已有边集E, E中所有的顶底集为V_s, 剩余顶点集V_r, 每次从V_r中找到相距V_s最近的顶点及其最近的边e, 将e加入E中.
# 时间复杂度: extract_min每次需要O(lgV), 总V(lgV), decrease_key每次O(1), 总EO(1)=O(E), 其他不超过这两个, 所以O(VlgV+E)
# 若将斐波那契堆换做最小堆, 每次decrease_key时间复杂度为O(lgV), 其他不变, 会有与kruskal一样的的时间复杂度O(ElgV), 越不稀疏越有优势.

from FibonacciHeap import *
from Graph_MinimumSpanningTree import *

# 字典, 用来存储斐波那契堆结点的key与key对应的结点, 方便快速定位结点, 即key:顶点(字符串, 也是value中结点的key), value:key对应结点
key_dict = {}


# 寻找权重最小的边
def min_edge(edges_dict):
    edge_min_value = float('inf')
    edge_min = ()
    for i, j in edges_dict.items():
        if j < edge_min_value:
            edge_min_value = j
            edge_min = i
    return edge_min


def prim(G):
    # result存储最小生成树的边集, 输出需要
    result = []
    fib_heap = FibonacciHeap()
    # 寻找所有边中最短的, 加入树中.
    aim_edge = min_edge(G.edge_dict)
    result.append(aim_edge)
    # 创建key是顶点名的斐波那契结点
    for v in G.vertices:
        key_dict[v] = NodeFib(key=v)
    # 为每个结点赋值, 方法是搜索结点与树中已有结点的最短距离, 树中目前只有aim_edge的两个结点
    # par中存储与结点间边值为value的顶点.
    for v in G.adj_v[aim_edge[0]]:
        key_dict[v].value = G.edge_dict[(aim_edge[0], v)]
        key_dict[v].par = aim_edge[0]
    for v in G.adj_v[aim_edge[1]]:
        if key_dict[v].value > G.edge_dict[(aim_edge[1], v)]:
            key_dict[v].value = G.edge_dict[(aim_edge[1], v)]
            key_dict[v].par = aim_edge[1]
    # v_rest没有在最小生成树中的顶点集
    v_rest = G.vertices.difference({aim_edge[0], aim_edge[1]})
    for v in v_rest:
        fib_heap.insert(key_dict[v])
    # 当所有顶点全部加入树中, 算法终止
    while v_rest:
        # 选取距离树中已有顶点最近的顶点, 将其对应的最近的边加入result中
        u = fib_heap.extract_min()
        v_rest.remove(u.key)
        result.append((u.key, u.par))
        # 因为新加入的顶点会可能导致与该顶点相邻顶点到已有顶点集的最近距离改变, 所以需要检索所有与新加入顶点相邻顶点.
        for v in G.adj_v[u.key]:
            if v in v_rest and G.edge_dict[(v, u.key)] < key_dict[v].value:
                fib_heap.decrease_value(key_dict[v], G.edge_dict[(v, u.key)])
                key_dict[v].par = u.key
    return result

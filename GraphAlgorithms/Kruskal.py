# Kruskal算法
# 原理: 已有边集E, 每次选择剩余边中的最短边, 是安全边加入E中, 不是从剩余边集中去除, 重新选最短边, 直到找到安全边, 依次循环
# 判断安全边时需要用到不相交集合森林数据结构
# 使用最小堆选取最小边时
# 时间复杂度O(ElgV): 抽取最小结点可能需要将全部边排序, 即O(ElgE), 即O(ElgV), 判断安全边时间复杂度O(Eα(v))可以看做O(E), 合并O(V)
from Graph_MinimumSpanningTree import *
from DisjointSet import *
from MinHeap import *
import copy


# 从最小堆总抽取最小元素, 并维持最小堆性质
def min_edge(min_heap):
    e = min_heap[0][0]
    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    min_heap.pop()
    min_heapify(min_heap, 0, len(min_heap) - 1)
    return e


# 判断边e是否是安全边, 即e的两个顶点是不是属于两棵不同的树
# 数据结构: 不相交集合森林
def is_safe(e):
    if find_set(key_dict[e[0]]) == find_set(key_dict[e[1]]):
        return False
    return True


# 算法主体
def kruskal(G):
    # 为每个顶点建树
    for vertex_v in G.vertices:
        make_set(vertex_v)
    # 利用图G的edge_dict的items()建立最小堆, items()中元素是元祖(a, b), a是边(边的形式(x, y), x,y是两端点名字), b是边的权重
    min_heap = list(G.edge_dict.items())
    build_min_heap(min_heap)
    # safe_edges存放最小生成树的边
    safe_edges = []
    # 最小生成树的边数==V-1, V是顶点数.
    i = 1
    n = len(G.vertices)
    while i < n:
        # 每次抽取棵考虑边中权重最小的边, 判断是否为安全边, 不是继续抽取, 直到找到第一个安全边
        consider_edge = min_edge(min_heap)
        while not (is_safe(consider_edge)):
            consider_edge = min_edge(min_heap)
        # 将安全边的两个端点所在的树合并, 数据结构是不相交集合森林
        union(key_dict[consider_edge[0]], key_dict[consider_edge[1]])
        # 将安全边加入树边中
        safe_edges.append(consider_edge)
        i += 1
    return safe_edges

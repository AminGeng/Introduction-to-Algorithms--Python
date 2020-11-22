# 最小生成树测试用例测试Kruskal算法和Prim算法
# 无向有环图, 边的权重非负

from Kruskal import *
from Prim import *
import random


# 判断两棵最小数的总边长是否相等, 一次判断两种算法的正确性
# 因为最小生成树可能不止一棵, 但最小生成树的总边长唯一, 所以用总边长判断.
def is_equal(list_k, list_p, G):
    length_k = 0
    length_p = 0
    for i in list_k:
        length_k += G.edge_dict[i]
    for i in list_p:
        length_p += G.edge_dict[i]
    return length_k == length_p


# 此例是中文版《算法导论》第三版P367页例子, 可以与教材进行输出比对
# vertices是顶点集, 此处是字母a~i
vertices = {chr(i) for i in range(97, 97 + 9)}
# path_dict存放边与边的权重键值对
path_dict = {('a', 'b'): 4, ('b', 'c'): 8, ('c', 'd'): 7, ('d', 'e'): 9, ('e', 'f'): 10, ('f', 'g'): 2,
             ('g', 'h'): 1, ('h', 'a'): 8, ('h', 'i'): 7, ('i', 'g'): 6, ('i', 'c'): 2, ('c', 'f'): 4,
             ('d', 'f'): 14, ('b', 'h'): 11}
G = GraphForMinimumSpanningTree(vertices=vertices, edge_dict=path_dict)
k_list = kruskal(G)
p_list = prim(G)
print(is_equal(k_list, p_list, G), p_list, k_list, sep='\n')

# 随机改变边的权重, 测试两种算法是否输出一致
for _ in range(10):
    for i in path_dict.keys():
        path_dict[i] = random.randint(1, 100)
    G = GraphForMinimumSpanningTree(vertices=vertices, edge_dict=path_dict)
    k_list = kruskal(G)
    p_list = prim(G)
    print(is_equal(k_list, p_list, G), p_list, k_list, sep='\n')

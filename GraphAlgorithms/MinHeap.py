# 最小二叉堆, Kruskal算法用到
# 这里以列表的形式存放最小堆
# Kruskal算法使用最小堆, 表头存放最小元素, 表头表尾元素交换, 然后pop表尾最小元素, 再运行一次min_heapify使最小元素依旧在表头


# 列表形式的二叉堆, 位于index_i的元素的左孩子所在位置
def left(index_i):
    return index_i * 2 + 1


# 列表形式的二叉堆, 位于index_i的元素的右孩子所在位置
def right(index_i):
    return index_i * 2 + 2


# edge_list: 列表, 元素(a, b), a是边(边的形式是(x, y), x和y是边的端点, x和y都是字符串, 即端点的名字), b是边的权重.
# min_heapify运行条件是列表从index_i+1到index_j已经符合最小堆要求.
# min_heapify处理index_i中元素, 将其放到正确位置
def min_heapify(edge_list, index_i, index_j):
    index_min = index_i
    if left(index_i) <= index_j and edge_list[left(index_i)][1] < edge_list[index_i][1]:
        index_min = left(index_i)
    if right(index_i) <= index_j and edge_list[right(index_i)][1] < edge_list[index_min][1]:
        index_min = right(index_i)
    if index_min != index_i:
        edge_list[index_min], edge_list[index_i] = edge_list[index_i], edge_list[index_min]
        min_heapify(edge_list, index_min, index_j)


# 将未排序列表排成一个最小堆
# 其叶节点的数目为元素总数-元素总数//2
# 从len(edge_list)//2-1开始往前依次运行min_heapify, 直到0位置, 以完成整个列表的最小堆化
def build_min_heap(edge_list):
    for index_i in range(len(edge_list) // 2 - 1, -1, -1):
        min_heapify(edge_list, index_i, len(edge_list) - 1)

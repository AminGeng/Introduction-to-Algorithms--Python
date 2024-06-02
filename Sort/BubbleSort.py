"""
冒泡排序
稳定
空间复杂度: O(1)
时间复杂度: O(N^2)
原理: 
    两层循环: 第i轮外层循环, 内层从后往前检索到位置i, 检索过程比较相邻位置大小, 若后者小于前者, 交换位置 第i轮循环结束, 列表前i个依次排列列表前i小元素
"""

def bubble_sort(list_to_sort):
    # 外层循环, 指定内层循环每次停止位置.
    # 只需到倒数第二位时, 整个列表已经排好, 最后剩下的一个一定是倒数第一
    for index_i in range(len(list_to_sort) - 1):
        # 内层循环, 从后往前检索到位置index_i+1(因为比较过程是list_to_sort[index_j] < list_to_sort[index_j - 1])
        # 检索过程比较相邻位置大小, 若后者小于前者, 交换位置
        for index_j in range(len(list_to_sort) - 1, index_i, -1):
            if list_to_sort[index_j] < list_to_sort[index_j - 1]:
                list_to_sort[index_j], list_to_sort[index_j - 1] = list_to_sort[index_j - 1], list_to_sort[index_j]


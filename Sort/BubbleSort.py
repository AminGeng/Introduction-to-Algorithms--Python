# 冒泡排序
# 原理: 两层循环: 第i轮外层循环, 内层从后往前检索到位置i, 检索过程比较相邻位置大小, 若后者小于前者, 交换位置
# 原理续: 第i轮循环结束, 列表前i个依次排列列表前i小元素
# 稳定排序, 原址排序
# 时间复杂度: O(N^2)
import random
import time


def bubble_sort(list_a):
    # 外层循环, 指定内层循环每次停止位置.
    # 只需到倒数第二位时, 整个列表已经排好, 最后剩下的一个一定是倒数第一
    for index_i in range(len(list_a) - 1):
        # 内层循环, 从后往前检索到位置index_i+1(因为比较过程是list_a[index_j] < list_a[index_j - 1])
        # 检索过程比较相邻位置大小, 若后者小于前者, 交换位置
        for index_j in range(len(list_a) - 1, index_i, -1):
            if list_a[index_j] < list_a[index_j - 1]:
                list_a[index_j], list_a[index_j - 1] = list_a[index_j - 1], list_a[index_j]


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 116.59624123573303, 最慢一个
start = time.time()
for i in range(1000):
    A = [random.randint(1, 100) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    bubble_sort(A)
    if A != B:
        print('error')
print(time.time() - start)

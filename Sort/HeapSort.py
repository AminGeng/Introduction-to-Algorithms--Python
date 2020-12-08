# 堆排序
# 原理: 通过build_max_heap方法将列表排成最大堆, 即满足: list(i)>list(i*2+1)(i位置元素左孩子), list(i)>list(i*2+2)(i位置元素右孩子)
# 原理续: 进入循环, 第i此交换倒数第i为与第一位, 使第i大的元素排在倒数第i位, 然后运行max_heapify方法, 保持前N-i个元素的堆性质
# 不稳定, 原址排序
# 时间复杂度O(NlgN)
import random
import time


# def parent(i):
#     return (i + 1) // 2 - 1


# 列表中index_i位置处的元素的左孩子的位置
def left(index_i):
    return (index_i + 1) * 2 - 1


# 列表中index_i位置处的元素的右孩子的位置
def right(index_i):
    return (index_i + 1) * 2


# 维持列表从位置index_i到index_j的堆性质
# 运行前提条件: 列表从位置index_i+1到index_j满足最大堆性质
def max_heapify(list_a, index_i, index_j):
    # 在list_a中的index_i, left(index_i), right(index_i)三个位置找出元素的值最大的那个
    index_max = index_i
    if left(index_i) <= index_j and list_a[left(index_i)] > list_a[index_i]:
        index_max = left(index_i)
    if right(index_i) <= index_j and list_a[right(index_i)] > list_a[index_max]:
        index_max = right(index_i)
    # 如果值最大的在index_i处, 堆性质不需要维护
    # 否则将最大元素交换到index_i处, 并继续, 从最大元素所在原始位置开始运行max_heapify操作, 维持从从位置index_man到index_j的堆性质
    if index_max != index_i:
        list_a[index_max], list_a[index_i] = list_a[index_i], list_a[index_max]
        max_heapify(list_a, index_max, index_j)


# 将list_a建成一个最大堆
# 最大堆的内部结点有len(list)//2个, 所以直接从len(list_a)//2-1处开始运行max_heapify, 维持从该位置到列表最后的堆性质, 依此降序到0
def build_max_heap(list_a):
    for index_i in range(len(list_a) // 2 - 1, -1, -1):
        max_heapify(list_a, index_i, len(list_a) - 1)


# 堆排序主体
# 首次运行build_max_heap建立最大堆, 将列首最大元素与列尾元素交换
# 之后每次运行max_heapify, 维持从列首到列尾未交换过的元素位置的最大堆性质
def heap_sort(list_a):
    build_max_heap(list_a)
    for index_i in range(len(list_a) - 1, 0, -1):
        list_a[index_i], list_a[0] = list_a[0], list_a[index_i]
        max_heapify(list_a, 0, index_i - 1)


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 10.619423866271973, 倒数第三
start = time.time()
for i in range(1000):
    A = [random.randint(1, 100) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    heap_sort(A)
    if A != B:
        print('error')
print(time.time() - start)

# 插入排序
# 原理: 两层循环, 外层指针从列表第二项到列表最后一项, 内层从外层指针位置处向前搜索, 直到找到第一个值小于等于该项的位置, 将该项放到其后
# 稳定排序, 原址
# 时间复杂度: 最坏情况O(N^2), 最好情况O(N), 平均O(N^2)
import random
import time


def insert_sort(list_a):
    # 外层循环: 指针, 从列表第二项到列表最后一项
    for index_i in range(1, len(list_a)):
        # 复制list_a[index_i], 循环指针index_j指针指向index_i - 1
        a_i = list_a[index_i]
        index_j = index_i - 1
        # 向前进行搜索, 直到找到第一个值小于等于list_a[index_i]的位置
        # 过程: 若前一项值大于list_a[index_i], 指针处项的值更新为前一项的值, 直到某一项的值小于等于list_a[index_i], 或搜索到列表头.
        while index_j > -1 and list_a[index_j] > a_i:
            list_a[index_j + 1] = list_a[index_j]
            index_j -= 1
        # 将第一个值小于等于list_a[index_i]的位置的后一项的值更新为list_a[index_i]
        list_a[index_j + 1] = a_i


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 52.72240877151489, 倒数第二, 很慢
start = time.time()
for i in range(1000):
    A = [random.randint(1, 100) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    insert_sort(A)
    if A != B:
        print('error')
print(time.time() - start)

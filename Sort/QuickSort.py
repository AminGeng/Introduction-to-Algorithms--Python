# 快速排序
# 原理: 每次随机指定列表某个位置, 检索处理列表, 使小于该位置值的元素交换移至列表左侧, 大于该位置值的元素交换移至列表右侧
# 原理续: , 该位置元素交换移至中间, 这样只需再对左右两侧分别排序即可, 所以对列表左侧及右侧进行上述同样操作, 直到完成排序
# 不稳定排序, 原址排序
# 时间复杂度: 最好O(NlgN), 最坏O(N^2), 平均O(NLgN)
import random
import time


# 随机指定列表某个位置, 检索处理列表, 使小于该位置值的元素交换移至列表左侧, 大于该位置值的元素交换移至列表右侧
# 该位置元素交换移至中间, 返回该位置元素最终在列表中的位置
def find_position(list_b, index_i, index_j):
    # 随机指定列表某个位置, 将该位置元素与列表最后一位交换
    index_r = random.randint(index_i, index_j)
    r_value = list_b[index_r]
    list_b[index_r], list_b[index_j] = list_b[index_j], list_b[index_r]
    # smaller_next_index指向已检索过的小于指定元素的元素所在位置的后一项
    smaller_next_index = index_i
    # 从index_i搜索到index_j - 1, 因为index_j存放指定元素
    for index_p in range(index_i, index_j):
        # 若index_p位置处元素小于指定元素, 将其交换放到smaller_next_index处, 并将smaller_next_index后移一位
        if list_b[index_p] < r_value:
            list_b[index_p], list_b[smaller_next_index] = list_b[smaller_next_index], list_b[index_p]
            smaller_next_index += 1
    # 最后将指定元素交换放到smaller_next_index处, 并返回smaller_next_index的值
    list_b[smaller_next_index], list_b[index_j] = list_b[index_j], list_b[smaller_next_index]
    return smaller_next_index


# 递归: 每次调用find_position方法, 检索处理列表为左右两侧, 再对左右侧进行同样操作
def quick_sort(list_a, index_x, index_y):
    if index_x < index_y:
        divide = find_position(list_a, index_x, index_y)
        quick_sort(list_a, index_x, divide - 1)
        quick_sort(list_a, divide + 1, index_y)


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 3.907013416290283, 很快, 仅次于线性排序,
start = time.time()
for i in range(1000):
    A = [random.randint(1, 100) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    quick_sort(A, 0, len(A) - 1)
    if A != B:
        print('error')
print(time.time() - start)

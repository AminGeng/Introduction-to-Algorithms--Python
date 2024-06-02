"""
快速排序
不稳定
空间复杂度: O(1)
时间复杂度: 最好O(NlgN), 最坏O(N^2), 平均O(NLgN)
原理: 
    每次随机指定列表某个位置, 检索处理列表, 使小于该位置值的元素交换移至列表左侧, 大于该位置值的元素交换移至列表右侧
    该位置元素交换移至中间, 这样只需再对左右两侧分别排序即可, 所以对列表左侧及右侧进行上述同样操作, 直到完成排序
"""
import random


# 随机指定列表某个位置, 检索处理列表, 使小于该位置值的元素交换移至列表左侧, 大于该位置值的元素交换移至列表右侧
# 该位置元素交换移至中间, 返回该位置元素最终在列表中的位置
def find_position(list_b, index_head, index_tail):
    # 随机指定列表某个位置, 将该位置元素与列表最后一位交换
    index_r = random.randint(index_head, index_tail)
    r_value = list_b[index_r]
    list_b[index_r], list_b[index_tail] = list_b[index_tail], list_b[index_r]
    # small_index指向已检索过的小于指定元素的元素所在位置的后一项
    small_index = index_head
    # 从index_head搜索到index_tail - 1, 因为index_tail存放指定元素
    for index_p in range(index_head, index_tail):
        # 若index_p位置处元素小于指定元素, 将其交换放到small_index处, 并将small_index后移一位
        if list_b[index_p] < r_value:
            list_b[index_p], list_b[small_index] = list_b[small_index], list_b[index_p]
            small_index += 1
    # 最后将指定元素交换放到small_index处, 并返回small_index的值
    list_b[small_index], list_b[index_tail] = list_b[index_tail], list_b[small_index]
    return small_index


# 递归: 每次调用find_position方法, 检索处理列表为左右两侧, 再对左右侧进行同样操作
def quick_sort_(list_a, index_x, index_y):
    if index_x < index_y:
        index_divide = find_position(list_a, index_x, index_y)
        quick_sort_(list_a, index_x, index_divide - 1)
        quick_sort_(list_a, index_divide + 1, index_y)


def quick_sort(list_a):
    quick_sort_(list_a, 0, len(list_a)-1)

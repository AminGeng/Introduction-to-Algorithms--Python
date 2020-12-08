# 归并排序
# 原理: 二分列表, 分别排好序两个子列表, 然后运行merge方法将两个排好序的子列表归并为排好序的列表
# 原理续: 对子列表排序也是用二路归并策略, 所以merge_sort主体中需要用到递归
# 稳定排序, 非原址
# 时间复杂度: NlgN
import random
import time


# 将x[index_head1:index_head2]和x[index_head2:index_tail + 1]归并为排好序的列表x[index_head1:index_tail + 1]
# 运行条件: x[index_head1:index_head2]和x[index_head2:index_tail + 1]已经分别排好序
def merge(list_x, index_head1, index_head2, index_tail):
    # 复制x[index_head1:index_head2]和x[index_head2:index_tail + 1], 因为归并时会改变x
    list_l = list_x[index_head1:index_head2]
    list_r = list_x[index_head2:index_tail + 1]
    # 在list_l和list_r的尾部插入哑元素infinite, 为了在归并时省去判断是否搜到列表尾.
    list_l.append(float('inf'))
    list_r.append(float('inf'))
    # index_list_l是list_l的位置指针, index_list_r是list_r的位置指针
    index_list_l, index_list_r = 0, 0
    # 归并过程
    # 第k轮, 判断list_l[index_list_l]与list_r[index_list_r]的大小, 将小的放到x[index_head1 + k]的位置, 然后较小的位置指针后移1位
    for k in range(index_tail - index_head1 + 1):
        if list_r[index_list_r] < list_l[index_list_l]:
            list_x[index_head1 + k] = list_r[index_list_r]
            index_list_r += 1
        else:
            list_x[index_head1 + k] = list_l[index_list_l]
            index_list_l += 1


# 归并排序list_x[index_head: index_tail+1]
def merge_sort(list_x, index_head, index_tail):
    # 归并启动条件 list_x[index_head: index_tail+1]中的元素个数>1: 元素个数=index_tail-index_head+1
    if index_tail - index_head > 0:
        # 精髓所在
        # 二分列表为两个子列, 分别排好序, 然后运行merge方法, 归并排好序的两部分列表
        # 子列表排序也采用二路归并策略, 所以用到递归
        index_m = (index_head + index_tail) // 2
        merge_sort(list_x, index_head, index_m)
        merge_sort(list_x, index_m + 1, index_tail)
        merge(list_x, index_head, index_m + 1, index_tail)


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 4.455240488052368, 快
start = time.time()
for i in range(1000):
    A = [random.randint(1, 100) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    merge_sort(A, 0, len(A) - 1)
    if A != B:
        print('error')
print(time.time() - start)

"""
归并排序
稳定
空间复杂度: N
时间复杂度: NlgN
原理: 
    二分列表, 分别排好序两个子列表, 然后运行merge方法将两个排好序的子列表归并为排好序的列表, 
    对子列表排序也是用二路归并策略, 所以merge_sort主体中需要用到递归
"""


# 将list_to_merge[index_head:index_middle]和list_to_merge[index_middle:index_tail + 1]归并为排好序的列表list_to_merge[index_head:index_tail + 1]
# 运行条件: list_to_merge[index_head:index_middle]和list_to_merge[index_middle:index_tail + 1]已经分别排好序
def merge(list_to_merge, index_head, index_middle, index_tail):
    # 复制list_to_merge[index_head:index_middle]和list_to_merge[index_middle:index_tail + 1], 因为归并时会改变list_to_merge
    list_l = list_to_merge[index_head: index_middle]
    list_r = list_to_merge[index_middle: index_tail + 1]
    # 在list_l和list_r的尾部插入哑元素infinite, 为了在归并时省去判断是否搜到列表尾.
    list_l.append(float('inf'))
    list_r.append(float('inf'))
    # index_list_l是list_l的位置指针, index_list_r是list_r的位置指针
    index_list_l, index_list_r = 0, 0
    # 归并过程
    # 第k轮, 判断list_l[index_list_l]与list_r[index_list_r]的大小, 将小的放到list_to_merge[index_head + k]的位置, 然后较小的位置指针后移1位
    for k in range(index_head, index_tail+1):
        if list_r[index_list_r] < list_l[index_list_l]:
            list_to_merge[k] = list_r[index_list_r]
            index_list_r += 1
        else:
            list_to_merge[k] = list_l[index_list_l]
            index_list_l += 1


# 归并排序list_x[index_head: index_tail+1]
def merge_sort_(list_x, index_head, index_tail):
    """
    sort list_x[index_head: index_tail+1]
    """
    # 归并启动条件 list_x[index_head: index_tail+1]中的元素个数>1: 元素个数=index_tail-index_head+1
    if index_tail - index_head > 0:
        # 精髓所在
        # 二分列表为两个子列, 分别排好序, 然后运行merge方法, 归并排好序的两部分列表
        # 子列表排序也采用二路归并策略, 所以用到递归
        index_m = (index_head + index_tail) // 2
        merge_sort_(list_x, index_head, index_m)
        merge_sort_(list_x, index_m + 1, index_tail)
        merge(list_x, index_head, index_m + 1, index_tail)

def merge_sort(list_x):
    merge_sort_(list_x, 0 , len(list_x)-1)
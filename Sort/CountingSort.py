# 计数排序
# 原理: 计数排序需要提前知道列表中会出现哪些数, 记出现的数的总数为K, 列表的总容量为N
# 原理续: 先检索一遍列表, 记录各个数出现的次数, 然后计算出各个数该出现的最后位置(从小到大次数累加)
# 原理续: 新建一个等大列表, 从后往前检索原列表(稳定性), 将该数放到它的实际排序位置处(放到该出现的最后位置, 然后该数出现的最后位置-1)
# 稳定排序, 非原址
# 时间复杂度: O(K+N)
# 为了方便, 我只编写了可能出现的数是[k1, k2]区间的整数的列表, 其他情况我简单脑补可以通过字典的形式解决
import random
import time


# k1, k2是整数, list_a中只出现[k1, k2]区间的整数
def counting_sort(list_a, k1, k2):
    # list_b用来存放最后排好序的列表
    list_b = list_a[:]  # 复制比创建等大的新列表速度快, 比如创建:list_b = [0 for _ in range(len(list_a))]
    # 用来存放每个数和每个数该出现的最后位置: key:数, value:该数出现的最后位置
    dict_c = {}
    # 为每个可能出现在列表中的数创建key
    for number_i in range(k1, k2 + 1):
        dict_c[number_i] = 0
    # 计算每个数出现的次数
    for index_i in range(len(list_a)):
        dict_c[list_a[index_i]] += 1
    # 计数每个数出现的最后位置
    for number_i in range(k1 + 1, k2 + 1):
        dict_c[number_i] += dict_c[number_i - 1]
    # 确保稳定性
    # 从后往前检索原列表(稳定性), 将该数放到它的实际排序位置处(放到该出现的最后位置, 然后该数出现的最后位置-1)
    for index_i in range(len(list_a) - 1, -1, -1):
        list_b[dict_c[list_a[index_i]] - 1] = list_a[index_i]
        dict_c[list_a[index_i]] -= 1
    return list_b


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: [-100, 100]:1.535020351409912, [-1000, 1000]:2.2114148139953613
# 最快的啦
# 如需更改范围, 请更改标记两处
start = time.time()
for i in range(1000):
    # random.randint(-1000, 1000), 指定整数范围[-1000, 1000]
    A = [random.randint(-1000, 1000) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    # counting_sort(A, -1000, 1000), 必须与指定一致或包含指定区间
    if counting_sort(A, -1000, 1000) != B:
        print('error')
print(time.time() - start)

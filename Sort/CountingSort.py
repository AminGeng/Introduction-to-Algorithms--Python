"""
计数排序
稳定 
空间复杂度: O(K+N)
时间复杂度: O(K+N)
原理: 
    假设N个元素都是[0,K]区间的整数. 
    创建列表L_K(size=K+1), 先检索一遍原列表, 记录各个数出现的次数至L_K, 然后计算出各个数该出现的最后位置(L_K[i+1]+=L_K[i] i in [0, K-1])
    新建一个等大列表L_N, 从后往前检索原列表(稳定性), 将该数放到它的实际排序位置处(L_N[L_K[i]++])
"""

# k1, k2是整数, list_x中只出现[k1, k2]区间的整数
def counting_sort(list_x):
    if (len(list_x)<2): return
    # list_b用来存放最后排好序的列表
    x_min = min(list_x)
    x_max = max(list_x)

    list_x_ = list_x[:]  # 复制列表
    # 用来存放每个数和每个数该出现的最后位置
    list_last_position = [0]*(x_max-x_min+1)
    # 记录每个元素出现的次数
    for e in list_x:
        list_last_position[e-x_min] += 1
    # 计算每个元素出现的最后位置+1
    for i in range(0, x_max-x_min):
        list_last_position[i+1] += list_last_position[i]
    for e in list_x_[::-1]:
        list_x[list_last_position[e-x_min]-1] = e
        list_last_position[e-x_min] -= 1


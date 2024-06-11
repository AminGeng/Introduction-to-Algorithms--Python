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

# k1, k2是整数, list_a中只出现[k1, k2]区间的整数
def counting_sort(list_a):
    if (len(list_a)<2): return
    # list_b用来存放最后排好序的列表
    k1 = min(list_a)
    k2 = max(list_a)

    list_b = list_a[:]  # 复制列表
    # 用来存放每个数和每个数该出现的最后位置
    list_k = [0]*(k2-k1+1)
    # 记录每个元素出现的次数
    for e in list_a:
        list_k[e-k1] += 1
    # 计算每个元素出现的最后位置+1
    for i in range(0, k2-k1):
        list_k[i+1] += list_k[i]
    for e in list_b[::-1]:
        list_a[list_k[e-k1]-1] = e
        list_k[e-k1] -= 1


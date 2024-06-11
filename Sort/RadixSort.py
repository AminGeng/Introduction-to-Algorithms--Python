"""
基数排序
稳定
空间复杂度: O(N)
时间复杂度: O(D(N+R)): D是整数的位数, N:列表元素总数, R:每一位的数字数, 十进制就是0~9共10个
原理: 
    从个位开始, 从低到高位, 依次运行counting_sort按该位大小(稳定的)对列表进行排序
    为了方便, 我只编写了对四位数以每一位为基进行排序, 其他情况对代码进行相应更改即可
"""

# 2进制+counting_sort
def counting_sort_binary(list_a, bina_i):
    list_0 = []
    list_1 = []
    for i in range(len(list_a)):
        if list_a[i]>>bina_i & 1==0:
            list_0.append(list_a[i])
        else: list_1.append(list_a[i])
    list_a[:len(list_0)] = list_0
    list_a[len(list_0):] = list_1

# 从个位开始, 从低到高位, 依次运行counting_sort_binary按该位大小(稳定的)对列表进行排序
import math
def radix_sort(list_a):
    if (len(list_a) < 2): return
    binary_num = math.ceil(math.log(max(list_a),2))
    for bina_i in range(binary_num):
        counting_sort_binary(list_a, bina_i)


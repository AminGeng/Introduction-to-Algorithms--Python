# 基数排序
# 此文以固定位数的整数为例
# 原理: 从个位开始, 从低到高位, 依次运行counting_sort按该位大小(稳定的)对列表进行排序
# 稳定排序, 非原址
# 时间复杂度O(D(N+R)): D是整数的位数, N:列表元素总数, R:每一位的数字数, 十进制就是0~9共10个
# 为了方便, 我只编写了对四位数以每一位为基进行排序, 其他情况对代码进行相应更改即可
import random
import time


# 在计数排序的基础上进行了稍微的更改, 按位从低到高, 每次依照第digit_i位大小对list_a排序, 具体原理参见Counting_Sort.py
# list_a[index_i] // (10 ** digit_i) % 10 取list_a[index_i]得第digit_i位数(个位:0, 十位:1, ...)
# digit_i: 排序的位, [k1, k2]: 整数所在区间
def counting_sort(list_a, digit_i, k1, k2):
    list_b = list_a[:]
    dict_c = {}
    for number_i in range(k1, k2 + 1):
        dict_c[number_i] = 0
    for index_i in range(len(list_a)):
        dict_c[list_a[index_i] // (10 ** digit_i) % 10] += 1
    for number_i in range(k1 + 1, k2 + 1):
        dict_c[number_i] += dict_c[number_i - 1]
    for index_i in range(len(list_a) - 1, -1, -1):
        value_i_i = list_a[index_i] // (10 ** digit_i) % 10
        list_b[dict_c[value_i_i] - 1] = list_a[index_i]
        dict_c[value_i_i] -= 1
    return list_b


# 从个位开始, 从低到高位, 依次运行counting_sort按该位大小(稳定的)对列表进行排序
# digits: 指定数的位数
def radix_sort(list_a, digits):
    for digit_i in range(digits):
        list_a = counting_sort(list_a, digit_i, 0, 9)
    return list_a


# 测试部分
# 与系统方法sorted()的结果进行比对
# 测试用时: 三位数:3.2386910915374756, 四位数:4.086498498916626, 五位数5.053367853164673
# 随位数线性增长, 很快
# 如需更改位数, 请更改标记两处
start = time.time()
for i in range(1000):
    # random.randint(10000, 99999), 指定是5位数
    A = [random.randint(10000, 99999) for _ in range(random.randint(1, 2000))]
    B = sorted(A)
    # radix_sort(A, 5), 必须填写指定位数
    if radix_sort(A, 5) != B:
        print('error')
print(time.time() - start)

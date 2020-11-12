import random


def counting_sort(list_a, k):
    list_b = list_a[:]  # 复制比创建等大的新列表速度快
    dict_c = {}
    for i in range(k + 1):
        dict_c[i] = 0
    for i in range(len(list_a)):
        dict_c[list_a[i]] += 1
    for i in range(1, k + 1):
        dict_c[i] += dict_c[i - 1]
    for i in range(len(list_a) - 1, -1, -1):  # insure stability
        list_b[dict_c[list_a[i]] - 1] = list_a[i]
        dict_c[list_a[i]] -= 1
    return list_b


A = [random.randint(0, 20) for i in range(50)]
A_sorted = counting_sort(A, 20)
print(A_sorted)
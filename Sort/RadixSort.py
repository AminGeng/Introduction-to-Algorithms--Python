import random


def counting_sort(list_a, n, k):
    list_b = list_a[:]
    dict_c = {}
    for i in range(k + 1):
        dict_c[i] = 0
    for i in range(len(list_a)):
        dict_c[int(list_a[i][n])] += 1
    for i in range(1, k + 1):
        dict_c[i] += dict_c[i - 1]
    for i in range(len(list_a) - 1, -1, -1):  # insure stability
        list_b[int(dict_c[int(list_a[i][n])]) - 1] = list_a[i]
        dict_c[int(list_a[i][n])] -= 1
    return list_b


A = [str(random.randint(100, 999)) for _ in range(500)]


def radix_sort(list_a, d):
    for i in range(d - 1, -1, -1):
        list_a = counting_sort(list_a, i, 9)
    return list_a


print(radix_sort(A, 3))

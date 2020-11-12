#  稳定排序
import random


def merge(x, p, q, r):
    list_l = x[p:q]
    list_m = x[q:r + 1]
    i, j = 0, 0
    list_l.append(float('inf'))
    list_m.append(float('inf'))
    for k in range(r - p + 1):
        if list_m[i] < list_l[j]:
            x[p + k] = list_m[i]
            i += 1
        else:
            x[p + k] = list_l[j]
            j += 1


def merge_sort(x, p, q):
    if q - p > 0:
        t = (p + q) // 2
        merge_sort(x, p, t)
        merge_sort(x, t + 1, q)
        merge(x, p, t + 1, q)


x = [random.randint(1, 1000) for _ in range(100)]
merge_sort(x, 0, len(x) - 1)
print(x)

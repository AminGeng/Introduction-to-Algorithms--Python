import random


def bubble_sort(list_a):
    for i in range(len(list_a)):
        for j in range(len(list_a) - 1, i, -1):
            if list_a[j] < list_a[j - 1]:
                list_a[j], list_a[j - 1] = list_a[j - 1], list_a[j]
    return list_a


A = [random.randint(0, 100) for _ in range(50)]
print(bubble_sort(A))
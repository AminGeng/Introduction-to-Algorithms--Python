import random


def insert_sort(list_a):
    for i in range(1, len(list_a)):
        j = i-1
        a_i = list_a[i]
        while j > -1 and list_a[j] > a_i:
            list_a[j + 1] = list_a[j]
            j -= 1
        list_a[j + 1] = a_i


A = [random.uniform(1,10) for _ in range(10)]
insert_sort(A)
print(A)
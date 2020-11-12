import random

# def parent(i):
#     return (i + 1) // 2 - 1


def left(i):
    return (i + 1) * 2 - 1


def right(i):
    return (i + 1) * 2


def max_heapify(list_a, i, j):
    max_index = i
    if left(i) <= j and list_a[left(i)] > list_a[i]:
        max_index = left(i)
    if right(i) <= j and list_a[right(i)] > list_a[max_index]:
        max_index = right(i)
    if max_index != i:
        list_a[max_index], list_a[i] = list_a[i], list_a[max_index]
        max_heapify(list_a, max_index, j)


def build_max_heap(list_a):
    for i in range(len(list_a) // 2, -1, -1):
        max_heapify(list_a, i, len(list_a) - 1)


def heap_sort(list_a):
    build_max_heap(list_a)
    for i in range(len(list_a) - 1, 0, -1):
        list_a[i], list_a[0] = list_a[0], list_a[i]
        max_heapify(list_a, 0, i - 1)  # 注意只能从最后删除元素才不会影响堆, 不能直接删除第一个, 那就可能不再是堆了.


A = [random.randint(1, 10) for _ in range(7)]
print(len(A))
build_max_heap(A)
print(A)
heap_sort(A)
print(A)
def left(i):
    return (i + 1) * 2 - 1


def right(i):
    return (i + 1) * 2


def min_heapify(edges_list, i, j):  # edges_list 形如[(('a', 'b'), 3),...]; i is the begin index, j is the end index
    min_index = i
    if left(i) <= j and edges_list[left(i)][1] < edges_list[i][1]:
        min_index = left(i)
    if right(i) <= j and edges_list[right(i)][1] < edges_list[min_index][1]:
        min_index = right(i)
    if min_index != i:
        edges_list[min_index], edges_list[i] = edges_list[i], edges_list[min_index]
        min_heapify(edges_list, min_index, j)


def build_min_heap(edges_list):
    for i in range(len(edges_list) // 2, -1, -1):
        min_heapify(edges_list, i, len(edges_list) - 1)

import random


# index_i, index_j is the begin and end index
def find_position(list_b, index_i, index_j):
    index_r = random.randint(index_i, index_j)
    r_value = list_b[index_r]
    list_b[index_r], list_b[index_j] = list_b[index_j], list_b[index_r]
    small_max = index_i - 1
    for k in range(index_i, index_j):
        if list_b[k] < r_value:
            small_max += 1
            list_b[k], list_b[small_max] = list_b[small_max], list_b[k]
    small_max += 1
    list_b[small_max], list_b[index_j] = list_b[index_j], list_b[small_max]
    return small_max


def quick_sort(list_a, index_x, index_y):
    if index_x >= index_y:
        return
    divide = find_position(list_a, index_x, index_y)
    quick_sort(list_a, index_x, divide - 1)
    quick_sort(list_a, divide + 1, index_y)


A = [random.randint(1, 500) for _ in range(100)]
quick_sort(A, 0, 99)
print(A)
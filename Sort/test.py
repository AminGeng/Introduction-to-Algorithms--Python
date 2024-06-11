import pickle
import random
import time
import os
import sys
current_file_path = os.path.abspath(__file__)
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
test_samples_path = os.path.join(script_dir, 'test_samples.pkl')
# test_List = [[], [1] , 100x[10 values], 100x[100 values], 100x[1000 values], 20x[10^4 values], 2x[10^5 values], [10^6 values]]
testList_listNum_list = [100, 100, 100, 20, 2, 1]
# def make_test_samples():
#     """
#     make test set
#     """
#     test_List = [[], [1]]
#     sorted_test_List = [[], [1]]
#     for i in range(6):
#         n = 10**(i+1)
#         for j in range(testList_listNum_list[i]):
#             test_list = [random.randint(0, 1000) for _ in range(n)]
#             sorted_test_list = sorted(test_list)
#             test_List.append(test_list)
#             sorted_test_List.append(sorted_test_list)
#     save_tuple = (test_List, sorted_test_List)

#     with open(test_samples_path, 'wb') as f:
#         pickle.dump(save_tuple, f)


def test_inplace(sort_func):
    """
    sort_func: argument only list A(call like sort_func(A)), sort A inplace, no return
    """
    with open(test_samples_path, 'rb') as f:
        test_List, sorted_test_List = pickle.load(f)
    for i in range(2):
        try:
            sort_func(test_List[i])
            if test_List[i] != sorted_test_List[i]:
                raise ValueError(f"List {i} is not sorted correctly")
        except Exception as e:
            print(e)
    print("|   | list len| average time|\n| - | ------- | ----------- |")
    for i in range(6):
        total_time = 0
        for j in range(testList_listNum_list[i]):
            list_index = sum(testList_listNum_list[:i])+j+2
            try:
                start = time.time()
                sort_func(test_List[list_index])
                total_time += time.time()- start
                if test_List[list_index] != sorted_test_List[list_index]:
                    raise ValueError(f"List {list_index} is not sorted correctly")
            except Exception as e:
                print(e)
        average_time = total_time * 1000 / testList_listNum_list[i]
        print("| {:1d} |{:9d}|{:10.3f} ms|".format(i+1, 10**(i+1), average_time))
        if average_time > 1000:
            break
        

if __name__ == "__main__":
    from InsertionSort import insert_sort
    from BubbleSort import bubble_sort
    from HeapSort import heap_sort
    from MergeSort import merge_sort
    from QuickSort import quick_sort
    from CountingSort import counting_sort
    from RadixSort import radix_sort
    test_inplace(radix_sort)
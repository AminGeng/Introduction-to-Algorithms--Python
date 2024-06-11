# Introduction-to-Algorithms--Python
用Python基本完成了《算法导论》前六章教材内容，欢迎志同道合之士批评指正，一起探讨学习

## Sort: 7种排序算法
### 前言
- 原址排序

    空间复杂度 O(1): 算法在数组A中重排这些数, 在任何时候, 最多只有其中常数个数字存储在数组外

- 稳定排序

    具有相同值的元素在输出数组中的相对次序与他们在输入数组中的相对次序相同

### 简介 & 测速
- 插入排序: [InsertionSort.py](Sort/InsertionSort.py)
    - 稳定
    - 原址
    - 时间复杂度O(N^2)
    - 适用于小规模输入: 内层循环紧凑

    |   | list len| average time|
    | - | ------- | ----------- |
    | 1 |     10  |     0.001 ms|
    | 2 |    100  |     0.053 ms|
    | 3 |   1000  |     6.479 ms|
    | 4 |  10000  |   687.882 ms|
    | 5 | 100000  | 70917.873 ms|

- 冒泡排序: [BubbleSort.py](Sort/BubbleSort.py)
    - 稳定
    - 原址
    - 时间复杂度O(N^2)
    - 效率非常低: (1)内层循环次数固定; (2)交换操作耗时.
 
    |   | list len| average time|
    | - | ------- | ----------- |
    | 1 |     10  |     0.002 ms|
    | 2 |    100  |     0.140 ms|
    | 3 |   1000  |    18.099 ms|
    | 4 |  10000  |  1858.908 ms|

- 堆排序: [HeapSort.py](Sort/HeapSort.py)
    - 不稳定
    - 原址
    - 时间复杂度O(NlgN)

    |   |list len | average time|
    | - | ------- | ----------- |
    | 1 |     10  |     0.004 ms|
    | 2 |    100  |     0.088 ms|
    | 3 |   1000  |     1.492 ms|
    | 4 |  10000  |    21.951 ms|
    | 5 | 100000  |   293.812 ms|
    | 6 |1000000  |  3891.938 ms|

- 归并排序: [MergeSort.py](Sort/MergeSort.py)
    - 稳定
    - 空间复杂度: N
    - 时间复杂度: NlgN

    |   |list len | average time|
    | - | ------- | ----------- |
    | 1 |     10  |     0.004 ms|
    | 2 |    100  |     0.050 ms|
    | 3 |   1000  |     0.661 ms|
    | 4 |  10000  |     8.031 ms|
    | 5 | 100000  |    92.571 ms|
    | 6 |1000000  |  1080.527 ms|

- 快速排序: [QuickSort.py](Sort/QuickSort.py)
    - 不稳定
    - 空间复杂度: O(1)
    - 时间复杂度: 最好O(NlgN), 最坏O(N^2), 平均O(NLgN)

    |   |list len | average time|
    | - | ------- | ----------- |
    | 1 |     10  |     0.003 ms|
    | 2 |    100  |     0.035 ms|
    | 3 |   1000  |     0.524 ms|
    | 4 |  10000  |     7.070 ms|
    | 5 | 100000  |   143.076 ms|

    *list len 1000000, maximum recursion depth exceeded*

- 计数排序: [CountingSort.py](Sort/CountingSort.py)
    - 稳定 
    - 空间复杂度: O(K+N): 假设所有元素为整数且在区间[x, x+K)
    - 时间复杂度: O(K+N)

    |   | list len| average time|
    | - | ------- | ----------- |
    | 1 |       10|     0.019 ms|
    | 2 |      100|     0.029 ms|
    | 3 |     1000|     0.127 ms|
    | 4 |    10000|     1.084 ms|
    | 5 |   100000|    11.123 ms|
    | 6 |  1000000|   145.962 ms|

- 基数排序: [RadixSort.py](Sort/RadixSort.py)
    - 稳定
    - 空间复杂度: O(N)
    - 时间复杂度: O(D(N+R)): D是整数的位数, N:列表元素总数, R:每一位的数字数, 十进制就是0~9共10个
    - 核心: 取位运算+CountingSort

    |   | list len| average time|
    | - | ------- | ----------- |
    | 1 |       10|     0.007 ms|
    | 2 |      100|     0.048 ms|
    | 3 |     1000|     0.471 ms|
    | 4 |    10000|     4.582 ms|
    | 5 |   100000|    50.087 ms|
    | 6 |  1000000|   629.789 ms|
    
## BinaryTree: 二叉搜索树的各种方法, 最满意的是用海龟制图实现了简单二叉树的绘制
- [Tree.py](BinaryTree/Tree.py): 二叉树的各种方法实现代码
    插入, 删除, 最大, 最小, 前驱, 后继, 高度, 层, 绘制等
- [Example.py](BinaryTree/Example.py): 简单的测试用例

## GraphAlgorithms: 各种图算法
- 深度优先搜索与广度优先搜索: 基于图的邻接链表表示

    - [BFS_AdjacencyList.py](GraphAlgorithms/BFS_AdjacencyList.py)
    - [DFS_AdjacencyList.py](GraphAlgorithms/DFS_AdjacencyList.py)
    - [Example_BFS_DFS.py](GraphAlgorithms/Example_BFS_DFS.py)

- 最小生成树:
    - [Graph_MinimumSpanningTree.py](GraphAlgorithms/Graph_MinimumSpanningTree.py): 最小生成树邻接链表表示法所需要的图类, 带权重无向图.
    - [Kruskal.py](GraphAlgorithms/Kruskal.py): Kruskal算法, 每次选取最小边使用了最小堆, 判断安全边采用不相交集合森林, 其中使用按秩合并与路径压缩来加速.
    - [MinHeap.py](GraphAlgorithms/MinHeap.py): 最小堆
    - [DisjointSet.py](GraphAlgorithms/DisjointSet.py): 不相交集合森林
    - [Prim.py](GraphAlgorithms/Prim.py): Prim算法, 采用斐波那契堆来选取一条新的边
    - [FibonacciHeap.py](GraphAlgorithms/FibonacciHeap.py): 斐波那契堆的基本操作, 由于时间原因, 目前笔者还没有简单实现斐波那契堆的绘制
    - [Example_FibonacciHeap.py](GraphAlgorithms/Example_FibonacciHeap.py): 斐波那契堆的简单示例
    - [Example_MinimunSpanningTree.py](GraphAlgorithms/Example_MinimumSpanningTree.py): 最小生成树的简单示例
- 单源最短路径:
    - [Graph_SingleSourceShortestPaths.py](GraphAlgorithms/Graph_SingleSourceShortestPaths.py): 采用邻接链表表示法, 带权重有向图.
    - [BellmanFold.py](GraphAlgorithms/BellmanFold.py): BellmanFold算法, 可以有负权重, 可以判断是否有负值环路.
    - [TopologicalSortSingleSourceShortestPaths.py](GraphAlgorithms/TopologicalSortSingleSourceShortestPaths.py)：基于有拓扑顺序的有向图, 即有向无环图的单源最短路径.
    - [Dijkstra.py](GraphAlgorithms/Dijkstra.py): Dijkstra算法, 只针对非负值权重, 与Prim算法类似, 采用斐波那契堆加速
    - [FibonacciHeap.py](GraphAlgorithms/FibonacciHeap.py): 还是那个斐波那契堆
    - [Example_SingleSourceShortestPaths.py](GraphAlgorithms/Example_SingleSourceShortestPaths.py): 简单示例
- 所有节点对的最短路径:
    - 下面的算法采用邻接矩阵表示法表示图:
        - [MatrixMultiplyAllPairsShortestPath.py](GraphAlgorithms/MatrixMultiplyAllParisShortestPath.py): 模拟矩阵乘积操作, 实现所有结点对最短路径
        - [MarixMultiplyAllPairsShortestPath_Advanced.py](GraphAlgorithms/MatrixMultiplyAllParisShortestPath_Advanced.py): 模拟矩阵乘法, 进行合并加速.
        - [FloydWarshall.py](GraphAlgorithms/FloydWarshall.py): FloydWarshll算法.
    - 基于稀疏图, 采用邻接链表表示法表示图:
        - [Johnson.py](GraphAlgorithms/Johnson.py): Johnson算法, 通过高度函数, 实现图权重非负化, 从而逐点使用Dijkstra算法
- 最大流: 流网络中最大流的选取
    - [EdmondsKarp.py](GraphAlgorithms/EdmondsKarp.py): 基于残存网络使用广度优先搜索来选取增广路径
    - [GenericPushRelabel.py](GraphAlgorithms/GenericPushRelabel.py): 通用推送-重贴标签算法.
    - [RelabelToFront.py](GraphAlgorithms/RelabelToFront.py): 前置重贴标签算法.

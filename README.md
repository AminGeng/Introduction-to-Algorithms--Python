# Introduction-to-Algorithms--Python
个人用Python基本完成了算法导论前六章教材部分，欢迎志同道合之士批评指正，一起探讨学习

## Sort: 7种排序算法
    冒泡排序: BubbleSort.py
    插入排序: InsertionSort.py
    堆排序: HeapSort.py
    归并排序: MergeSort.py
    快速排序: QuickSort.py
    计数排序: CountingSort.py
    基数排序: RadixSort.py
    
## BinaryTree: 二叉搜索树的各种方法, 最满意的是用海龟制图实现了简单二叉树的绘制
    Tree.py: 二叉树的各种方法实现代码
        插入, 删除, 最大, 最小, 前驱, 后继, 高度, 层, 绘制等
    Example.py: 简单的测试用例

## GraphAlgorithms: 各种图算法
    深度优先搜索与广度优先搜索: 基于图的邻接链表表示
        BFS_AdjacencyList.py
        DFS_AdjacencyList.py
        Example_BFS_DFS.py
    最小生成树:
        Graph_MinimumSpanningTree.py: 最小生成树邻接链表表示法所需要的图类, 带权重无向图.
        Kruskal.py: Kruskal算法, 每次选取最小边使用了最小堆, 判断安全边采用不相交集合森林, 
                    其中使用按秩合并与路径压缩来加速.
            MinHeap.py: 最小堆
            DisjointSet.py: 不相交集合森林
        Prim.py: Prim算法, 采用斐波那契堆来选取一条新的边
            FibonacciHeap.py: 斐波那契堆的基本操作, 时间问题还没有实现斐波那契对的绘制
            Example_FibonacciHeap.py: 斐波那契堆的简单示例
        Example_MinimunSpanningTree.py: 最小生成树的简单示例
    单源最短路径:
        Graph_SingleSourceShortestPaths.py: 采用邻接链表表示法, 带权重有向图.
        BellmanFold.py: BellmanFold算法, 可以有负权重, 可以判断是否有负值环路.
        TopologicalSortSingleSourceShortestPaths.py：基于有拓扑顺序的有向图, 即有向无环图的
                                                     单源最短路径.
        Dijkstra.py: Dijkstra算法, 只针对非负值权重, 与Prim算法类似, 采用斐波那契堆加速
            FibonacciHeap.py: 还是那个斐波那契堆
        Example_SingleSourceShortestPaths.py: 简单示例
    所有节点对的最短路径:
        下面的算法采用邻接矩阵表示法表示图:
            MatrixMultiplyAllPairsShortestPath.py: 模拟矩阵乘积操作, 实现所有结点对最短路径
            MarixMultiplyAllPairsShortestPath_Advanced.py: 模拟矩阵乘法, 进行合并加速.
            FloydWarshall.py: FloydWarshll算法.
        基于稀疏图, 采用邻接链表表示法表示图:
            Johnson.py: Johnson算法, 通过高度函数, 实现图权重非负化, 从而逐点使用Dijkstra算法
    最大流: 流网络中最大流的选取
        EdmondsKarp.py: 基于残存网络使用广度优先搜索来选取增广路径
        GenericPushRelabel.py: 通用推送-重贴标签算法.
        RelabelToFront.py: 前置重贴标签算法.

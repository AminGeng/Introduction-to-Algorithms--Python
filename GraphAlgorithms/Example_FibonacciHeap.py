from FibonacciHeap import *

# 生成结点
i = NodeFib(key='i', value=6)
f = NodeFib(key='f', value=2)
d = NodeFib(key='d', value=float('inf'))
e = NodeFib(key='e', value=float('inf'))
b = NodeFib(key='b', value=11)
a = NodeFib(key='a', value=8)
c = NodeFib(key='c', value=float('inf'))

# 建堆
fib_heap = FibonacciHeap()

# 插入结点
fib_heap.insert(i)
fib_heap.insert(f)
fib_heap.insert(c)
fib_heap.insert(a)
fib_heap.insert(b)
fib_heap.insert(e)
fib_heap.insert(d)

# 打印堆
print('new')
fib_heap.fib_show(fib_heap.min)

# 抽取最小结点, 然后打印堆
print('new')
fib_heap.extract_min()
fib_heap.fib_show(fib_heap.min)

# 减值操作, 然后打印堆
print('new')
fib_heap.decrease_value(c, 4)
fib_heap.fib_show(fib_heap.min)

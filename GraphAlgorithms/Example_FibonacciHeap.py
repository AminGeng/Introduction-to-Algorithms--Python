from FibonacciHeap import *

# for i in range(20):
#     exec('x{}=NodeFib(key={}, value={})'.format(i, i, i))
#
# H = FibonacciHeap()
# h = FibonacciHeap()
#
# for i in range(10):
#     exec('H.insert(x{})'.format(i))
#
# for i in range(10, 20):
#     exec('h.insert(x{})'.format(i))
# print('new')
# h.fib_show(h.min)
#
# h.union(H)
# print('new')
# h.fib_show(h.min)
# h.extract_min()
# print('new')
# h.fib_show(h.min)
# h.decrease_value(x6, 0)
# print('new')
# h.fib_show(h.min)
# h.decrease_value(x7, -1)
# h.delete(x19)
# print('new')
# h.fib_show(h.min)

i = NodeFib(key='i', value=6)
f = NodeFib(key='f', value=2)
d = NodeFib(key='d', value=float('inf'))
e = NodeFib(key='e', value=float('inf'))
b = NodeFib(key='b', value=11)
a = NodeFib(key='a', value=8)
c = NodeFib(key='c', value=float('inf'))
fib_heap = FibonacciHeap()
fib_heap.insert(i)
fib_heap.insert(f)
fib_heap.insert(c)
fib_heap.insert(a)
fib_heap.insert(b)
fib_heap.insert(e)
fib_heap.insert(d)
print('new')
fib_heap.fib_show(fib_heap.min)
fib_heap.extract_min()
print('new')
fib_heap.fib_show(fib_heap.min)
fib_heap.decrease_value(c, 4)
print('new')
fib_heap.fib_show(fib_heap.min)

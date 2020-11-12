from tree import *

import random

l = [random.randint(1, 100) for _ in range(30)]
# l= [13, 100, 29, 18, 83, 86, 46, 29, 71, 70, 57, 92, 93, 98, 74, 79, 44, 86, 29, 2, 36, 94, 21, 42, 98, 4, 87, 82, 52, 42]
print(l)

l_tree = BinaryTree()
l_tree.list2tree(l)
a = l_tree.inorder(l_tree.root)
b = l_tree.preorder(l_tree.root)
c = l_tree.postorder(l_tree.root)
d = l_tree.layers()
h = l_tree.height()
M = l_tree.maximum().val
m = l_tree.minimum().val
s = l_tree.successor(l_tree.root).val
p = l_tree.predecessor(l_tree.root).val
print(a)
print(b)
print(c)
print(d)
print(h)
print(M)
print(m)
print(s)
print(p)
l_tree.draw()
l_tree.delete(l_tree.root)
l_tree.draw()

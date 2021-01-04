from Tree import *

list_tree = [random.randint(1, 100) for _ in range(30)]
i = 0
print(list_tree)

l_tree = BinaryTree()
l_tree.list2tree(list_tree)

print(l_tree.inorder())
print(l_tree.preorder())
print(l_tree.postorder())
print(l_tree.layers())
print(l_tree.height())
print(l_tree.maximum().val)
print(l_tree.minimum().val)
print(l_tree.successor(l_tree.root).val)
print(l_tree.predecessor(l_tree.root).val)

l_tree.draw()
l_tree.delete(l_tree.root)
try:
    print('nil', l_tree.nil.parent.val)
except AttributeError:
    pass
l_tree.draw()

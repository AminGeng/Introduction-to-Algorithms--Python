class NodeFib(object):
    __slots__ = ('key', 'value', 'child', 'parent', 'mark', 'degree', 'par', 'left', 'right')

    def __init__(self, *, key, value=float('inf')):
        self.key = key
        self.value = value
        self.mark = False
        self.parent = None
        self.child = None
        self.degree = 0
        self.par = None


class FibonacciHeap(object):
    def __init__(self):
        self.min = None
        self.number = 0

    def minimum(self):
        if self.number == 0:
            return
        return self.min

    def insert(self, x):
        self.number += 1
        if self.number == 1:
            self.min = x
            x.right = x
            x.left = x
        else:
            min_right = self.min.right
            self.min.right = x
            x.right = min_right
            min_right.left = x
            x.left = self.min
            if self.min.value > x.value:
                self.min = x

    def add_child_list_to_root_list(self, x, y):  # y is x.left equal x is head, y is tail
        # 去掉父指针
        x.parent = None
        x_right = x.right
        while x_right != x:
            x_right.parent = None
            x_right = x_right.right
        # 链接到根链表
        min_right = self.min.right
        x.left = self.min
        self.min.right = x
        y.right = min_right
        min_right.left = y

    def union(self, h):  # 讲斐波那契堆h链接到self上,方法是root_list合并,最后指定最小指针
        if h.number == 0:
            return
        # 连接过程
        self.add_child_list_to_root_list(h.min, h.min.left)
        self.number += h.number
        if self.min.value > h.min.value:
            self.min = h.min

    def root_node_link(self, x, y):  # 将x接到y上
        x.left.right = x.right
        x.right.left = x.left
        x.parent = y
        y.degree += 1
        if y.child:
            child_right = y.child.right
            y.child.right = x
            x.left = y.child
            x.right = child_right
            child_right.left = x
        else:
            y.child = x
            x.left = x
            x.right = x

    def consolidate(self):  # 让根结点的度各不相同,方法是合并相同度的结点
        degree_dict = {self.min.degree: self.min}
        node_x = self.min.right
        while node_x != self.min:
            node_x_right = node_x.right
            n = node_x.degree
            while degree_dict.get(n):
                node_y = degree_dict[n]
                if node_y.value > node_x.value:
                    self.root_node_link(node_y, node_x)
                else:
                    self.root_node_link(node_x, node_y)
                    node_x = node_y
                degree_dict.pop(n)
                n += 1
            degree_dict[n] = node_x
            node_x = node_x_right

    def extract_min(self):  # 去除最小值,并将它的孩子全部放到root_list,然后执行consolidate()
        if self.number == 0:
            return
        self.number -= 1
        h_min = self.min
        if self.number == 0:
            self.min = None
            return h_min
        if self.min.degree > 0:
            min_child = self.min.child
            min_child_left = min_child.left
            self.add_child_list_to_root_list(min_child, min_child_left)
        # 将self.min从根链表中去除
        self.min.left.right = self.min.right
        self.min.right.left = self.min.left
        # 将self.min指向原来的右侧
        self.min = self.min.right
        # 重新寻找min
        p_start = self.min
        p = p_start.right
        while p != p_start:
            if p.value < self.min.value:
                self.min = p
            p = p.right
        self.consolidate()
        return h_min

    def cut(self, x, y):  # remove x from the child list of y, add x to the root list
        x.parent = None
        y.degree -= 1
        if y.degree == 0:
            y.child = None
        else:
            if y.child == x:
                y.child = x.right
            x.left.right = x.right
            x.right.left = x.left
        min_right = self.min.right
        self.min.right = x
        x.left = self.min
        min_right.left = x
        x.right = min_right
        x.mark = False

    def cascading_cut(self, y):  # 级联切断
        if y.parent:
            if not y.mark:
                y.mark = True
            else:
                y_parent = y.parent
                self.cut(y, y_parent)
                self.cascading_cut(y_parent)

    def decrease_value(self, x, k):  # 如果k小于x.parent.key,将x放到root_list里
        if k >= x.value:
            return
        x.value = k
        if x.parent:
            if x.parent.value <= k:
                return
            x_parent = x.parent
            self.cut(x, x_parent)
            self.cascading_cut(x_parent)
        if k < self.min.value:
            self.min = x

    def delete(self, x):
        self.decrease_value(x, -float('inf'))
        self.extract_min()

    def fib_show(self, h):
        if h:
            print('当前位置->', 'key,value:', h.key, h.value, 'degree=', h.degree,'mark=', h.mark,
                  'left:', h.left.key, h.left.value, 'right:', h.right.key, h.right.value)
            if h.parent:
                print('parent:', h.parent.key, h.parent.value)
            else:
                print('parent: None')
            self.fib_show(h.child)
            h_right = h.right
            while h_right != h:
                print('当前位置->', 'key,value:', h_right.key, h_right.value, 'degree=',
                      h_right.degree, 'mark=', h_right.mark,'left:', h_right.left.key,
                      h_right.left.value, 'right:', h_right.right.key, h_right.right.value)
                if h_right.parent:
                    print('parent:', h.parent.key, h.parent.value)
                else:
                    print('parent: None')
                self.fib_show(h_right.child)
                h_right = h_right.right

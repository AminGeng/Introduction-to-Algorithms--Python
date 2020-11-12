from turtle import *
import math


class TreeNode(object):
    __slots__ = ('val', 'parent', 'left', 'right')  # 用来限制属性只能是这几个

    def __init__(self, x=None, *, parent=None, left=None, right=None):
        self.val = x
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.nil = TreeNode()
        self.root = self.nil
        self.inorder_list = []
        self.preorder_list = []
        self.postorder_list = []
        self.layer_list = []

    def transplant(self, node_x, node_y):  # 用y替换x
        node_y.parent = node_x.parent
        if node_x.parent == self.nil:
            self.root = node_y
        elif node_x.parent.left == node_x:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

    def insert(self, node_x):
        if self.root == self.nil:
            self.root = node_x
            self.root.parent = self.nil
            self.root.left = self.nil
            self.root.right = self.nil
            return
        p = self.root
        while p != self.nil:
            y = p
            if node_x.val > p.val:
                p = p.right
            else:
                p = p.left
        node_x.parent = y
        if node_x.val > y.val:
            y.right = node_x
        else:
            y.left = node_x
        node_x.left = self.nil
        node_x.right = self.nil

    def search(self, node_x):  # 查找val等于x节点,并返回指向该结点的指针
        p = self.root
        while p != self.nil:
            if node_x.val > p.val:
                p = p.right
            elif node_x.val < p.val:
                p = p.left
            else:
                return p
        return p

    def maximum(self):
        x = self.root
        while x != self.nil:
            y = x
            x = x.right
        return y

    def minimum(self):
        x = self.root
        while x != self.nil:
            y = x
            x = x.left
        return y

    def successor(self, node_x):
        if node_x.right != self.nil:
            y = node_x.right
            while y != self.nil:
                z = y
                y = y.left
            return z
        else:
            y = node_x.parent
            p = node_x
            while y != self.nil:
                if y.left == p:
                    return y
                else:
                    p = y
                    y = y.parent
        return y

    def predecessor(self, node_x):
        if node_x.left != self.nil:
            y = node_x.left
            while y != self.nil:
                z = y
                y = y.right
            return z
        else:
            y = node_x.parent
            p = node_x
            while y != self.nil:
                if y.right == p:
                    return y
                else:
                    p = y
                    y = y.parent
        return y

    def delete(self, node_x):
        if node_x.left == self.nil:
            self.transplant(node_x, node_x.right)
            if self.root == node_x:
                self.root = node_x.right
        elif node_x.right == self.nil:
            self.transplant(node_x, node_x.left)
            if self.root == node_x:
                self.root = node_x.left
        else:
            y = self.successor(node_x)
            if y == node_x.right:
                self.transplant(node_x, y)
            else:
                self.transplant(y, y.right)
                self.transplant(node_x, y)
                y.right = node_x.right
            y.left = node_x.left

    def list2tree(self, l: list):
        for i in l:
            self.insert(TreeNode(i))

    def inorder(self, x=0):  # 排序结点val值,返回一个列表
        if x == 0:
            x = self.root
        if x == self.root and self.inorder_list:
            self.inorder_list = []
        if x != self.nil:
            self.inorder(x.left)
            self.inorder_list.append(x.val)
            self.inorder(x.right)
        if x == self.root:
            return self.inorder_list

    def preorder(self, x=0):
        if x == 0:
            x == self.root
        if x == self.root and self.preorder_list:
            self.preorder_list = []
        if x != self.nil:
            self.preorder_list.append(x.val)
            self.preorder(x.left)
            self.preorder(x.right)
        if x == self.root:
            return self.preorder_list

    def postorder(self, x=0):
        if x == 0: x = self.root
        if x == self.root and self.postorder_list:
            self.postorder_list = []
        if x != self.nil:
            self.postorder(x.left)
            self.postorder(x.right)
            self.postorder_list.append(x.val)
        if x == self.root:
            return self.postorder_list

    def height(self):
        self.layers()
        return len(self.layer_list) - 1

    def layers(self):
        self.layer_list = []
        if self.root == self.nil:
            return self.layer_list
        layer = [self.root]
        self.layer_list = [[self.root]]
        while layer:
            layer_node_list = []
            for i in layer:
                if i.left != self.nil:
                    layer_node_list.append(i.left)
                if i.right != self.nil:
                    layer_node_list.append(i.right)
            layer = layer_node_list[:]
            if layer:
                self.layer_list.append(layer[:])
        self.layer_list = [[i.val for i in j] for j in self.layer_list]
        return self.layer_list

    def draw(self):
        if self.root == self.nil:
            return
        try:  # 为了防止多次调用时报错:Terminator
            reset()
        except Terminator:
            pass
        mode('logo')
        penup()
        setpos(0, 350)
        pendown()

        def node_circle(node_val, line_degree=120, circle_radius=15, line_length=50, left_or_right='left'):
            nonlocal draw_position
            speed(0)
            setheading(0)
            lt(line_degree)  # 画线
            fd(line_length)
            penup()
            rt(90)  # 画圆
            fd(circle_radius)
            lt(90)
            fd(circle_radius)
            pendown()
            circle(circle_radius)
            circle_draw_position = pos()
            draw_position = circle_position(pos(), heading(), left_or_right=left_or_right)

            penup()  # 写上val
            setpos(draw_position[0], draw_position[1] + circle_radius / 2)
            pendown()
            write(node_val, align='center', font=('Arial', 12, 'normal'))

        def circle_position(circle_coordinates, circle_heading, circle_radius=15, left_or_right='left'):
            x, y = circle_coordinates
            x = x + abs(circle_radius * math.cos(math.radians(circle_heading)))
            if left_or_right == 'left':
                y = y - abs(circle_radius * math.sin(math.radians(circle_heading))) - circle_radius
            else:
                y = y + abs(circle_radius * math.sin(math.radians(circle_heading))) - circle_radius
            return x, y

        radius = 15
        circle(radius)
        draw_position = (-radius, 350 - radius)
        penup()
        setpos(draw_position[0], draw_position[1] + radius / 2)
        pendown()
        write(self.root.val, align='center', font=('Arial', 12, 'normal'))

        self.layer_list = [[(self.root, draw_position)]]
        layer_node_list = [self.root]
        subtract = 0
        degree = 0
        while layer_node_list:
            layer_node_list = []
            for i in self.layer_list[-1]:
                if i[0].left != self.nil:
                    penup()
                    setpos(i[1])
                    pendown()
                    node_circle(i[0].left.val, line_length=180 - subtract, line_degree=100 + degree)
                    layer_node_list.append((i[0].left, draw_position))
                if i[0].right != self.nil:
                    penup()
                    setpos(i[1])
                    pendown()
                    node_circle(i[0].right.val, line_length=180 - subtract, line_degree=260 - degree,
                                left_or_right='right')
                    layer_node_list.append((i[0].right, draw_position))
            subtract += 20
            degree += 9
            if layer_node_list:
                self.layer_list.append(layer_node_list[:])
        penup()
        setheading(180)
        fd(radius)
        done()

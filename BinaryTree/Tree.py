# 实现的二叉树操作有:
# 寻找, 插入, 删除, 最大, 最小, 前驱, 后继, 中序遍历, 前序遍历, 后序遍历, 高度, 层
# 为了方便看二叉树, 加入了draw, 用来绘制简单的二叉树
from turtle import *
import math
import random


class TreeNode(object):
    __slots__ = ('val', 'parent', 'left', 'right')  # 用来限制属性只能是这几个

    def __init__(self, value=None):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree(object):
    # 初始生成一个空树, self.nil是dummy node
    def __init__(self):
        self.nil = TreeNode()
        self.root = self.nil

    # 将node_x插入树中, 找到满足(1), (2)条件之一的结点A, 所以node_x插入树中之后左右孩子都是叶节点.
    # (1)结点A左子树是nil, 且node_x值<= A.val, node_x成为A的左孩子, 并将node_x的左右孩子设置为nil
    # (2)结点A右子树是nil, 且node_x值> A.val, node_x成为A的右孩子, 并将node_x的左右孩子设置为nil
    def insert(self, node_x):
        node_x.left = self.nil
        node_x.right = self.nil
        if self.root == self.nil:
            self.root = node_x
            self.root.parent = self.nil
            return
        pointer = self.root
        while pointer != self.nil:
            pre_pointer = pointer
            if node_x.val > pointer.val:
                pointer = pointer.right
            else:
                pointer = pointer.left
        node_x.parent = pre_pointer
        if node_x.val > pre_pointer.val:
            pre_pointer.right = node_x
        else:
            pre_pointer.left = node_x
        node_x.left = self.nil
        node_x.right = self.nil

    # 在树中寻找第一个结点.val==node_x.val的结点
    # 未找到返回None
    def search(self, node_x):  # 查找val等于x节点,并返回指向该结点的指针
        pointer = self.root
        while pointer != self.nil:
            if node_x.val > pointer.val:
                pointer = pointer.right
            elif node_x.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer
        return None

    # 寻找树中的结点val最大值的结点: 最右侧结点
    # 空树返回None
    def maximum(self):
        if self.root == self.nil:
            return None
        pointer = self.root
        while pointer != self.nil:
            pre_pointer = pointer
            pointer = pointer.right
        return pre_pointer

    # 寻找树中的结点val最小值的结点: 最右侧结点
    # 空树返回None
    def minimum(self):
        if self.root == self.nil:
            return None
        pointer = self.root
        while pointer != self.nil:
            pre_pointer = pointer
            pointer = pointer.left
        return pre_pointer

    # 寻找树中值大于等于node_x的值得结点中值最小的一个, 就是大于等于它的最小值
    # 寻找守则: 右子树存在, 右子树的最左侧结点, 不存在, 找它作为左子树结点的最近祖先
    # 有返回结点, 没有返回None
    # 由于树中规则是右侧严格大于, 左侧小于等于, 所以结点无右孩子向上寻找时, 可能找到等于它的值(下面续)
    # 续: 此时, 若没有找到满足条件的结点, 可能它的左子树中有等于它的值的结点, 此情况这里没有讨论, 有需要可以加入.
    def successor(self, node_x):
        if node_x.right != self.nil:
            pointer = node_x.right
            while pointer != self.nil:
                pre_pointer = pointer
                pointer = pointer.left
            return pre_pointer
        else:
            pointer = node_x.parent
            pre_pointer = node_x
            while pointer != self.nil:
                if pointer.left == pre_pointer:
                    return pointer
                else:
                    pre_pointer = pointer
                    pointer = pointer.parent
        return None

    # 寻找树中值小于等于node_x的值得结点中值最大的一个, 就是小于等于它的最大值
    # 寻找守则: 左子树存在, 左子树的最右侧结点, 不存在, 找它作为右子树结点的最近祖先
    # 有返回结点, 没有返回None
    # 不会出现successor类似情况
    def predecessor(self, node_x):
        if node_x.left != self.nil:
            pointer = node_x.left
            while pointer != self.nil:
                pre_pointer = pointer
                pointer = pointer.right
            return pre_pointer
        else:
            pointer = node_x.parent
            pre_pointer = node_x
            while pointer != self.nil:
                if pointer.right == pre_pointer:
                    return pointer
                else:
                    pre_pointer = pointer
                    pointer = pointer.parent
        return None

    # 用node_y替代node_x
    # 此操作不改变node_y的孩子情况
    def transplant(self, node_x, node_y):
        node_y.parent = node_x.parent
        if node_x.parent == self.nil:
            self.root = node_y
        elif node_x.parent.left == node_x:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

    # 删除结点操作, 比较复杂一些些.
    # 守则: 该结点左右子树有一个为空, 用另一个替代该结点即可, 调用transplant()
    # 守则续: 若左右子树都不空, 则找大于它的后继(此时一定在右子树中), 用后继的右子树替代后继(后继的左子树一定为空), 用后继替代该结点.
    # 守则续: 此时两次调用transplant()
    # 有一个问题: 替代为后继时, 会给nil制定parent, 目前没有发现啥问题, 但是还是注意下.
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
            x_successor = self.successor(node_x)
            self.transplant(x_successor, x_successor.right)
            self.transplant(node_x, x_successor)
            x_successor.right = node_x.right
            x_successor.left = node_x.left

    # 将list转化为二叉树
    # 守则: 依次调用insert, 将val为list中的元素的结点一一插入树中.
    # shuttle: 是否需要打乱列表中元素顺序, 若列表严格排序, 树就是树干了, 一个分支都没有.
    def list2tree(self, list_tree, *, shuffle=False):
        if shuffle:
            random.shuffle(list_tree)
        for i in list_tree:
            self.insert(TreeNode(i))

    # 中序遍历树, 返回中序遍历结点val列表
    # 此时为从小到大的排序
    def inorder(self) -> list:  # 排序结点val值,返回一个列表
        if self.root == self.nil:
            return []
        inorder_list = []

        def add_to_list(node_x):
            if node_x.left != self.nil:
                add_to_list(node_x.left)
            inorder_list.append(node_x.val)
            if node_x.right != self.nil:
                add_to_list(node_x.right)

        add_to_list(self.root)
        return inorder_list

    # 前序遍历树, 返回前序遍历结点val列表
    # 此时一个结点后面是它的左子树然后右子树, 分形处理
    def preorder(self, x=0):
        if self.root == self.nil:
            return []
        preorder_list = []

        def add_to_list(node_x):
            preorder_list.append(node_x.val)
            if node_x.left != self.nil:
                add_to_list(node_x.left)
            if node_x.right != self.nil:
                add_to_list(node_x.right)

        add_to_list(self.root)
        return preorder_list

    # 后序遍历树, 返回后序遍历结点val列表
    # 此时一个结点的前面是它的左子树和右子树, 分形处理
    def postorder(self, x=0):
        if self.root == self.nil:
            return []
        postorder_list = []

        def add_to_list(node_x):
            if node_x.left != self.nil:
                add_to_list(node_x.left)
            if node_x.right != self.nil:
                add_to_list(node_x.right)
            postorder_list.append(node_x.val)

        add_to_list(self.root)
        return postorder_list

    # 返回层列表, 元素是每层结点val
    def layers(self) -> list:
        if self.root == self.nil:
            return []
        layer_node_list = []
        layer_current = [self.root]
        while layer_current:
            layer_node_list.append(layer_current)
            layer_next = []
            for i in layer_current:
                if i.left != self.nil:
                    layer_next.append(i.left)
                if i.right != self.nil:
                    layer_next.append(i.right)
            layer_current = layer_next

        layer_list = [[i.val for i in j] for j in layer_node_list]
        return layer_list

    # 返回数层数
    # 最底层是0层, 所以空树返回-1
    def height(self) -> int:
        return len(self.layers()) - 1

    # 画出二叉树
    # 由于画图过程中, 设置越靠近底部, 每次两引线夹角-9*2(初始80*2), 引线长-20(初始180), 所以理论最多8层, 然后左右子树角度不再争取
    # 问题, 没有加入滚动条, 绘制时可能会出现溢出屏幕无法看见个别结点情况
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

        # 找到结点圆的圆心位置
        def circle_center_position(circle_coordinates, circle_heading, circle_radius=15, left_or_right='left'):
            x, y = circle_coordinates
            x = x + abs(circle_radius * math.cos(math.radians(circle_heading)))
            if left_or_right == 'left':
                y = y - abs(circle_radius * math.sin(math.radians(circle_heading)))
            else:
                y = y + abs(circle_radius * math.sin(math.radians(circle_heading)))
            return x, y

        # 画出引出结点的线和结点, 并在结点内部写上结点的数值
        def node_circle(node_val, line_degree=120, line_length=50, circle_radius=15, left_or_right='left'):
            nonlocal draw_position
            speed(0)
            setheading(0)  # 朝上
            # 画出引出结点的线
            lt(line_degree)
            fd(line_length)

            # 记此时位置为A, 由于此模式下, 画的圆在前进方向左侧, 切点为A, 为了画出前进线指向圆心, 线圆交点为A的圆所以需要移动指针位置
            # 方法是右走半径长, 然后左走半径长再画圆
            penup()
            rt(90)
            fd(circle_radius)
            lt(90)
            fd(circle_radius)
            pendown()
            circle(circle_radius)

            # 记此时位置为A, 书写数值以A为起点, 水平向右写, A在数值左下角
            # 下面先找到数值开始书写的位置, 然后写上合适字体与大小的数值
            draw_position = circle_center_position(pos(), heading(), left_or_right=left_or_right)
            penup()
            setpos(draw_position[0], draw_position[1] - circle_radius / 2)
            pendown()
            write(node_val, align='center', font=('Arial', 12, 'normal'))

        radius = 15
        circle(radius)
        draw_position = (-radius, 350)
        penup()
        setpos(draw_position[0], draw_position[1] - radius / 2)
        pendown()
        write(self.root.val, align='center', font=('Arial', 12, 'normal'))
        # layer_current: 放入当前层的结点和其孩子结点引线开始位置
        layer_current = [(self.root, (draw_position[0], draw_position[1] - radius))]
        # line_length_subtract设置每层结点引线减少长度
        line_length_subtract = 0
        # degree_subtract设置每层结点引线角度减少度数/2, 因为左右都减少
        degree_subtract = 0
        # 每次绘制的是当前层的下一层
        while layer_current:
            # 放入下一层结点及其孩子结点引线开始位置
            layer_next = []
            for node_i in layer_current:
                if node_i[0].left != self.nil:
                    penup()
                    setpos(node_i[1])
                    pendown()
                    # line_degree: setheading(0)是朝正上方, 所以+degree_subtract会使左右引线夹角随层数慢慢减小
                    # +random.randint(-4, 4)是为了尽量减少画图时出现结点覆盖的现象
                    node_circle(node_i[0].left.val, line_length=180 - line_length_subtract + random.randint(-4, 4),
                                line_degree=100 + degree_subtract + random.randint(-4, 4))
                    layer_next.append((node_i[0].left, (draw_position[0], draw_position[1] - radius)))
                if node_i[0].right != self.nil:
                    penup()
                    setpos(node_i[1])
                    pendown()
                    node_circle(node_i[0].right.val, line_length=180 - line_length_subtract + random.randint(-4, 4),
                                line_degree=260 - degree_subtract + random.randint(-4, 4),
                                left_or_right='right')
                    layer_next.append((node_i[0].right, (draw_position[0], draw_position[1] - radius)))
            line_length_subtract += 20
            degree_subtract += 9
            layer_current = layer_next
        # 为了让结束之后的箭头在结点圆外而不是圆内会挡住数值
        penup()
        setheading(180)
        fd(radius)
        done()

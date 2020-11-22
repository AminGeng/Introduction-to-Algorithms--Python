# FibonacciHeap: 斐波那契堆; 是一种mergeable heap(可合并堆)
# 包含建堆, 插入, 查找最小值, 抽取最小值, 合并堆, 减值, 删除7种操作, 其中前5种是每个可合并堆都要支持的
# 摊还分析势函数是t(h)+2m(h): t(h): h的根结点数目; m(h): h中mark==True的结点的数目.
# 建堆, 插入, 查找最小值, 合并堆, 减值的摊还代价为O(1)
# 抽取最小值, 删除的摊还代价为O(lgn)


# 斐波那契堆所需要的的结点
class NodeFib(object):
    # key:结点名称, value:结点值, child:结点的孩子(结点有双向孩子链, child只指向孩子链中一个), parent:双亲
    # mark:标记(减值操作时进行更改), degree:度数(它的孩子数), left:左结点, right:右节点(因为是双向链表的结点)
    # par: 为了在Prim算法中引起结点减值操作的顶点, 不是斐波那契堆操作中需要的属性.
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
    # self.min指向value最小的根结点, 也是所有结点中value最小的
    # self.number记录堆中的结点数
    def __init__(self):
        self.min = None
        self.number = 0

    # 查询操作,返回最小结点
    # 摊还代价O(1)
    def minimum(self):
        if self.number == 0:
            return
        return self.min

    # 插入操作
    # 直接将新结点插入到root链中
    # 摊还代价O(1)
    def insert(self, x):
        self.number += 1
        # 空链表直接作为唯一结点
        if self.number == 1:
            self.min = x
            x.right = x
            x.left = x
        else:
            # 插入方案是插到原来min结点的右侧
            min_right = self.min.right
            self.min.right = x
            x.right = min_right
            min_right.left = x
            x.left = self.min
            # 根据新结点的值判断是否更改min指针
            if self.min.value > x.value:
                self.min = x

    # 将孩子链插入根链中, x是孩子链的头, y是x的left, 算做尾吧, 因为双向链表其实无所谓头尾.
    # 插入原则依旧是插入到min指针右侧
    # union和extract_min操作中用到
    def add_child_list_to_root_list(self, x, y):
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

    # 合并堆操作
    # 将斐波那契堆h链接到self上,方法是root链合并,最后指定最小指针
    # 摊还代价O(1)
    def union(self, h):
        if h.number == 0:
            return
        # 连接过程
        self.add_child_list_to_root_list(h.min, h.min.left)
        self.number += h.number
        # 判断是否更新min指针
        if self.min.value > h.min.value:
            self.min = h.min

    # 将根结点x插入到根结点y的孩子链中
    # consolidate操作中用到
    def root_node_link(self, x, y):
        # 根链中删除x
        x.left.right = x.right
        x.right.left = x.left
        x.parent = y
        y.degree += 1
        # 如果y的孩子链非空, 将x插入到y孩子指针所指结点的右侧.
        if y.child:
            child_right = y.child.right
            y.child.right = x
            x.left = y.child
            x.right = child_right
            child_right.left = x
        # 如果y的孩子链空, 直接指定x为y的唯一孩子.
        else:
            y.child = x
            x.left = x
            x.right = x

    # 这一步是FibonacciHeap的精髓所在
    # extract_min时用到
    # 通过合并相同degree的结点, 使根结点的degree各不相同
    def consolidate(self):
        # 合并两个相同degree结点时, 会将value较大的并到value较小的孩子链中
        # 从min开始, 右向搜索, 因为min的value最小, 会永远在root链中
        # degree_dict: 存放检索过的根结点的degree, 该degree所属的结点; key: degree, value: 结点
        degree_dict = {self.min.degree: self.min}
        node_x = self.min.right
        while node_x != self.min:
            node_x_right = node_x.right
            n = node_x.degree
            # 判断是否已经存在degree为n的结点
            while degree_dict.get(n):
                node_y = degree_dict[n]
                # 合并两个degree相同结点
                # node_x始终在根链中
                if node_y.value > node_x.value:
                    self.root_node_link(node_y, node_x)
                else:
                    self.root_node_link(node_x, node_y)
                    node_x = node_y
                # 合并之后, 检索过的根结点中将不再存在degree为n的结点, 所以degree_dict删除n
                degree_dict.pop(n)
                # 但检索过的根结点中会出现degree为n+1的结点, 所以进入循环.
                n += 1
            # 更新degree_dict, 继续向右检索.
            degree_dict[n] = node_x
            node_x = node_x_right

    # 关键关键操作!!!
    # 抽取最小结点,并将它的孩子全部放到root_list,然后执行consolidate()
    # 摊还代价O(lgn)
    # 实际代价O(t(h)+D(h)); 势的变化: O(D(h)+1)+2m(h)-O(t(h))-2m(h); 实际+势, 通过改变势函数中t(h)的系数, 可以摊还为O(lgn)
    # D(h)是最大的根degree, 在整个consolidate过程中, 可以发现根合并与斐波那契数列规律一致, 所以D(h)为O(lgn)
    def extract_min(self):
        # 如果是空堆, 返回None
        if self.number == 0:
            return
        self.number -= 1
        h_min = self.min
        # 如果堆中只有一个结点, 那直接取出, 并将堆设为空堆.
        if self.number == 0:
            self.min = None
            return h_min
        # 如果最小值有孩子链, 将孩子链插入到root链中
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
        # 运行堆调控操作, 这一步是关键!
        self.consolidate()
        return h_min

    # 切断操作
    # x.parent == y
    # 将x从y的孩子链中取出, 放到root链中
    # decrease_value操作用到
    def cut(self, x, y):
        x.parent = None
        y.degree -= 1
        if y.degree == 0:
            y.child = None
        # 重整y的孩子链表
        else:
            if y.child == x:
                y.child = x.right
            x.left.right = x.right
            x.right.left = x.left
        # 将x插入到root链中
        min_right = self.min.right
        self.min.right = x
        x.left = self.min
        min_right.left = x
        x.right = min_right
        x.mark = False

    # 级联切断
    # 根据结点的mark信息, 决定是否级联切断
    # mark == True切断
    # decrease_value操作用到
    def cascading_cut(self, y):
        if y.parent:
            if not y.mark:
                y.mark = True
            else:
                y_parent = y.parent
                self.cut(y, y_parent)
                self.cascading_cut(y_parent)

    # 结点减值操作
    # 如果减值后当前结点的value, 小于x.parent.value, 将x放到root_list里
    # 根据减值结点的父节点mark信息, 判断是否进行级联切断.
    # 摊还代价为O(1)
    # 这里是m(h)的用处, 进行一次级联操作, t(h)+1, 2m(h)-2, 所以势函数改变量是级联操作的正比, 实际代价也是级联操作的正比
    def decrease_value(self, x, k):
        # 判断是否是合格的减值
        if k >= x.value:
            return
        x.value = k
        # 根据x.parent的情况判断是否进行切断和级联切断.
        if x.parent:
            if x.parent.value <= k:
                return
            x_parent = x.parent
            self.cut(x, x_parent)
            self.cascading_cut(x_parent)
        # 判断是否更新min指针
        if k < self.min.value:
            self.min = x

    # 删除结点操作
    # 减值到-infinite, 然后运行取出最小值操作.
    def delete(self, x):
        self.decrease_value(x, -float('inf'))
        self.extract_min()

    # 此操作不属于堆的操作, 只是为了笔者方便查看堆信息
    # 通过打印出结点的key, value, degree, parent等信息, 简单版的展示堆的结构, 需要自己按照打印信息进行绘制
    # h是打印开始结点
    def fib_show(self, h):
        if h:
            print('当前位置->', 'key,value:', h.key, h.value, 'degree=', h.degree, 'mark=', h.mark,
                  'left:', h.left.key, h.left.value, 'right:', h.right.key, h.right.value)
            if h.parent:
                print('parent:', h.parent.key, h.parent.value)
            else:
                print('parent: None')
            self.fib_show(h.child)
            h_right = h.right
            # 打印顺序, 深度优先.
            while h_right != h:
                print('当前位置->', 'key,value:', h_right.key, h_right.value, 'degree=',
                      h_right.degree, 'mark=', h_right.mark, 'left:', h_right.left.key,
                      h_right.left.value, 'right:', h_right.right.key, h_right.right.value)
                if h_right.parent:
                    print('parent:', h.parent.key, h.parent.value)
                else:
                    print('parent: None')
                self.fib_show(h_right.child)
                h_right = h_right.right

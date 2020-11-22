# 数据结构: 不相交集合森林, 使用有根树来表示集合, Kruskal算法用到
# 有根树中根结点是唯一父指针指向自己的结点
# 支持建树, 查找根结点, 合并两棵树3个操作(建树是创建一棵只有根结点的树)
# 通过按秩合并和路径压缩两种方法, 可以证明对于任意m个操作序列(其中n个建树操作), 最坏运行时间为O(mα(n)), 其中α(n)<=4.

# 不相交集合森林所需结点
class NodeDisjointSet(object):
    # rank:秩(有根树的可能最大高度), parent:父指针, key:结点关键字, 即它的名字.
    __slots__ = ('rank', 'parent', 'key')

    # 建树操作等价于创建一个根结点, 所以初始化父指针指向自己.
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0


# 字典, 用来存储结点的key与key对应的结点, 方便快速定位结点, 即key:顶点(字符串, 结点的key, 及结点的名字), value:key对应结点
key_dict = {}


# 建树
# x结点的key, 即结点的名字, 字符串
def make_set(x):
    key_dict[x] = NodeDisjointSet(x)


# 关键步骤: 路径压缩
# 查找x的顶层结点, 将查找路径上的每一个结点的父指针都指向顶层结点, 即为路径压缩.
# x是结点
def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


# 按秩合并的关键操作,
# 如果x的秩大于y的秩, y变为x的孩子; 否则, x变为y的孩子, 若x的秩与y的秩相等, y的秩+1
def link(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# 合并x和y所在的集合
# 先找到x和y所在的链表的根结点, 然后对两个根结点执行按秩合并.
def union(x, y):
    link(find_set(x), find_set(y))

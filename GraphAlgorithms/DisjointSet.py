# union by rank
# path compression


class NodeDisjointSet(object):
    __slots__ = ('rank', 'parent', 'key')

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.rank = 0


key_dict = {}


def make_set(x):  # x is a key
    x = NodeDisjointSet(x)
    key_dict[x.key] = x
    x.parent = x
    x.rank = 0


# path compression
def find_set(x):  # x is a Node
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


# link by rank
def link(x, y):  # x, y are Nodes
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# union by rank
def union(x, y):  # x, y are Nodes
    link(find_set(x), find_set(y))

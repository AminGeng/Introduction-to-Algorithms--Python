# Ford-Fulkerson方法的一个具体实现算法,在残存网络中使用广度优先搜索寻找增广路径.
# O(VE^2)
from copy import deepcopy
from collections import deque


class GraphFlow(object):
    __slots__ = ('vertices', 'adj_v', 'edge_c', 'key_dict')

    def __init__(self, *, vertices=None, edge_capacity=None):
        self.vertices = vertices
        self.edge_c = edge_capacity  # edge capacity 边容量
        self.adj_v = self.edge_c2adj_v(edge_capacity)
        self.key_dict = self.set_key_dict(vertices)

    class Vertex(object):
        __slots__ = ('key', 'color', 'parent')

        def __init__(self, key, *, parent=None, color='white'):
            self.key = key
            self.parent = parent
            self.color = color

    def set_key_dict(self, vertices):
        key_dict = {}
        for i in vertices:
            key_dict[i] = self.Vertex(i)
        return key_dict

    def edge_c2adj_v(self, edge_capacity):
        adjacency_vertices = dict((i, set()) for i in self.vertices)
        for i in edge_capacity.keys():
            adjacency_vertices[i[0]].add(i[1])
        return adjacency_vertices


def bfs(G, s, t):
    key_dict = G.key_dict
    for i in G.vertices:
        key_dict[i].color = 'white'
        key_dict[i].parent = None
    key_dict[s].color = 'black'
    v_deque = deque(s)
    while v_deque:
        v_current = v_deque.popleft()  # deque可以在O(1)的时间内完成左侧去掉, 而list需要O(n)
        for v_i in G.adj_v[v_current]:
            if v_i == t:
                aug_path = deque([v_current, t])
                v_par = key_dict[v_current].parent
                while v_par:
                    aug_path.appendleft(v_par.key)
                    v_par = v_par.parent
                return aug_path
            elif key_dict[v_i].color == 'white':
                key_dict[v_i].color = 'black'
                key_dict[v_i].parent = key_dict[v_current]
                v_deque.append(v_i)
    return False


def edmonds_karp(G, s, t):
    res_net = deepcopy(G)  # residual network 残存网络
    aug_path = bfs(res_net, s, t)  # augmentation path:增广路径
    flow = dict((i, 0) for i in res_net.edge_c.keys())
    while aug_path:
        path_flow = res_net.edge_c[(aug_path[0], aug_path[1])]
        for i in range(1, len(aug_path) - 1):
            if path_flow > res_net.edge_c[(aug_path[i], aug_path[i + 1])]:
                path_flow = res_net.edge_c[(aug_path[i], aug_path[i + 1])]
        for i in range(len(aug_path) - 1):
            res_net.edge_c[(aug_path[i], aug_path[i + 1])] -= path_flow
            if res_net.edge_c[(aug_path[i], aug_path[i + 1])] == 0:
                res_net.edge_c.pop((aug_path[i], aug_path[i + 1]))
                res_net.adj_v[aug_path[i]].remove(aug_path[i + 1])
            if (aug_path[i + 1], aug_path[i]) in res_net.edge_c:
                res_net.edge_c[(aug_path[i + 1], aug_path[i])] += path_flow
            else:
                res_net.edge_c[(aug_path[i + 1], aug_path[i])] = path_flow
                res_net.adj_v[aug_path[i + 1]].add(aug_path[i])
            if (aug_path[i], aug_path[i + 1]) in flow:
                flow[(aug_path[i], aug_path[i + 1])] += path_flow
            else:
                flow[(aug_path[i + 1], aug_path[i])] -= path_flow
        aug_path = bfs(res_net, s, t)
    return flow


v = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
e = {('s', 'v1'): 12, ('s', 'v2'): 13, ('v1', 'v3'): 12, ('v2', 'v1'): 4, ('v2', 'v4'): 14,
     ('v3', 'v2'): 9, ('v3', 't'): 20, ('v4', 'v3'): 7, ('v4', 't'): 4}
G = GraphFlow(vertices=v, edge_capacity=e)

print(edmonds_karp(G, 's', 't'))

# O(v^3)


from copy import deepcopy


class GraphFlow(object):
    __slots__ = ('vertices', 'adj_v', 'edge_c', 'key_dict')

    def __init__(self, *, vertices=None, edge_capacity=None):
        self.vertices = vertices
        self.edge_c = edge_capacity
        self.adj_v = self.edge_c2adj_v(edge_capacity)
        self.key_dict = self.set_key_dict(vertices)

    class Vertex(object):
        __slots__ = ('height', 'excess_flow')

        def __init__(self, *, height=0, excess_flow=0):
            self.height = height
            self.excess_flow = excess_flow

    def set_key_dict(self, vertices):
        key_dict = {}
        for i in vertices:
            key_dict[i] = self.Vertex()
        return key_dict

    def edge_c2adj_v(self, edge_capacity):
        adjacency_vertices = dict((i, set()) for i in self.vertices)  # 因为需要进入循环,改变大小
        for i in edge_capacity.keys():
            adjacency_vertices[i[0]].add(i[1])
        return adjacency_vertices


def push(G, u, v, delta, flow):
    G.key_dict[u].excess_flow -= delta
    G.key_dict[v].excess_flow += delta
    G.edge_c[(u, v)] -= delta
    if G.edge_c[(u, v)] == 0:
        G.edge_c.pop((u, v))
        G.adj_v[u].remove(v)
    if (u, v) in flow:
        flow[(u, v)] += delta
    else:
        flow[(v, u)] -= delta
    if (v, u) in G.edge_c:
        G.edge_c[(v, u)] += delta
    else:
        G.edge_c[(v, u)] = delta
        G.adj_v[v].add(u)


def relabel(G, e):
    h = min(G.key_dict[i].height for i in G.adj_v[e])
    G.key_dict[e].height = h + 1


def discharge(G, u, l, flow):
    while G.key_dict[u].excess_flow > 0:
        current_index = l[0]
        if current_index == len(l):
            relabel(G, u)
            l[0] = 1
        elif (u, l[current_index]) in G.edge_c and G.key_dict[u].height == G.key_dict[l[current_index]].height + 1:
            delta = min(G.key_dict[u].excess_flow, G.edge_c[(u, l[current_index])])
            push(G, u, l[current_index], delta, flow)
        else:
            l[0] += 1


def relabel2front(G, s, t):
    class Node(object):
        __slots__ = ('key', 'next')

        def __init__(self, key):
            self.key = key
            self.next = None

    res_net = deepcopy(G)  # residual network 剩余网络,残存网络
    topo_list = Node('head')  # topological sort list

    l_current = topo_list
    for v_j in res_net.vertices:
        if v_j != s and v_j != t:
            l_current.next = Node(v_j)
            l_current = l_current.next

    v_possible_dict = dict((i, [0]) for i in res_net.vertices)
    for e_i in res_net.edge_c.keys():
        v_possible_dict[e_i[0]].append(e_i[1])
        v_possible_dict[e_i[1]].append(e_i[0])

    key_dict = res_net.key_dict
    key_dict[s].height = len(res_net.vertices)
    flow = dict((i, 0) for i in res_net.edge_c.keys())
    for v_i in res_net.adj_v[s]:
        flow[(s, v_i)] = res_net.edge_c[(s, v_i)]
        key_dict[v_i].excess_flow = flow[(s, v_i)]
        res_net.edge_c[(v_i, s)] = res_net.edge_c.pop((s, v_i))
        res_net.adj_v[v_i].add(s)
    res_net.adj_v[s] = set()

    l_current = topo_list.next
    l_current_pre = topo_list
    while l_current:
        old_height = key_dict[l_current.key].height
        discharge(res_net, l_current.key, v_possible_dict[l_current.key], flow)
        if key_dict[l_current.key].height > old_height:
            l_current_pre.next = l_current.next
            l_current.next = topo_list.next
            topo_list.next = l_current
            l_current_pre = topo_list
        else:
            l_current_pre = l_current
            l_current = l_current.next

    return flow


v = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
e = {('s', 'v1'): 12, ('s', 'v2'): 13, ('v1', 'v3'): 12, ('v2', 'v1'): 4, ('v2', 'v4'): 14,
     ('v3', 'v2'): 9, ('v3', 't'): 20, ('v4', 'v3'): 7, ('v4', 't'): 4}
G = GraphFlow(vertices=v, edge_capacity=e)

print(relabel2front(G, 's', 't'))

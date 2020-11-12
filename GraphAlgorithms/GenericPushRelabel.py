# Goldberg的通用最大流算法
# 最大流算法的最快实现基于推送重贴标签算法
# O(v^2E)


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


def generic_push_relabel(G, s, t):
    res_net = deepcopy(G)  # residual network 剩余网络,残存网络
    key_dict = res_net.key_dict
    key_dict[s].height = len(res_net.vertices)
    flow = dict((i, 0) for i in res_net.edge_c.keys())
    excess_flow_v = set()
    for v_i in res_net.adj_v[s]:
        flow[(s, v_i)] = res_net.edge_c[(s, v_i)]
        key_dict[v_i].excess_flow = flow[(s, v_i)]
        if v_i != t:
            excess_flow_v.add(v_i)
        res_net.edge_c[(v_i, s)] = res_net.edge_c.pop((s, v_i))
        res_net.adj_v[v_i].add(s)
    res_net.adj_v[s] = set()
    while excess_flow_v:
        e_v = excess_flow_v.pop()
        remove_set = set()
        for v_i in res_net.adj_v[e_v]:
            if key_dict[v_i].height == key_dict[e_v].height - 1 and (e_v, v_i) in res_net.edge_c:
                delta = min(key_dict[e_v].excess_flow, res_net.edge_c[(e_v, v_i)])
                push(res_net, e_v, v_i, delta, flow)
                if res_net.edge_c[(e_v, v_i)] == 0:
                    res_net.edge_c.pop((e_v, v_i))
                    remove_set.add(v_i)  # 不能改变循环体中的集合大小
                if v_i != t and v_i != s:
                    excess_flow_v.add(v_i)
                if key_dict[e_v].excess_flow == 0:
                    break
        res_net.adj_v[e_v].difference_update(remove_set)
        if key_dict[e_v].excess_flow == 0:
            continue
        excess_flow_v.add(e_v)
        relabel(res_net, e_v)
    return flow


v = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
e = {('s', 'v1'): 12, ('s', 'v2'): 13, ('v1', 'v3'): 12, ('v2', 'v1'): 4, ('v2', 'v4'): 14,
     ('v3', 'v2'): 9, ('v3', 't'): 20, ('v4', 'v3'): 7, ('v4', 't'): 4}
G = GraphFlow(vertices=v, edge_capacity=e)

print(generic_push_relabel(G, 's', 't'))

# 无权重最短路径
from collections import deque


class GraphAdjacencyList(object):
    def __init__(self, *, vertices, adjacency_list):
        self.vertices = vertices  # Node形式的顶点
        self.adjacency_list = adjacency_list  # key: str, 顶点名; value:list, [str1,str2,...]与它相连的顶点名


def breath_first_search(G, s):
    class Vertex(object):
        __slots__ = ('key', 'color', 'parent', 'distance')

        def __init__(self, key, *, parent=None, distance=float('infinity'), color='white'):
            self.key = key
            self.parent = parent
            self.distance = distance
            self.color = color

    key_dict = {}
    for vertex_i in G.vertices:
        key_dict[vertex_i] = Vertex(vertex_i)

    key_dict[s].color = 'black'
    key_dict[s].distance = 0
    vertex_deque = deque(s)
    while vertex_deque:
        vertex_current = vertex_deque.popleft()  # deque可以在O(1)的时间内完成左侧去掉, 而list需要O(n)
        for vertex_i in G.adjacency_list[vertex_current]:
            if key_dict[vertex_i].color == 'white':
                key_dict[vertex_i].color = 'black'
                key_dict[vertex_i].distance = key_dict[vertex_current].distance + 1
                key_dict[vertex_i].parent = key_dict[vertex_current]
                vertex_deque.append(vertex_i)
    distance_list = []
    for vertex_i in G.vertices:
        path_deque = deque(vertex_i)
        i_parent = key_dict[vertex_i].parent
        while i_parent:
            path_deque.appendleft(i_parent.key)
            i_parent = i_parent.parent
        distance_list.append((vertex_i, key_dict[vertex_i].distance, path_deque))
    return distance_list
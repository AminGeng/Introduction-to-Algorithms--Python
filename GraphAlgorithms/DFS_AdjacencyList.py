# Topological_Sort
# Strongly_connected_components
from copy import deepcopy


class GraphAdjacencyList(object):
    def __init__(self, *, vertices, adjacency_list):
        self.vertices = vertices  # Node形式的顶点
        self.adjacency_list = adjacency_list  # key: str, 顶点名; value:list, [str1,str2,...]与它相连的顶点名


class Vertex(object):
    __slots__ = ('key', 'color', 'parent', 'distance', 'discover', 'finish')

    def __init__(self, key, *, parent=None, distance=float('infinity'), color='white', discover=0, finish=0):
        self.key = key
        self.parent = parent
        self.distance = distance
        self.color = color
        self.discover = discover
        self.finish = finish


def depth_first_search(G):
    key_dict = {}
    for vertex_i in G.vertices:
        key_dict[vertex_i] = Vertex(vertex_i)

    time = 0

    def dfs_visit(G, v):
        nonlocal time
        for vertex_j in G.adjacency_list[v]:
            if key_dict[vertex_j].color == 'white':
                key_dict[vertex_j].parent = v
                key_dict[vertex_j].color = 'black'
                time += 1
                key_dict[vertex_j].discover = time
                dfs_visit(G, vertex_j)
        time += 1
        key_dict[v].finish = time

    for vertex_i in G.vertices:
        if key_dict[vertex_i].color == 'white':
            key_dict[vertex_i].color = 'black'
            time += 1
            key_dict[vertex_i].discover = time
            dfs_visit(G, vertex_i)

    return dict((vertex_i, (key_dict[vertex_i].discover, key_dict[vertex_i].finish)) for vertex_i in G.vertices)


def is_cyclic(G):
    class GetOutOfRecursion(Exception):
        pass

    key_dict = {}
    for vertex_i in G.vertices:
        key_dict[vertex_i] = Vertex(vertex_i)

    def dfs_visit(G, v):
        for vertex_j in G.adjacency_list[v]:
            if key_dict[vertex_j].color == 'white':
                key_dict[vertex_j].color = 'gray'
                dfs_visit(G, vertex_j)
            elif key_dict[vertex_j].color == 'gray':
                raise GetOutOfRecursion
        key_dict[v].color = 'black'

    try:
        for vertex_i in G.vertices:
            if key_dict[vertex_i].color == 'white':
                key_dict[vertex_i].color = 'gray'
                dfs_visit(G, vertex_i)
    except GetOutOfRecursion:
        return True
    return False


def topological_sort(G):
    if is_cyclic(G):
        return 'cyclic, no topological sort'
    vertex_discover_finish_dict = depth_first_search(G)
    vertex_sort_list = deepcopy(G.vertices)
    vertex_sort_list.sort(key=lambda x: -vertex_discover_finish_dict[x][1])
    return vertex_sort_list


def strongly_connected_components(G):
    def reverse_adjacency_list(G):
        reverse_list = dict((i, []) for i in G.vertices)
        for i, j in G.adjacency_list.items():
            for v in j:
                reverse_list[v].append(i)
        return reverse_list

    result = []
    vertex_discover_finish_dict = depth_first_search(G)
    G_new = deepcopy(G)
    G_new.vertices.sort(key=lambda x: -vertex_discover_finish_dict[x][1])
    G_new.adjacency_list = reverse_adjacency_list(G)
    vertex_discover_finish_dict_new = depth_first_search(G_new)
    result = deepcopy(G.vertices)
    result.sort(key=lambda x: -vertex_discover_finish_dict_new[x][1])
    result_group = []
    i = 0
    while i < len(result):
        group_i = [result[i]]
        j = i+1
        while j < len(result) and vertex_discover_finish_dict_new[result[j]][0] > vertex_discover_finish_dict_new[result[i]][0]:
            group_i.append(result[j])
            j += 1
        i = j
        result_group.append(group_i)
    return result_group

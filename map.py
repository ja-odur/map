from functools import wraps
from graph import AdjacencyMatrixGraph
import abc


class NamedVertexMeta(type):

    ADJUST_ARGS = [
                    'add_edge', 'get_adjacent_vertices', 'get_edge_weight', 'get_indegree', 'minimum_spanning_tree',
                    'shortest_path', 'build_distance_table_unweighted', 'build_distance_table_weighted',
                    'topological_sort',
                 ]

    ADJUST_RETURN_VALUE = [
        'shortest_path', 'topological_sort',
    ]

    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs)

        def get_index(lst, val):
            try:
                return lst.index(val)
            except ValueError:
                return val

        def get_name(lst, index):
            return lst[index]

        def covert_name_decorator(func):
            @wraps(func)
            def decorated(*args, **kwargs):
                self, *args = args
                args = [get_index(self.named_vertices, name) for name in args]
                return func(self, *args, **kwargs)

            return decorated

        def return_value_decorator(func):
            @wraps(func)
            def decorated(*args, **kwargs):
                self, *args = args
                val = func(self, *args, **kwargs)

                return [get_name(self.named_vertices, index) for index in val]

            return decorated

        for name in dir(cls):
            if name in mcs.ADJUST_ARGS:
                attr = covert_name_decorator(getattr(cls, name))
                setattr(cls, name, attr)

            if name in mcs.ADJUST_RETURN_VALUE:
                attr = return_value_decorator(getattr(cls, name))
                setattr(cls, name, attr)

        return cls


class CombinedMeta(abc.ABCMeta, NamedVertexMeta):
    pass


class Map(AdjacencyMatrixGraph, metaclass=CombinedMeta):
    def __init__(self, named_vertices, weighted=False, directed=False):
        super().__init__(len(named_vertices), weighted, directed)
        self.named_vertices = named_vertices

    def get_named_adjacent_vertices(self, v):
        values = super().get_adjacent_vertices(self.named_vertices.index(v))
        return [self.named_vertices[val] for val in values]

    def display(self):
        for src, dest in super().display():
            print(self.named_vertices[src], '--->', self.named_vertices[dest])

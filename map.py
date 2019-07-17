import abc
from graph import AdjacencyMatrixGraph
from metaclasses import NamedVertexMeta


class ABCNamedVertexMeta(abc.ABCMeta, NamedVertexMeta):
    """combines the ABCMeta and NamedVertexMeta metaclasses"""


class Map(AdjacencyMatrixGraph, metaclass=ABCNamedVertexMeta):
    def __init__(self, named_vertices, weighted=False, directed=False):
        super().__init__(len(named_vertices), weighted, directed)
        self.named_vertices = named_vertices

    def get_named_adjacent_vertices(self, v):
        values = super().get_adjacent_vertices(self.named_vertices.index(v))
        return [self.named_vertices[val] for val in values]

    def display(self):
        for src, dest in super().display():
            print(self.named_vertices[src], '--->', self.named_vertices[dest])

    def minimum_spanning_tree(self, source=None, algorithm='kruskal'):
        tree = super().minimum_spanning_tree(source, algorithm)

        if algorithm == 'kruskal':
            for key, values in tree.items():
                for value in values:
                    print(self.named_vertices[key], '<--->', self.named_vertices[value])
        else:
            for edge in tree:
                print(edge)


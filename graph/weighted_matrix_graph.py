import numpy as np
from .interface import GraphInterface
from .shortest_path import ShortestPath
from .graph_sort import SortGraph
from .spanning_tree import SpanningTree


class AdjacencyMatrixGraph(SortGraph, ShortestPath, SpanningTree,  GraphInterface):

    def __init__(self, num_vertices, weighted=False, directed=False):
        super().__init__(num_vertices, weighted, directed)
        self.matrix = np.zeros([num_vertices, num_vertices])

    def add_edge(self, v1, v2, weight=1):

        if not 0 <= v1 < self.num_vertices or not 0 <= v2 < self.num_vertices:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight < 1:
            raise ValueError('An edge cannot have weight less than 1')

        # auto-set the weight flag if weight exceeds 1
        if weight > 1:
            self.weighted = True

        self.matrix[v1, v2] = weight

        if not self.directed:
            self.matrix[v2, v1] = weight

    def get_adjacent_vertices(self, v):
        if not 0 <= v < self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        return [vertex for vertex in range(self.num_vertices) if self.matrix[v, vertex] > 0]

    def get_indegree(self, v):
        if not 0 <= v < self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')
        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i, v]:
                indegree += 1
        return indegree

    #         return len(self.get_adjacent_vertices(v))

    def get_edge_weight(self, v1, v2):

        return self.matrix[v1][v2]

    def display(self):
        ad_vertices = []
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                # print(i, '--->', v)
                ad_vertices.append((i, v))
        return ad_vertices


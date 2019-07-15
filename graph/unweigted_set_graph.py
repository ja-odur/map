from .interface import GraphInterface
from .shortest_path import ShortestPath
from .graph_sort import SortGraph
from .spanning_tree import SpanningTree


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError(f'The vertex {v} cannot be adjacent to itself')
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)  # sorting for only  access convenience


class AdjacencySetGraph(SortGraph, ShortestPath,SpanningTree, GraphInterface):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(self.num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if not 0 <= v1 < self.num_vertices or not 0 <= v2 < self.num_vertices:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight != 1:
            raise ValueError('An edge can not have weight less than or morethan 1')

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if not 0 <= v < self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if not 0 <= v < self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        indegree = 0

        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '--->', v)

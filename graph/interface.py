import abc


class GraphInterface(abc.ABC):
    def __init__(self, num_vertices, weighted=False, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.weighted = weighted

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

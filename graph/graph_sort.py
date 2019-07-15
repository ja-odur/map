from queue import Queue
from .interface import GraphInterface


class GraphSortError(Exception):
    pass


class SortGraph(GraphInterface):
    def topological_sort(self):
        if not self.directed:
            raise GraphSortError('Topological sort cannot be performed on undirected graphs')

        vertex_queue = Queue()

        indegree_map = {}

        for vertex in range(self.num_vertices):
            indegree_map[vertex] = self.get_indegree(vertex)
            if indegree_map.get(vertex) == 0:
                vertex_queue.put(vertex)
        sorted_list = []

        while not vertex_queue.empty():
            vertex = vertex_queue.get()
            sorted_list.append(vertex)

            for vert in self.get_adjacent_vertices(vertex):
                indegree_map[vert] = indegree_map.get(vert) - 1

                if indegree_map[vert] == 0:
                    vertex_queue.put(vert)

        if len(sorted_list) != self.num_vertices:
            raise ValueError('This graph has a cycle')

        # print(sorted_list)
        return sorted_list


from utils.priority_dict import priority_dict
from .interface import GraphInterface


class SpanningTree(GraphInterface):

    def _prim_minimum_spanning_tree(self, source):

        distance_table = {}

        for i in range(self.num_vertices):
            distance_table[i] = (None, None)

        distance_table[source] = (0, source)

        priority_queue = priority_dict()

        priority_queue[source] = 0

        visited_vertices = set()

        spanning_tree_set = set()

        while priority_queue.keys():
            current_vertex = priority_queue.pop_smallest()

            if current_vertex in visited_vertices:
                continue

            visited_vertices.add(current_vertex)

            if current_vertex != source:
                last_vertex = distance_table[current_vertex][1]
                edge = f'{last_vertex}-->{current_vertex}'

                if edge not in spanning_tree_set:
                    spanning_tree_set.add(edge)

            for neighbour in self.get_adjacent_vertices(current_vertex):
                distance = self.get_edge_weight(current_vertex, neighbour)

                neighbour_distance = distance_table[neighbour][0]

                if neighbour_distance is None or neighbour_distance > distance:
                    distance_table[neighbour] = (distance, current_vertex)
                    priority_queue[neighbour] = distance

        for edge in spanning_tree_set:
            print(edge)

    def _kruskal_minimum_spanning_tree(self):
        priority_queue = priority_dict()
        for v in range(self.num_vertices):
            for neighbour in self.get_adjacent_vertices(v):
                priority_queue[(v, neighbour)] = self.get_edge_weight(v, neighbour)

        visited_vertices = set()
        spanning_tree = {}

        for v in range(self.num_vertices):
            spanning_tree[v] = set()

        num_edges = 0

        while priority_queue.keys() and num_edges < self.num_vertices - 1:
            v1, v2 = priority_queue.pop_smallest()
            if v1 in spanning_tree[v2]:
                continue

            vertex_pair = sorted([v1, v2])
            spanning_tree[vertex_pair[0]].add(vertex_pair[1])

            if self._has_cycle(spanning_tree):
                spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
                continue

            num_edges += 1

            visited_vertices.add(v1)
            visited_vertices.add(v2)

        print('Visited vertices:', visited_vertices)

        if len(visited_vertices) != self.num_vertices:
            print('Minimum spanning tree not found')
        else:
            print('Minimum spanning tree')
            for key, values in spanning_tree.items():
                for value in values:
                    print(key, '--->', value)

    @staticmethod
    def _has_cycle(spanning_tree):
        for source in spanning_tree:

            vertices = []
            vertices.append(source)

            visited_vertices = set()

            while vertices:
                vertex = vertices.pop(0)

                if vertex in visited_vertices:
                    return True
                visited_vertices.add(vertex)

                vertices.extend(spanning_tree[vertex])
        return False

    def minimum_spanning_tree(self, source=None, algorithm='kruskal'):
        return self._kruskal_minimum_spanning_tree() if str(algorithm).lower() == 'kruskal' else \
               self._prim_minimum_spanning_tree(source)


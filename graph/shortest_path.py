from queue import Queue
from utils.priority_dict import priority_dict
from graph import GraphInterface


class ShortestPath(GraphInterface):

    def build_distance_table_unweighted(self, source):
        distance_table = {}

        for i in range(self.num_vertices):
            distance_table[i] = (None, None)

        distance_table[source] = (0, source)

        node_queue = Queue()

        node_queue.put(source)

        while not node_queue.empty():

            current_vertex = node_queue.get()

            current_distance = distance_table.get(current_vertex)[0]

            for neighbour in self.get_adjacent_vertices(current_vertex):

                if distance_table[neighbour][0] is None:
                    distance_table[neighbour] = (1 + current_distance, current_vertex)

                    if self.get_adjacent_vertices(neighbour):
                        node_queue.put(neighbour)

        return distance_table

    def build_distance_table_weighted(self, source):
        distance_table = {}

        for vertex in range(self.num_vertices):
            distance_table[vertex] = (None, None)

        distance_table[source] = (0, source)

        priority_queue = priority_dict()

        priority_queue[source] = 0

        while priority_queue.keys():
            current_vertex = priority_queue.pop_smallest()

            current_distance = distance_table[current_vertex][0]

            for neighbour in self.get_adjacent_vertices(current_vertex):
                distance = current_distance + self.get_edge_weight(current_vertex, neighbour)

                neighbour_distance = distance_table[neighbour][0]

                if neighbour_distance is None or neighbour_distance > distance:
                    distance_table[neighbour] = (distance, current_vertex)
                    priority_queue[neighbour] = distance

        return distance_table

    def shortest_path(self, source, destination):
        distance_table = self.build_distance_table_unweighted(source)if not self.weighted else \
            self.build_distance_table_unweighted(source)

        path = [destination]

        prev_vertex = distance_table[destination][1]

        while prev_vertex is not None and prev_vertex is not source:
            path = [prev_vertex] + path
            prev_vertex = distance_table[prev_vertex][1]

        if prev_vertex is None:
            print(f'There is no path {source} to {destination}')
            return None

        else:
            path = [source] + path
            print(f'Shortest path is: {path}')
            return path

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, capacity_matrix):
        self.capacity = capacity_matrix
        self.size = len(capacity_matrix)
        self.flow = np.zeros_like(capacity_matrix)
        self.source = 0
        self.sink = self.size - 1


    def _bfs(self, parent):
        visited = [False] * self.size
        queue = [self.source]
        visited[self.source] = True


        while queue:
            current = queue.pop(0)


            for neighbor in range(self.size):
                if not visited[neighbor] and self.capacity[current, neighbor] - self.flow[current, neighbor] > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current


                    if neighbor == self.sink:
                        return True


        return False

def EdmondKarp(self, source=0, sink=None):
        """
        Implements the Edmonds-Karp algorithm to calculate the maximum flow.
        Args:
            source: The source node (default: 0).
            sink: The sink node (default: last node).
        Returns:
            The value of the maximum flow.
        """
        if sink is None:
            sink = self.size - 1  # Default sink is the last node

        max_flow = 0
        parent = [-1] * self.size

        while self.bfs(source, sink, parent):
            # Find the bottleneck capacity
            path_flow = float('Inf')
            current = sink
            while current != source:
                prev = parent[current]
                path_flow = min(path_flow, self.capacity[prev][current] - self.flow[prev][current])
                current = prev

            # Update residual capacities in the flow graph
            current = sink
            while current != source:
                prev = parent[current]
                self.flow[prev][current] += path_flow
                self.flow[current][prev] -= path_flow
                current = prev

            # Add path flow to the overall maximum flow
            max_flow += path_flow

        return max_flow
    def edmonds_karp(self):
        parent = [-1] * self.size
        max_flow = 0


        while self._bfs(parent):
            path_flow = float('Inf')
            current = self.sink


            while current != self.source:
                path_flow = min(path_flow, self.capacity[parent[current], current] - self.flow[parent[current], current])
                current = parent[current]


            current = self.sink
            while current != self.source:
                prev = parent[current]
                self.flow[prev, current] += path_flow
                self.flow[current, prev] -= path_flow
                current = prev


            max_flow += path_flow


        return max_flow

# Visualize the flow network
visualize_flow(graph, capacity_matrix)




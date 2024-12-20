import numpy as np

class Graph:
    def __init__(self, data):
        """
        Initialize the graph with an adjacency matrix of capacities.
        Args:
            data: 2D numpy array representing the capacity matrix.
        """
        self.capacity = data  # Capacity matrix
        self.size = data.shape[0]  # Number of nodes
        self.flow = np.zeros_like(data)  # Initialize flow matrix with zeros

    def bfs(self, source, sink, parent):
        """
        Perform a BFS to find an augmenting path in the residual graph.
        Args:
            source: The source node.
            sink: The sink node.
            parent: List to store the path.
        Returns:
            True if an augmenting path exists, False otherwise.
        """
        visited = [False] * self.size
        queue = [source]
        visited[source] = True
 while queue:
            current = queue.pop(0)
            for neighbor in range(self.size):
                # If not visited and residual capacity exists
                if not visited[neighbor] and (self.capacity[current][neighbor] - self.flow[current][neighbor] > 0):
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    if neighbor == sink:
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

def visualize_graph(graph, flow_graph):
    G = nx.DiGraph()
    for u in graph:
        for v, capacity in graph[u].items():
            G.add_edge(u, v, capacity=capacity, flow=flow_graph[u].get(v, 0))
    
    pos = nx.spring_layout(G)
    edge_labels = {
        (u, v): f"{d['flow']}/{d['capacity']}" for u, v, d in G.edges(data=True)
    }
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()


    # Source and Sink
source, sink = 'S', 'T'

# Run Edmonds-Karp Algorithm
max_flow, flow_distribution = edmonds_karp(graph, source, sink)

# Output Results
print(f"Maximum Flow: {max_flow}")

# Visualize the Graph and Flow Distribution
visualize_graph(graph, flow_distribution)


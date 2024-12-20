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

  def visualize_flow(self):
        G = nx.DiGraph()
        for u in range(self.size):
            for v in range(self.size):
                if self.capacity[u, v] > 0:
                    G.add_edge(u, v, capacity=self.capacity[u, v], flow=self.flow[u, v])


        # Custom positions for better layout
        #pos = nx.spring_layout(G)  # Gjeneron pozicione automatikisht për çdo nyje
        pos = {
            0: (-2, 0), 1: (-1, 1), 2: (-1, -1), 3: (0, 1), 4: (0, -1), 5: (1, 0)
        }


        # Highlight source and sink nodes with different colors
        node_colors = ["green" if node == self.source else "red" if node == self.sink else "lightblue" for node in G.nodes()]


        # Edge labels with capacity for all edges
        edge_labels = {}
        for u, v, d in G.edges(data=True):
            edge_labels[(u, v)] = f"{d['capacity']}"


        # Draw straight and curved edges selectively
        curved_edges = []
        straight_edges = []
        for u, v in G.edges():
            if G.has_edge(v, u) and (v, u) not in curved_edges:
                curved_edges.append((u, v))
            else:
                straight_edges.append((u, v))


        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
        nx.draw_networkx_labels(G, pos, font_weight='bold', font_size=10)


        nx.draw_networkx_edges(G, pos, edgelist=straight_edges, connectionstyle="arc3,rad=0", arrows=True, arrowstyle='-|>', min_target_margin=15)
        nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle="arc3,rad=0.2", arrows=True, arrowstyle='-|>', min_target_margin=15)


        # Ensure all edge labels, including curved edges, are displayed clearly
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5, rotate=False)


        # Explicitly label bidirectional edges to ensure both capacities are shown
        for (u, v) in curved_edges:
            if (v, u) in G.edges:
                plt.text(
                    (pos[u][0] + pos[v][0]) / 2 - 0.2,
                    (pos[u][1] + pos[v][1]) / 2 + 0.2,
                    f"{G[u][v]['capacity']}/{G[v][u]['capacity']}",
                    fontsize=10, color="black"
                )


        plt.box(False)  # Remove the black border box
        plt.show()


def get_user_input():
    nodes = int(input("Enter the number of nodes in the graph: "))
    capacity_matrix = np.zeros((nodes, nodes), dtype=int)


    print("Enter the edges in the format 'source destination capacity' (0-indexed).")
    print("Type 'done' when finished.")


    max_edges = nodes * (nodes - 1)  # Maximum allowed edges
    edge_count = 0


    while edge_count < max_edges:
        user_input = input(f"Edge ({edge_count + 1}/{max_edges}): ")
        if user_input.lower() == "done":
            break


        try:
            u, v, capacity = map(int, user_input.split())
            if u == v:
                print("Self-loops (edges from a vertex to itself) are not allowed. Try again.")
                continue
            if u < 0 or v < 0 or u >= nodes or v >= nodes or capacity < 0:
                print("Invalid edge or capacity. Please try again.")
                continue
            if capacity_matrix[u, v] > 0:
                print("Edge already exists. Duplicates are not allowed. Try again.")
                continue


            capacity_matrix[u, v] = capacity  # Add edge
            edge_count += 1
        except ValueError:
            print("Invalid input format. Please enter: 'source destination capacity'.")


    if edge_count == max_edges:
        print("Maximum number of edges reached.")


    return capacity_matrix
if __name__ == "__main__":
     choice = input("Use default graph (yes/no)? ").lower()
     if choice == "yes":
        # Default hardcoded graph
        capacity_matrix = np.array([
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ])
     else:
        # Get graph input from the user
        capacity_matrix = get_user_input()



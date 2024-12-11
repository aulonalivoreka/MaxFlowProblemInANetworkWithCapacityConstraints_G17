from collections import deque

def create_graph():
    """
    Create a simple directed graph as an adjacency dictionary.
    Each key is a node, and the value is a dictionary of neighbors with capacities.
    """
    graph = {
        'A': {'B': 10, 'C': 5},
        'B': {'C': 15, 'D': 10},
        'C': {'D': 10},
        'D': {}
    }
    return graph
    
def bfs(residual_graph, source, sink, parent):
    """
    Perform BFS to find an augmenting path in the residual graph.
    Args:
        residual_graph: The residual graph with capacities.
        source: The source node.
        sink: The sink node.
        parent: Dictionary to store the path.
    Returns:
        True if an augmenting path exists, False otherwise.
    """
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()
        for neighbor, capacity in residual_graph[current].items():
            if neighbor not in visited and capacity > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
                if neighbor == sink:
                    return True
    return False

import matplotlib.pyplot as plt
import networkx as nx

def visualize_flow(graph, residual_graph):
    """
    Visualizes the flow distribution in the graph.
    Args:
        graph: The original graph.
        residual_graph: The residual graph with updated flows.
    """
    G = nx.DiGraph()
    for u in graph:
        for v, capacity in graph[u].items():
            G.add_edge(u, v, capacity=capacity)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
    edge_labels = {
        (u, v): f"{graph[u][v] - residual_graph[u][v]}/{graph[u][v]}"
        for u in graph for v in graph[u]
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Flow Distribution (flow/capacity)")
    plt.show()

def main():
    """
    Main function to execute the Edmonds-Karp algorithm and visualize results.
    """
    # Create the graph
    graph = create_graph()

    # Define source and sink
    source, sink = 'A', 'D'

    # Run Edmonds-Karp algorithm
    max_flow, residual_graph = edmonds_karp(graph, source, sink)

    # Output results
    print(f"Maximum Flow: {max_flow}")

    # Visualize the graph and flow distribution
    visualize_flow(graph, residual_graph)

if _name_ == "_main_":
    main()

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
    Basic BFS implementation to find an augmenting path.
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

def edmonds_karp(graph, source, sink):

    """

    Implements the Edmonds-Karp algorithm to compute the maximum flow.

    Args:
        graph: The input graph with capacities.
        source: The source node.
        sink: The sink node.
    Returns:
        max_flow: The maximum flow value.
        residual_graph: The updated residual graph.

    """

    # Initialize residual graph

    residual_graph = {u: {v: graph[u][v] for v in graph[u]} for u in graph}
    for u in graph:
        for v in graph[u]:
            if v not in residual_graph:
                residual_graph[v] = {}
            residual_graph[v][u] = 0  # Reverse edge

    max_flow = 0
    parent = {}


    # Find augmenting paths using BFS
    while bfs(residual_graph, source, sink, parent):
        # Find bottleneck capacity in the augmenting path
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

max_flow += path_flow

    return max_flow, residual_graph



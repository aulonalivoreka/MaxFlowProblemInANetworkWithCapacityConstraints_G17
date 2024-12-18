from collections import deque

def bfs_capacity(graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        node = queue.popleft()
        for neighbor, capacity in graph[node].items():
            if neighbor not in visited and capacity > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == sink:
                    return True
    return False

# Example Graph Input
graph = {
    'S': {'A': 16, 'C': 13},
    'A': {'B': 12},
    'B': {'S': 4, 'T': 20},
    'C': {'A': 10, 'D': 14},
    'D': {'B': 7, 'T': 4},
    'T': {}
}

def edmonds_karp(graph, source, sink):
    parent = {}
    max_flow = 0
    residual_graph = {u: {} for u in graph}
    
    # Initialize residual graph with capacities
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] = capacity
            residual_graph[v].setdefault(u, 0)
    
    while bfs_capacity(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink


       # Find the minimum capacity in the augmenting path
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


import networkx as nx
import matplotlib.pyplot as plt

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


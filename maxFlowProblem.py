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

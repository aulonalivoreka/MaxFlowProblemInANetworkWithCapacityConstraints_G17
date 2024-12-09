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

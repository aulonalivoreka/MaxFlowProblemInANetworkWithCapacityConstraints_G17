# Max Flow Visualization using Edmonds-Karp Algorithm

This project implements the **Edmonds-Karp algorithm**, a specific implementation of the Ford-Fulkerson method, to solve the **Maximum Flow Problem** in a directed network. The program is written in Python and includes functionality for graph visualization to display the flow distribution.

---

## Features

### Algorithm
- Implements the **Edmonds-Karp algorithm**, using **Breadth-First Search (BFS)** to find augmenting paths.
- Calculates the maximum possible flow from a source to a sink in a directed graph.

### Graph Visualization
- Uses **NetworkX** and **Matplotlib** to display the flow network.
- Highlights:
  - Source node in green.
  - Sink node in red.
  - Intermediate nodes in light blue.
- Displays:
  - Edge capacities.
  - Flow values for each edge.
  - Curved edges for bidirectional links for clarity.

### User Interaction
- Allows users to define custom graphs interactively.
- Provides a default graph for quick testing.
- Validates user input for correct graph structure.

---

## Requirements

- Python 3.9+
- Required libraries:
  - **NumPy**
  - **NetworkX**
  - **Matplotlib**

Install dependencies:
```bash
pip install numpy networkx matplotlib

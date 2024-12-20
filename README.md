# Max Flow Visualization using Edmonds-Karp Algorithm

This project implements the **Edmonds-Karp algorithm**, a specific implementation of the Ford-Fulkerson method, to solve the **Maximum Flow Problem** in a directed network. The program is written in Python and includes functionality for graph visualization to display the flow distribution.

---

## Edmonds-Karp Algorithm

The **Edmonds-Karp algorithm** uses a BFS (Breadth-First Search) to find, in each iteration, the shortest augmenting path between the source and the sink. The algorithm works as follows:
1. In each iteration, the **bottleneck capacity** of the path is calculated.
2. A suitable amount of flow is sent along the augmenting path.
3. The process is repeated until no augmenting path exists in the residual network.

### Key Characteristics:
- Each path contains at least one edge.
- A single BFS runs in **O(E)**, where **E** is the number of edges.
- Each edge can be part of an augmenting path at most **V** times, where **V** is the number of vertices.
- The overall worst-case running time is **O(VE²)**.

---

## Features

### Algorithm
- Implements the **Edmonds-Karp algorithm** to calculate the maximum flow.
- Uses **BFS** to find the shortest augmenting paths.

### Graph Visualization
- Displays the flow network using **NetworkX** and **Matplotlib**.
- Highlights:
  - Source node in green.
  - Sink node in red.
  - Intermediate nodes in light blue.
- Labels edges with capacities and flows.
- Curved edges are used for bidirectional flows.

![image](https://github.com/user-attachments/assets/6c8762e2-6c89-458c-969c-c9af3fe923eb)


### User Interaction
- Allows users to define custom graphs interactively.
- Provides a default graph for quick testing.
- Validates user input for graph structure correctness.

---

## Prerequisites

- Python 3.9+
- Required libraries:
  - **NumPy**
  - **NetworkX**
  - **Matplotlib**

Install dependencies:
```bash
pip install numpy networkx matplotlib

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

To install the dependencies, run:
pip install numpy networkx matplotlib


### How to Run

## Step 1: Clone the Repository
git clone https://github.com/aulonalivoreka/MaxFlowProblemInANetworkWithCapacityConstraints_G17.git
cd MaxFlowProblemInANetworkWithCapacityConstraints_G17



## Step 2: Run the Script
Execute the following command to start the script:



## Step 3: Select Graph Input Method
When prompted, choose one of the following options:
- **Default Graph**: Use a predefined graph provided in the script.
- **Custom Input**: Enter the number of nodes and edges interactively.

### Input Format

#### Default Graph
If you choose the default graph, the script will use the following capacity matrix:

```plaintext
[0, 16, 13,  0,  0,  0],
[0,  0, 10, 12,  0,  0],
[0,  4,  0,  0, 14,  0],
[0,  0,  9,  0,  0, 20],
[0,  0,  0,  7,  0,  4],
[0,  0,  0,  0,  0,  0]
```

#### Custom Graph
If you choose to provide custom input:
1. Enter the number of nodes in the graph.
2. Define the edges in the format: `source destination capacity`.
3. Use `done` to finish adding edges.

```plaintext
Enter the number of nodes in the graph: 4
Enter the edges in the format 'source destination capacity' (0-indexed).
Type 'done' when finished.
Edge (1/12): 0 1 10
Edge (2/12): 0 2 5
Edge (3/12): 1 3 10
Edge (4/12): 2 3 5
Edge (5/12): done
```

### Output

#### Example Output for Maximum Flow
After running the script, you will see the following example output:


### Graph Visualization
The output includes a visualization of the graph:
- Nodes are color-coded to distinguish the source, sink, and intermediate nodes.
- Edges are labeled with their capacity and flow values.
- Curved edges are used to represent bidirectional flows, if applicable.


# _Depth First Search_

_**Depth First Search (DFS)**, is an algorithm used for traversing or searching **tree** or **graph** data structure. Unlike, breadth first search (BFS), which explores nodes layer by layer, DFS prioritize depth over breadth. It starts at **root node** (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking. The goal is to visit all nodes in the structure systematically._

### How does the DFS algorithm work?
Here are the key steps of the DFS algorithm:
1. **Initialization**:
    - Start at the root node (or any chosen sstarting point).
    - Maintaina **stack** (or use recursion) to keep track of visited nodes.
    - Mark the starting node as **visited**.

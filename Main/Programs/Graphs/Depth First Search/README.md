# _Depth First Search_

_**Depth First Search (DFS)**, is an algorithm used for traversing or searching **tree** or **graph** data structure. Unlike, breadth first search (BFS), which explores nodes layer by layer, DFS prioritize depth over breadth. It starts at **root node** (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking. The goal is to visit all nodes in the structure systematically._

### How does the DFS algorithm work?
Here are the key steps of the DFS algorithm:
1. **Initialization**:
    - Start at the root node (or any chosen sstarting point).
    - Maintaina **stack** (or use recursion) to keep track of visited nodes.
    - Mark the starting node as **visited**.
  
2. **Exploration**:
    - While the stack is not empty:
        - Pop a node from the stack.
        - Visit the popped node (e.g., print its value or perform any other desired operation).
        - Push it unvisited neighbors onto the stack.
        - Mark the neighbors as visited.
     
3. **Termination**:
    - Repeat step 2 until the stack becomes empty.
  
> _DFS explores as deeply as possible along each branch before backtracking to explore other branches. It ensures that all reachable nodes are visited._

### Illustration
_Let's understand the working of DFS with a simple example:_
1. Initially, the stack and visited arrays are empty.
2. We push the root node (e.g., node 0) into the stack and mark it as visited.
3. While the stack is not empty:
    - Pop a node (e.g., node 0).
    - Visit the popped node (print its value).
    - Push its unvisited neighbors (e.g., nodes 1, 2 and 3) into the stack and mark them as visited.
4. Repeat the process until the stack become empty.

### Application of DFS
- **Pathfinding**: Finding paths between nodes.

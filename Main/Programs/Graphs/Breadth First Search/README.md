# Breadth First Search

_**Breadth First Search (BFS)** is an algorithm used to explore a **tree** or **graph** data structure. It starts at a specified **source node** (often called the **root**) and systematically explores all nodes at the current depth level before moving on to the nodes at the next depth level._

_In other words, BFS visits nodes layer by layer, ensuring that all nodes at a particular level are processed before moving deeper into the structure._

### How does the BFS Algorithm Work?
Here are the key steps of the BFS algorithm:
1. **Initialization**:
    - Enqueue the starting node into a queue (a data structure that follows the **first-in, first-out** principle).
    - Mark the starting node as **visited**.
  
2. **Exploration**:
    - While the queue is not empty:
        - Dequeue a node from the queue (i.e., remove it from the front of the queue).
        - Visit the dequeued node (e.g., print its value or perform any other desired operation).
        - For each unvisited neighbor of the dequeued node:
            - Enqueue the neighbor into the queue.
            - Mark the neighbor as visited.
         
3. **Termination**:
    - Repeat step 2 until the queue is empty.
  
> _This algorithm ensures that all nodes in the graph (or tree) are visited in a breadth-first manner, starting from the specified source node._

### Illustration
_Let's understand the working of BFS with a simple example:_
1. Initially, the queue and visited arrays are empty.
2. We push the root node (e.g., node 0) into the queue and mark it as visited.
3. While the queue is not empty:
    - Dequeue a node (e.g., node 0).
    - Visit the dequeued node (print its value).
    - Enqueue its unvisited neighbors (e.g., nodes 1 and 2) into the queue and mark them as visited.
4. Repeat the process until the queue becomes empty.

### Application of BFS
_BFS is commonly used in various scenarios:_
- **Pathfinding**: Finding the shortest path between two nodes.
- **Connected Components**: Identifying connected components in a graph.
- **Web Crawling**: Crawling web pages in a systematic manner.
- **Social Network Analysis**: Analyzing relationships between users.
- **Puzzle Solving**: Solving puzzles like the "15-puzzle" or "8-puzzle".

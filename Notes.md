# Day 1

- Graphs

  - Nodes are connected by edges
    - also called vertexes, vertices, verts
  - Edges may have numeric weights associated with them
    - if not shown, assume all weights are 1
  - Edges may be directed or undirected
    - directed --> it's a one-way edge
    - if there are only undirected edges
      - undirected graph
    - else
      - directed graph
  - Cyclic graphs
    - graphs that can contain a cycle
    - cycle
      - can get to the start node
  - Acyclic graphs
    - graphs that don't contain a cycle

- Represent Graph in memory

  - adjacency matrix
    - grid with true/false or edge weight values showing which nodes are adjacent
  - adjacency list
    - list of all nodes with their adjacent nodes
      - use python dictionary to keep track
        - {A: [B, c], B:[D, C], C:[C, B], D:[]}

- Traversing Graph

  - Breadth-first traversal
    - visit all nodes 1 level out from the node you start at
      - everything at distance 0 is visited before distance 1
      - everything at distance 1 is visited before distance 2
    - initialization phase
      - added starting vertex to the front of the queue
    - main loop
      ```
      while queue is not empty:
          pop current vertex off queue
          if not visited:
              "visit" the node
              mark node as visited
              add all its neighbors (adjacent nodes) to the queue
      ```
  - Depth-first traversal
    - visit all nodes down to as far as you could go on one line
    - uses stack instead of a queue
    - same code as bft just using a stack

- Searching in a graph
  - breadth-first search
    - keep track of the path so far
    - enqueue lists of the path so far
      - queue --> [[C, B], [C, G]]
    - queue is keeping track of all the shortest paths so far
    ```
        create an empty queue and enque starting vertex
        create a set to store visited vertices
        while the queue is not empty:
            dequeue the first PATH
            grab the last vertex from the PATH
            if that vertex not visited:
                check if vertex is target vertex:
                    return PATH
                visit the node
                add a PATH TO its neighbors to the back of the queue
                    copy the PATH
                    append the neighbor PATH to the back
    ```

# Day 2

- wordladders in day2.py

# Day 3

- Connected Component
  - cluster of nodes that are connected via edges to each other
    - think of as separate islands in a graph
  - worked example of island counter for a matrix representing nodes in a graph

#Traverse a graph level by level.
#Purpose: Shortest paths (unweighted), spread simulation, connectivity.

"""Logic -

Explores neighbors first.
Useful in: shortest path in unweighted graphs, network spreading."""


"""ALGORITHM-

BFS(start):
  queue = [start]
  mark start as visited
  while queue not empty:
      node = queue.pop()
      for each neighbor:
          if not visited → mark visited → enqueue
"""



from collections import deque

# Define the graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

# BFS function
def bfs(start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

# Run BFS
print("\nBFS Traversal:")
bfs(0)

#Traverse a graph using DFS

# Purpose: Explore entire graph deeply, detect connected components.

"""Logic

Explores deep before backtracking.
Useful in: checking connectivity, topological sorting, cycle detection."""


""" ALGORITHM-

DFS(node):
  mark node as visited
  for each neighbor:
      if neighbor not visited → DFS(neighbor)
"""




graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],    
    3: [1, 2]
}

visited = set()

def dfs(node):
    if node in visited: return
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        dfs(neighbor)

print("DFS Traversal:")
dfs(0)

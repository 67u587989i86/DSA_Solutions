#Linear ordering of a DAG (Directed Acyclic Graph).
"""Logic -

Nodes appear before their dependencies.
Useful in: build systems, course scheduling, task ordering.

Algo (DFS-based) -

DFS(node):
  mark visited
  for neighbor:
      if neighbor not visited → DFS(neighbor)
  push node to stack
  """
#Purpose: Scheduling tasks, dependency resolution, compilation order.



# Topological Sort using DFS
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # reverse stack to get topological order

# Directed Acyclic Graph (DAG) example
dag = {
    5: [2, 0],  # 5 points to 2 and 0
    4: [0, 1],  # 4 points to 0 and 1
    2: [3],     # 2 points to 3
    3: [1],     # 3 points to 1
    1: [],      # 1 has no outgoing edges
    0: []       # 0 has no outgoing edges
}

# Graph structure visualization:
#      5      4
#     / \    / \
#    2   0  0   1
#    |
#    3
#    |
#    1

# Run Topological Sort
print("\nTopological Sort:", topological_sort(dag))

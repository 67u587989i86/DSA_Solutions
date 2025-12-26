#Detect if a graph contains a cycle.

"""Logic - 

Cycle detection is critical in deadlock detection, topology, dependency resolution.
For undirected graph: use DFS + parent check.
For directed graph: use DFS + recursion stack.
"""
# Purpose: Detect loops, avoid infinite recursion, dependency checks.



# Cycle detection in a directed graph using DFS
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited and dfs(neighbor):
                return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example directed graph with a cycle: 0 → 1 → 2 → 0
directed_graph = {0:[1], 1:[2], 2:[0]}
print("\nCycle in Directed Graph:", has_cycle_directed(directed_graph))  # True

#Directed graphs: use a recursion stack to detect back edges.
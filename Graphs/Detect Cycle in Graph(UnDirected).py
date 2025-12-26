# Cycle detection in an undirected graph using DFS
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

# Example undirected graph with a cycle: 0—1—2—0
undirected_graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print("Cycle in Undirected Graph:", has_cycle_undirected(undirected_graph))  # True


#Undirected graphs: track parent while traversing to avoid false positives.
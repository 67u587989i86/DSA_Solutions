
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            # Stack mein neighbours daalne ka order ulta hoga
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


dfs_iterative(graph, 'A')




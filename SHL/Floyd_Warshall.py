def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # Deep copy

    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Agar new path chhota hai to update karo
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist



INF = float('inf')

graph = [
    [0,   3,   1],
    [INF, 0,   1],
    [INF, INF, 0]
]

shortest = floyd_warshall(graph)

# Print karo
nodes = ['A', 'B', 'C']
print("📍 All-Pairs Shortest Paths:")
for i in range(len(shortest)):
    for j in range(len(shortest)):
        print(f"{nodes[i]} → {nodes[j]} = {shortest[i][j]}")

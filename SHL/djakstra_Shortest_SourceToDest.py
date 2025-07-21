import heapq

def dijkstra(n, edges, source, destination):
    # Step 1: Create adjacency list
    graph = [[] for _ in range(n)]  # graph[i] = list of [neighbor, cost]
    
    for u, v, cost in edges:
        graph[u].append([v, cost])

    # Step 2: Priority queue for (cost, node)
    heap = [[0, source]]
    dist = [float('inf')] * n
    dist[source] = 0

    while heap:
        curr_cost, node = heapq.heappop(heap)

        if node == destination:
            return curr_cost

        for neighbor, weight in graph[node]:
            new_cost = curr_cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, [new_cost, neighbor])

    return -1  # Destination not reachable




n = 5  # number of nodes
edges = [
    [0, 1, 10],
    [0, 2, 3],
    [1, 2, 1],
    [2, 1, 4],
    [2, 3, 2],
    [1, 3, 2],
    [3, 4, 7]
]
source = 0
destination = 4

print(dijkstra(n, edges, source, destination))  # Output: 12


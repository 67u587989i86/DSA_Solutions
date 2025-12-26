#Find shortest path from a source in a weighted graph (non-negative weights).

"""Logic -

Greedy: always extend the node with smallest known distance.
Useful in routing (GPS, networks), pathfinding."""
# Purpose: Fastest path in maps, logistics, networks



import heapq

# Weighted Directed Graph (Adjacency List with weights)
graph = {
    0: [(1, 2), (2, 4)],  # Node 0 connects to 1 (weight 2) and 2 (weight 4)
    1: [(2, 1), (3, 7)],  # Node 1 connects to 2 (weight 1) and 3 (weight 7)
    2: [(3, 3)],           # Node 2 connects to 3 (weight 3)
    3: []                  # Node 3 has no outgoing edges
}

# Graph visualization:
#       (0)
#      /   \
#   2 /     \4
#    /       \
#  (1)----1-->(2)
#    \         |
#     7        3
#      \       |
#       (3)    |

# Dijkstra's Algorithm
def dijkstra(start):
    heap = [(0, start)]  # Min-heap to get the node with smallest distance
    distances = {node: float('inf') for node in graph}  # Initialize distances
    distances[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:  # Skip if we already have a shorter path
            continue
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    return distances

# Compute shortest paths from node 0
print("\nDijkstra Shortest Paths from 0:", dijkstra(0))

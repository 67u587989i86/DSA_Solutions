import heapq

def dijkstra(graph, start):
    # Step 1: Sab distance infinity, except start node = 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Step 2: Min-heap use karte hain (distance, node)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Agar naye se bada distance mil gaya to skip
        if current_dist > distances[current_node]:
            continue

        # Step 3: Sab neighbours check karo
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # Agar naye path se distance chhota hai to update karo
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances




graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1)],
    'C': [('D', 5)],
    'D': []
}

shortest_paths = dijkstra(graph, 'A')
print("📍Shortest paths from A:")
for node, dist in shortest_paths.items():
    print(f"A → {node} = {dist}")


print(f"A → C = {shortest_paths['C']}")
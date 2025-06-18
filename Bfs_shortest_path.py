from collections import deque  # Import deque for efficient queue operations

def bfs_shortest_path(graph, start, goal):
    visited = set()  # Set to keep track of already visited nodes
    
    queue = deque([[start]])  # Initialize the queue with the starting path (as a list)

    while queue:
        path = queue.popleft()  # Get the first path from the queue (FIFO)
        node = path[-1]         # Get the last node from the current path
        
        # ✅ If we have reached the goal node, return the path
        if node == goal:
            return path 
        
        # ✅ If this node hasn't been visited yet
        if node not in visited:
            visited.add(node)  # Mark it as visited
            
            # Iterate over all the neighbors (called 'manthan' here) of the current node
            for manthan in graph[node]:
                # Create a new path that includes the current path + this neighbor
                new_path = path + [manthan]
                
                # Add the new path to the queue for further exploration
                queue.append(new_path)
    
    # ❌ If we finish the loop without finding the goal, return None
    return None


# 🧠 Example graph using letter-labeled nodes
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# 🎯 Call the function to find the shortest path from 'A' to 'D'
print(bfs_shortest_path(graph, 'A', 'D'))  # Output: ['A', 'B', 'D']

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        time = 0

        # Step 1: Count fresh oranges and enqueue all rotten oranges with time complexity O(m*n)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
 #we traveresed through each element of the grid and added all the rotten oranges to the queue and counted the fresh oranges
        
        
        
        # Step 2: BFS
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        return time if fresh == 0 else -1
    
    
# Example usage:
grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution() # Create an instance of the Solution class

print(sol.orangesRotting(grid))  # Output: 4
      
grid = [[2,1,1],[1,1,0],[0,0,1]] # output should be -1

print(sol.orangesRotting(grid))
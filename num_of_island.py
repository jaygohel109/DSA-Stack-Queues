class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited

            while queue:
                x, y = queue.popleft()

                # Check all four directions
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "1":
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = "0"  # Mark as visited

        # Iterate through the grid and start BFS when we find land ('1')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    bfs(r, c)

        return island_count


#input and output:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

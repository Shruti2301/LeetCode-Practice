# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands. An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# We are given a m x n grid (2D List) where 1 = land and 0 = water
# An island is a group of 1s (ones) which is connected horizontally or vertically (diagonal does not count)
# We can use DFS or BFS. First, mark all connected 1s as 0s (visited). This ensures we don't count
# the same island twice. Each time we start a DFS/BFS ---> we can increment island count.
# We continue until all the cells are visited.
# We can use a recursive DFS approach

# Why DFS?
# 1. The problem belongs to connected components - we are asked to group touching elements together
# or find isolated clusters in a graph or grid.
# 2. DFS naturally says - "Pick a starting point, explore as far as possible along every branch 
# before backtracking, and mark everything you hit along the way"
# 3. In this DFS is ideal to implement with recursion. We can also use BDS with Queue (explore outward).


# Let's count the number of island in a 2D grid using DFS
def numIslands(grid):
    if not grid:
        return 0

    # Rows : Top Level items are directly in the grid
    # Columns : We need to look iside one of the rows to see how many individual cells it contains
    rows, cols = len(grid), len(grid[0])

    island_count = 0

    # Helper function to perform DFS and mark visited lands
    def dfs(r,c):
        # Base Cases : Out of Bounds of Water
        # Checks if the current cell coordinate (r,c) is out of grid boundaries OR
        # is water ('0'), meaning the search should stop and turn back.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
    
        # Mark current cell as visited by setting it to '0'
        grid[r][c] = '0'
    
        # Explore all 4 directions (up,down,left and right)
        dfs(r+1,c) # Down (moves the next row down)
        dfs(r-1,c) # Up (moves to the previous row up)
        dfs(r,c+1) # Right (moves to the next column right)
        dfs(r,c-1) # Left (moves to the previous column left)
    
    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1': # Found Unvisited Land
                island_count = island_count + 1
                dfs(r,c) # Mark all connected land as visited
    
    return island_count

# Test Case 1: Grid with 1 island
test_grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print("Islands in Grid 1:", numIslands(test_grid_1))
# Expected Output: 1


# Test Case 2: Grid with 3 islands
test_grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("Islands in Grid 2:", numIslands(test_grid_2))

# Time Complexity = O(m * n)
# Space Complexity = O(h)

# We marked visited land to avoid duplicates. We used BFS/DFS to explore all connected land.
# Only horizontal/vertical neighbors count. Everytime we start DFS/BDS ==> we can increment island count


        




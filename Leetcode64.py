class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []: return 0
        result = 0
        
        for row in range(len(grid)):
            if row != 0:
                grid[row][0] = grid[row - 1][0] + grid[row][0]
        
        for col in range(len(grid[0])):
            if col != 0:
                grid[0][col] = grid[0][col -1] + grid[0][col]
                
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] = min(grid[row - 1][col]+grid[row][col], grid[row][col - 1]+grid[row][col])
                
        print(grid)
            
        return grid[-1][-1]
        
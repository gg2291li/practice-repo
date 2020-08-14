class Solution:
    def numMagicSquaresInside(self, grid):
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.checkMagic(grid, row, col, count)
        return count
        
    def checkMagic(self, grid, row, col, count):
        if row + 2 >= len(grid):
            return
        
        if col + 2 >= len(grid(row)):
            return

        if 

        return
class Solution:
    def __init__ (self):
        self.checked = []
        self.grid = []

    def numIslands(self, grid):
        self.grid = grid[:]
        if grid == []: return 0

        result = 0
        self.checked = [[False] * len(grid[0]) for item in grid]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    self.checked[row][col] = True
                elif self.checked[row][col]:
                    continue
                else:
                    result += 1
                    self.dfs(row, col)
        return result

    def dfs(self, row, col):
        if row == -1 or row >= len(self.checked) or col == -1 or col >= len(self.checked[0]) or self.checked[row][col]:
            return
        self.checked[row][col] = True

        if self.grid[row][col] == "1":
            self.dfs(row - 1, col)
            self.dfs(row, col - 1)
            self.dfs(row + 1, col)
            self.dfs(row, col + 1)

        return
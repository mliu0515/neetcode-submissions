class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rlen, clen = len(grid), len(grid[0])

        def dfs(x, y):
            if (x < 0 or y < 0 or
                x >= rlen or y >= clen or
                grid[x][y] == 0):
                return 0
            grid[x][y] = 0
            sumArea = 1   
            for i, j in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                sumArea += dfs(i, j)
            return sumArea

        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
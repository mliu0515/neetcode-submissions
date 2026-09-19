class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea, curArea = 0, 0
        rlen, clen = len(grid), len(grid[0])

        def dfs(x, y):
            nonlocal maxArea, curArea
            if (x < 0 or y < 0 or
                x >= rlen or y >= clen or
                grid[x][y] == 0):
                return
            grid[x][y] = 0
            curArea += 1
            maxArea = max(maxArea, curArea)
            for i, j in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                dfs(i, j)

        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == 1:
                    curArea = 0
                    dfs(i, j)
        return maxArea
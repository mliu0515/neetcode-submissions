class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def treeTraverse(coordinate):
            x, y = coordinate[0], coordinate[1]
            if (
                    x < 0
                    or x >= len(grid)
                    or y < 0
                    or y >= len(grid[0])
                    or grid[x][y] == "0"
                ):
                return
            grid[x][y] = "0"

            for i, j in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                treeTraverse((i, j))
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    treeTraverse((i, j))

        return count
        
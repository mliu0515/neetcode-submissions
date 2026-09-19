class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        traversed = set()
        count = 0

        def treeTraverse(coordinate):
            if coordinate in traversed:
                return
            traversed.add(coordinate) # Has to add before the traverse takes place!
            x, y = coordinate[0], coordinate[1]
            for i, j in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if (
                    0 <= i < len(grid)
                    and 0 <= j < len(grid[0])
                    and (i, j) not in traversed
                    and grid[i][j] == "1"
                ):
                    treeTraverse((i, j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in traversed:
                    count += 1
                    treeTraverse((i, j))

        return count
        
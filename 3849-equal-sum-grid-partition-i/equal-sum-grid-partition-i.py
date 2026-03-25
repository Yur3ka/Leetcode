class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        row = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += grid[i][j]
            row.add(total)
        if total %2 == 1:
            return False
        middle = total //2
        if middle in row:
            return True
        col = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                col += grid[j][i]
            if col == middle:
                return True
        return False
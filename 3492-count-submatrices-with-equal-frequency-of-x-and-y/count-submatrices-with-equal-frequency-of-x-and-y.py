class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        precount = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            x_count = 0
            y_count = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    x_count += 1
                elif grid[i][j] == 'Y':
                    y_count += 1
                precount[i][j] = [x_count,y_count]
        for j in range(n):
            x, y = 0, 0
            for i in range(m):
                x += precount[i][j][0]
                y += precount[i][j][1]
                if x == y and x > 0:
                    ans += 1
        return ans
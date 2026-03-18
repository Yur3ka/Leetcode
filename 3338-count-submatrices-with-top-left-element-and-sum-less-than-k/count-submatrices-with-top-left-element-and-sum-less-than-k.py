class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        prefix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            temp = 0
            for j in range(n):
                temp += grid[i][j]
                prefix[i][j] = temp
        for j in range(n):
            temp = 0
            for i in range(m):
                temp += prefix[i][j]
                if temp <= k: 
                    ans += 1
                else:
                    break
        return ans
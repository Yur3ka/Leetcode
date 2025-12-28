class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        i = m-1
        for j in range(n):
            if i < 0: break
            while i >=0 and grid[i][j] < 0:
                ans += n-j
                i -= 1
        return ans

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        m, n = len(grid), len(grid[0])
        dp = [[[-float('inf'), float('inf')] for _ in range(n)] for _ in range(m)]
        move = [[0,1],[1,0]]
        dp[0][0] = [grid[0][0],grid[0][0]]
        # print(dp)
        # return -1
        for i in range(m):
            for j in range(n):
                for dx, dy in move:
                    nx = i+dx
                    ny = j+dy
                    if 0 <= nx < m and 0<=ny<n:
                        temp1 = grid[nx][ny] * dp[i][j][0]
                        temp2 = grid[nx][ny] * dp[i][j][1]
                        # temp3 = grid[nx][ny] * dp[i][j][1]
                        # temp4 =  
                        dp[nx][ny][0] = max(dp[nx][ny][0],temp1,temp2)
                        dp[nx][ny][1] = min(dp[nx][ny][1],temp1,temp2)
        # print(dp)
        if dp[m-1][n-1][0] < 0:
            return -1
        else:
            return dp[m-1][n-1][0]%MOD
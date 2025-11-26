class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ans = 0 
        MOD = 10**9+7
        # directions = [(1,0),(0,1)]
        memo = {}
        m,n = len(grid), len(grid[0])
        def dp(x,y,point,mat,mem):
            # print('hello',m,n)
            if (x,y,point) in mem:
                return mem[(x,y,point)]
            # print(x,m,y,n)
            if x == m-1 and y == n-1:
                # print('!!!')
                if point % k == 0:
                    return 1
                else:
                    return 0
            if x+1 < m:
                down= dp(x+1,y,(point+mat[x+1][y])%k,mat,mem)
            else: down = 0
            if y+1 < n:
                right = dp(x,y+1,(point+mat[x][y+1])%k,mat,mem)
            else: right = 0
            temp = (down + right) % MOD
            mem[(x,y,point)] = temp
            return temp
        return dp(0,0,grid[0][0],grid,memo) % MOD
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        neighbor = [[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += 2
                for dx,dy in neighbor:
                    newX = i + dx
                    newY = j + dy
                    if newX < 0 or newX >=n or newY < 0 or newY >= n:
                        ans += grid[i][j]
                    else:
                        ans += max(0,grid[i][j]-grid[newX][newY])
        return ans
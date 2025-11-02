class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        grid = [[0 for i in range(n)] for j in range(m)]
        for x,y in walls:
            grid[x][y] = 1
        for x,y in guards:
            grid[x][y] = 2
        for x,y in guards:
            for dx,dy in directions:
                currx, curry = x,y
                while 0<=currx+dx<m and 0 <=curry+dy<n:
                    currx += dx
                    curry += dy
                    if grid[currx][curry] == 1 or grid[currx][curry] == 2:
                        break
                    else:
                        grid[currx][curry] = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        return ans

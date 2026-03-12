class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])
        # visited  = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                temp = 0
                stack = [(i,j)]
                while stack:
                    currx, curry = stack.pop()
                    if (currx, curry) == 0:
                        continue
                    for dx, dy in directions:
                        newx = currx + dx
                        newy = curry + dy
                        if 0 <= newx < m and 0 <= newy < n:
                            # print(grid[newx][newy], newx, newy)
                            if grid[newx][newy] == 0:
                                continue
                            stack.append((newx,newy))
                    temp += grid[currx][curry]
                    grid[currx][curry] = 0
                ans = max(ans,temp)
        return ans
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        path = {}
        path[2] = {(-1,0),(1,0)}
        path[1] = [(0,1), (0,-1)]
        path[3] = [(0,-1),(1,0)]
        path[4] = [(1,0),(0,1)]
        path[5] = [(-1,0),(0,-1)]
        path[6] = [(-1,0),(0,1)]

        def canMove(nx,ny,px,py):
            for dx, dy in path[grid[nx][ny]]:
                if nx+dx == px and ny+dy == py:
                    return True
            return False

        stack = [(0,0)]
        visited = set()
        while stack:
            x,y = stack.pop()
            if x== m-1 and y == n-1:
                return True
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for dx,dy in path[grid[x][y]]:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    if canMove(nx,ny,x,y):
                        stack.append((nx,ny))
        return False
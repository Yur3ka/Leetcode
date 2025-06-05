class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        visited = set()
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        queue.append((entrance,0))
        while queue:
            loc ,step = queue.popleft()
            x,y = loc
            # print(x,y,entrance)
            if (x,y) in visited:
                continue
            if (x == 0 or y == 0 or x == n-1 or y == m-1) and (x != entrance[0] or y!= entrance[1]):
                return step
            visited.add((x,y))
            for dx, dy in direction:
                newx = x + dx
                newy = y + dy
                if 0<= newx < n and 0 <= newy < m:
                    if (newx,newy) not in visited and maze[newx][newy] != '+':
                        queue.append(([newx,newy],step+1))
        return -1
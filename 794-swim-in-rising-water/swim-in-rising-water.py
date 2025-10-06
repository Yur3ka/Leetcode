class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heap.append([grid[0][0],0,0])
        visited = set()
        move = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            time,x,y = heapq.heappop(heap)
            if (x == n-1) and (y == n-1):
                return time
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for dx,dy in move:
                newX = x + dx
                newY = y + dy
                if 0<=newX<=n-1 and 0<=newY<=n-1:
                    heapq.heappush(heap,(max(time,grid[newX][newY]),newX,newY))
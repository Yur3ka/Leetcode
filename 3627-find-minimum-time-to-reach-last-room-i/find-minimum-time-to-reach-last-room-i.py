class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        ans = {}
        heap = []
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        heapq.heapify(heap)
        heapq.heappush(heap,[0,(0,0)])
        while heapq:
            time, location = heapq.heappop(heap)
            if location in visited:
                continue
            x,y = location
            visited.add((x,y))
            if x == n-1 and y == m-1:
                return time
            for movex, movey in move:
                newx = x + movex
                newy = y + movey
                if (newx,newy) in visited:
                    continue
                if 0<= newx < n and 0 <= newy < m:
                    newTime = max(time + 1, moveTime[newx][newy]+1)
                    heapq.heappush(heap,[newTime,(newx,newy)])
        

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heap = [i for i in range(n)]
        curr = []
        used = defaultdict(int)
        meetings.sort(key=lambda x:x[0])
        for m in meetings:
            start, end = m
            while curr and curr[0][0] <= start:
                heapq.heappush(heap,curr[0][1])
                heapq.heappop(curr)
            if heap:
                slot = heapq.heappop(heap)
                heapq.heappush(curr,(end,slot))
                used[slot] += 1
            else:
                time, slot = heapq.heappop(curr)
                
                heapq.heappush(curr,(time + end - start,slot))
                used[slot] += 1
        ans, mans = 0,0
        for k,v in used.items():
            if v > mans:
                ans = k
                mans = v
            elif v == mans:
                ans = min(ans,k)
        return ans
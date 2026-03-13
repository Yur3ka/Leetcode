class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        for w in workerTimes:
            heapq.heappush(heap,[w,w,1])
        ans = 0
        for i in range(1, mountainHeight+1):
            curr, addition, used = heapq.heappop(heap)
            print(curr,used)
            ans = curr
            used += 1
            curr = curr + used*addition
            heapq.heappush(heap,[curr, addition,used])
        return ans

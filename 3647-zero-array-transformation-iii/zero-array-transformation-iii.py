class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heap = []
        queue = []
        ans = 0
        n = len(nums)
        most = [0]*(n+1)
        for i,j in queries:
            heapq.heappush(heap,(i,j))
        curr = 0
        for i in range(n):
            while heap and heap[0][0] <= i:
                start,end = heapq.heappop(heap)
                heapq.heappush(queue,(-end,start))
            while queue and -queue[0][0] < i:
                heapq.heappop(queue)
                ans += 1
            curr += most[i]
            # print(curr, most[i], i)
            if curr >= nums[i]:
                continue
            else:
                while queue and curr < nums[i]:
                    end, start = heapq.heappop(queue)
                    if start <= i <=-end:
                        curr += 1
                        most[-end+1] -= 1
                    else:
                        ans += 1
                if curr < nums[i]:
                    return -1
        return ans + len(heap) + len(queue)
            
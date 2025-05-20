class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        heap = []
        heapq.heapify(heap)
        for query in queries:
            heapq.heappush(heap,(query[0],1))
            heapq.heappush(heap,(query[1]+1,-1))
        curr = 0
        n = len(nums)
        for i in range(n):
            while heap and i == heap[0][0]:
                curr += heap[0][1]
                heapq.heappop(heap)
            if curr < nums[i]:
                return False
        return True
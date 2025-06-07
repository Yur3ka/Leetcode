class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,-n)
        curr = 0
        for _ in range(k):
            curr = heapq.heappop(heap)
            # print(curr)
        return -curr
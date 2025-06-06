class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap  = []
        count = Counter(words)
        
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        ans = []
        for i in range(k):
            _, current = heapq.heappop(heap)
            ans.append(current)
        return ans
class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        ans = list(s)
        for i in range(len(s)):
            if s[i] != '*':
                heapq.heappush(heap,(s[i],-i))
            else:
                ans[i] = ''
                curr = heapq.heappop(heap)
                ans[-curr[1]] = ''
        return ''.join(ans)
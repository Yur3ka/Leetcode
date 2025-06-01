class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit,n)+1):
            if n - i - limit > limit:
                continue
            lower = max(n-i-limit,0)
            upper = min(limit,n-i)
            ans += max(upper - lower + 1, 0)
        return ans
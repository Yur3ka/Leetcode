class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans = ans << 1
            ans += 1
            n = n >> 1
        return ans
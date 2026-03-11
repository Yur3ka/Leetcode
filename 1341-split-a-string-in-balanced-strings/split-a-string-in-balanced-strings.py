class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0 
        ans = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                ans += 1
        return ans
class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        l = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans += i-l
                l+= 1
        return ans
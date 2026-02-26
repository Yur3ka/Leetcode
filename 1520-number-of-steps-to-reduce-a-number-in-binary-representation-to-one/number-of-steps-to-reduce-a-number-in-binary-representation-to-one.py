class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        remain = 0
        for c in s[-1:0:-1]:
            curr = int(c) + remain
            remain = 0
            if curr == 0:
                ans+= 1
            elif curr == 1:
                ans += 2
                remain += 1
            else:
                remain += 1
                ans += 1
        if remain == 1:
            ans += 1
        
        return ans
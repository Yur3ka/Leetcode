class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        i = 1
        while i < n:
            ans += i*4
            i+= 1
        return ans
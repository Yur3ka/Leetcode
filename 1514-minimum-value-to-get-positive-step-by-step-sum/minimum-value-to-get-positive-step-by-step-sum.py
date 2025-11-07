class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        curr = 1
        for n in nums:
            curr += n
            if curr < 1:
                ans += (1-curr)
                curr = 1
        return ans
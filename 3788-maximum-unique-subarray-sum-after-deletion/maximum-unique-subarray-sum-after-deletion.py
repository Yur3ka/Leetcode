class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -float("inf")
        curr = 0
        nums = set(nums)
        for n in nums:
            if n > 0:
                curr += n
        if curr == 0:
            return max(nums)
        else:
            return curr
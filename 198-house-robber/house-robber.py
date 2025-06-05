class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        elif n == 3:
            return max(nums[1], nums[0]+nums[2])
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[0]+nums[2])
        for i in range(3,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i], dp[i-3] + nums[i])
        return max(dp[-1], dp[-2])
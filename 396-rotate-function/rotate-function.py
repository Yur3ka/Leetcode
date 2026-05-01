class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        n = len(nums)
        for i in range(n):
            ans += nums[i]*i
            total += nums[i]
        temp = ans
        for i in range(n-1,0,-1):
            temp += total - nums[i]*n
            ans = max(ans,temp)
        return ans
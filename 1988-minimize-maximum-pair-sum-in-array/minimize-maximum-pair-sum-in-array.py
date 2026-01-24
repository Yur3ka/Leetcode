class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -float('inf')
        for i in range(len(nums)//2):
            temp = nums[i] + nums[len(nums)-1-i]
            ans = max(ans,temp)
        return ans
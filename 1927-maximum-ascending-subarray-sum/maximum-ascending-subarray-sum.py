class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len (nums) == 1:
            return nums[0]
        curr = nums[0]
        ans = 0
        index = 0
        while index < len(nums)-1:
            if nums[index] < nums[index+1]:
                curr += nums[index+1]
                index += 1
            else:
                ans = max(ans, curr)
                curr = nums[index+1]
                index += 1
        ans = max(ans, curr)
        return ans    

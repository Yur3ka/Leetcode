class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp = []
        while len(nums) > 1:
            for i in range(len(nums)-1):
                temp.append((nums[i]+nums[i+1])%10)
            nums = temp[:]
            temp = []
        return nums[0]%10
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(digit) for digit in s]
        temp = []
        while len(nums) > 2:
            for i in range(len(nums)-1):
                temp.append(nums[i]+nums[i+1])
            nums = temp
            temp = []
        return nums[1] %10 == nums[0] % 10
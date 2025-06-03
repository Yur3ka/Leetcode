class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        current = 0
        index = 1
        while index < n and current < n:
            while current < n and nums[current] != 0:
                current += 1
            index = current + 1
            while index < n and nums[index] == 0:
                index += 1
            if current < n and index < n and (nums[index] != 0) and nums[current] == 0:
                nums[current], nums[index] = nums[index], nums[current]
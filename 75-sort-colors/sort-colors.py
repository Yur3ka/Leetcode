class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        two = 0
        for i in range(n):
            if nums[i] == 0:
                zero += 1
            if nums[i] == 2:
                two += 1
        l,r = 0, n-1
        i = 0
        while i < zero:
            if nums[i] == 0:
                i+= 1
            else:
                while nums[r] != 0:
                    r -= 1
                nums[i], nums[r] = nums[r], nums[i]
        l,r = 0, n-1
        i = n-1
        while i >= n-two:
            if nums[i] == 2:
                i-= 1
            else:
                while nums[l] != 2:
                    l+= 1
                nums[i], nums[l] = nums[l], nums[i]
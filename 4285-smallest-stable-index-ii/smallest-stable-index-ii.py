class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_until = [nums[0]]*n
        min_after = [nums[-1]]*n
        temp_max = nums[0]
        temp_min = nums[-1]
        for i in range(n):
            if nums[i] > temp_max:
                temp_max = nums[i]
            max_until[i] = temp_max
            if nums[n-1-i] < temp_min:
                temp_min = nums[n-1-i]
            min_after[n-1-i] = temp_min
        for i in range(n):
            if max_until[i] - min_after[i] <= k:
                return i
        return -1
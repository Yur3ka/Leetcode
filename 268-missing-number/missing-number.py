class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = set(nums)
        for i in range(len(nums)+1):
            if i not in k:
                return i
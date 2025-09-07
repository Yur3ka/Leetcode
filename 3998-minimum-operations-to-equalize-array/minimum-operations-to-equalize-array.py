class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(set(nums))
        if n ==1:
            return 0
        return 1
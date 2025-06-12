class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)
        for i in range(n+1):
            temp = abs(nums[i%n]- nums[(i+1)%n])
            if max_diff < temp:
                max_diff = temp
        return max_diff
        
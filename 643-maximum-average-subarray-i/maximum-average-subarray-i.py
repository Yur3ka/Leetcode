class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = 0
        for i in range(k):
            k_sum += nums[i]
        max_k = k_sum
        for i in range(k,len(nums)):
            k_sum += nums[i] - nums[i-k]
            max_k = max(max_k, k_sum)
        return max_k / k
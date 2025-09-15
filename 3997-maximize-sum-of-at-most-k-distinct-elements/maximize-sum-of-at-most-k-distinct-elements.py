class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(list(set(nums)), reverse=True)
        return sorted_nums[:k]
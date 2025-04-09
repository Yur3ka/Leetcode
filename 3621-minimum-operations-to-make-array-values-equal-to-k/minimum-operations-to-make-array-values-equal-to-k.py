class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        if k > mini:
            return -1
        distinct = len(set(nums))
        if k == mini:
            return distinct -1
        else:
            return distinct
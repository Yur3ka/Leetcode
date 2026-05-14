class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = [1]*(n)
        count[n-1] +=1
        for num in nums:
            if num > n-1:
                return False
            count[num] -= 1
            if count[num] < 0:
                return False
        return True
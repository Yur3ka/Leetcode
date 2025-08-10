class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        unsorted = []
        n = len(nums)
        for i in range(n):
            if nums[i] != i:
                unsorted.append(nums[i])
        if not unsorted:
            return 0
        else:
            ans = unsorted[0]
            for i in range(1,len(unsorted)):
                ans &= unsorted[i]
            return ans
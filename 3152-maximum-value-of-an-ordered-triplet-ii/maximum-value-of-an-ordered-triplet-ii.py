class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        post_max = [None] * n
        post_max[-1] = -1
        temp = nums[-1]
        for i in reversed(range(n-1)):
            if nums[i+1] > temp:
                temp = nums[i+1]
            post_max[i] = temp
        start = nums[0]
        for i in range(1,n):
            if nums[i] < start:
                temp = (start - nums[i])*post_max[i]
                ans = max(ans,temp)
            else:
                start = nums[i]
        return ans
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                continue
            for j in range(i+1,n-1):
                maxC = nums[i] + nums[j]-1
                last_idx = bisect_right(nums,maxC)
                ans += last_idx-j-1
        return ans
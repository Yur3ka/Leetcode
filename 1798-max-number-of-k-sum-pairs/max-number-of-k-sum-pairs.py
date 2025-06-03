class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        l,r = 0, n-1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                l+=1
                r-=1
                ans += 1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return ans
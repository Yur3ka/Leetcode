class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = [abs(i) for i in nums]
        arr.sort()
        l = 0
        r = len(nums)-1
        ans = 0
        while l <=r:
            if l <= r:
                ans += arr[r]**2
                r -= 1
            if l <=r:
                ans -= arr[l]**2
                l += 1
        return ans
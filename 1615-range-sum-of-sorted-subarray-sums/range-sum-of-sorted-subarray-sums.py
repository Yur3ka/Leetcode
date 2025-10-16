class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = []
        ans = 0
        MOD = 10**9+7
        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr += nums[j]
                s.append(curr)
        s.sort()
        for i in range(left-1,right):
            ans += s[i]
            ans %= MOD
        return ans
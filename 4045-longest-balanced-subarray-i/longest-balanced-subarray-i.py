class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            e = set()
            o = set()
            for j in range(i,len(nums)):
                if nums[j]%2 == 0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])
                if len(o) == len(e):
                    ans = max(ans,j-i+1)
        return ans
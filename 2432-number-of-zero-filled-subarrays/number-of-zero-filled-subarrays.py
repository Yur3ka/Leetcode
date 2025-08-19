class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr += 1
            else:
                ans += curr*(curr+1)//2
                curr = 0
        ans += curr*(curr+1)//2
        return ans
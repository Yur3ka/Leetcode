class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            if i > start+ans:
                return ans
            if nums[i] == target:
                ans = min(ans,abs(i-start))
        return ans
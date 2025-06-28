class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_index = []
        for i in range(len(nums)):
            nums_index.append((nums[i],i))
        nums_index.sort(key=lambda x:x[0])
        res = nums_index[-k:]
        res.sort(key=lambda x: x[1])
        ans = []
        for n in res:
            ans.append(n[0])
        return ans
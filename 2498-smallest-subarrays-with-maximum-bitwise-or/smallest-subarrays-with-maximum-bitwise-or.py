class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = []
        pos = [[-1 for i in range(31)] for j in range(len(nums))]
        for i in range(len(nums)):
            for j in range(31):
                if (nums[i] & (1<<j)) != 0:
                    pos[i][j] = i
        for i in range(len(nums)-2,-1,-1):
            for j in range(31):
                if pos[i][j] == -1:
                    pos[i][j] = pos[i+1][j]
        for i in range(len(nums)):
            ans.append(max(max(pos[i]),i)-i+1)
        return ans
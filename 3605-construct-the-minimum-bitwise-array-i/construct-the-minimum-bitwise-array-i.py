class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i%2 == 0:
                ans.append(-1)
            else:
                for k in range(i):
                    if (k|(k+1)) == i:
                        ans.append(k)
                        break
        return ans
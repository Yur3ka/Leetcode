class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(-1)
            else:
                res = -1
                for k in range(31,-1,-1):
                    if (i & (1<<k)):
                        temp = i ^ (1<<k)
                        if (temp|(temp+1)) == i:
                            res = temp
                            break
                ans.append(res)
        return ans
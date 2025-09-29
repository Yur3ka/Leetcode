class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        n = len(values)
        # ans = float('inf')
        def dp(start,end,nums):
            if (start,end) in memo:
                return memo[(start,end)]
            if end <= start+1:
                return 0
            elif start + 2 == end:
                v = nums[start]*nums[start+1]*nums[end]
                memo[(start,end)] = v
                return v
            else:
                v = float('inf')
                for k in range(start+1,end):
                    temp = dp(start,k,nums)+dp(k,end,nums)+nums[start]*nums[end]*nums[k]
                    v= min(v,temp)
                memo[(start,end)] = v
                return v
        return dp(0,n-1,values)
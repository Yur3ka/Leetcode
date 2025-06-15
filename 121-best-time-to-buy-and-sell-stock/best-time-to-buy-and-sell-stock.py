class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suff_max = [0]*n
        suff_max[-1] = prices[-1]
        for i in range(n-2,-1,-1):
            suff_max[i] = max(suff_max[i+1],prices[i])
        ans = 0
        for i in range(n-1):
            ans = max(ans,suff_max[i+1]-prices[i])
        return ans
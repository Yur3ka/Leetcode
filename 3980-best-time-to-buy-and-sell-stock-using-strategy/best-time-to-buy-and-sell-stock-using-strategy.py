class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix = [0]
        for i in range(len(prices)):
            prefix.append(prefix[i] + prices[i]*strategy[i])
        temp = 0
        print(prefix)
        for i in range(k//2,k):
            temp += prices[i]
        curr = prefix[-1] - prefix[k] + temp
        ans = max(prefix[-1],curr)
        for i in range(1,len(prices)-k+1):
            curr += prices[i-1]*strategy[i-1]
            curr -= prices[i-1+k//2]
            curr -= prices[i+k-1]*strategy[i+k-1]
            curr += prices[i+k-1]
            print(curr)
            ans = max(ans,curr)
        return ans
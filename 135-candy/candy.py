class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ans = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        if ratings[n-1] > ratings[n-2]:
            ans[n-1] = ans[n-2]+1
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1]+1)
        return sum(ans)
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*(n+1+forget)
        MOD = 10**9 + 7
        dp[1] = 1
        for i in range(1,n):
            for j in range(delay,forget):
                dp[i+j] += dp[i]
                dp[i+j] %= MOD
            
        return sum(dp[n+1-forget:n+1])%MOD
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            if i + k <= n-1:
                dp[i] = dp[i+k]+energy[i]
            else:
                dp[i] = energy[i]
        return max(dp)
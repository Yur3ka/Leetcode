class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        nums = sorted(list(set(power)))
        dp = [0]*len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            dp[i] = curr*c[curr]
            if i == 0:
                dp[0]=(curr*c[curr])
            else:
                j = i-1
                while j >= 0 and nums[j] >= curr -2:
                    dp[i] = max(dp[i],dp[j])
                    j-=1
                if j >= 0:
                    dp[i] = max(dp[i],dp[j]+curr*c[curr])
        # print(dp)
        return dp[-1]
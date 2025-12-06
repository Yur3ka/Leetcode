class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        dp = [0]*(n+1)
        prefix = [0]*(n+1)     # prefix dp
        
        dp[0] = 1
        prefix[0] = 1
        
        minh = []  # (value, index)
        maxh = []  # (-value, index)
        
        L = 0
        
        for R in range(n):
            heapq.heappush(minh, (nums[R], R))
            heapq.heappush(maxh, (-nums[R], R))

            # fix window
            while -maxh[0][0] - minh[0][0] > k:
                L += 1
                # remove invalid entries
                while minh[0][1] < L:
                    heapq.heappop(minh)
                while maxh[0][1] < L:
                    heapq.heappop(maxh)

            # dp[R+1] = sum(dp[L..R])
            dp[R+1] = (prefix[R] - prefix[L-1]) % MOD if L > 0 else prefix[R]
            prefix[R+1] = (prefix[R] + dp[R+1]) % MOD
        
        return dp[n] % MOD
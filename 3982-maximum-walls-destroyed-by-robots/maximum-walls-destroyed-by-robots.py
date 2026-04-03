class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        rb = list(zip(robots,distance))
        rb.sort()
        walls.sort()
        def count_in_range(a, L, R):
            left = bisect.bisect_left(a, L)
            right = bisect.bisect_right(a, R)
            return right - left

        dp = [[[0,0]for _ in range(2)] for _ in range(len(rb))]
        # print(dp)
        for i in range(len(rb)):
            r, d = rb[i]
            if i == 0:
                last_right = 0
                past_l, past_r = 0, 0
            else:
                last_right = dp[i-1][1][1]
                past_l, past_r = dp[i-1][0][0], dp[i-1][1][0]
            next_right = rb[i+1][0] if i < len(rb)-1 else float('inf')
            past_left = rb[i-1][0] if i > 0 else -1
            go_left_1 = count_in_range(walls,max(r-d,last_right+1),r)
            go_left_2 = count_in_range(walls,max(past_left+1,r-d),r)
            go_right = count_in_range(walls, r, min(next_right-1,r+d))

            dp[i][0] = [max(go_left_1+past_r,go_left_2+past_l),r]
            dp[i][1] = [max(past_l,past_r)+go_right,r+d]

        ans = 0
        for i in range(2):
            ans = max(ans,dp[len(rb)-1][i][0])
        return ans
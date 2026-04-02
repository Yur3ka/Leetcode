class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[None] * 3 for _ in range(n)] for _ in range(m)]

        # trạng thái bắt đầu
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        def relax(x, y, k, val):
            if val is None:
                return
            if dp[x][y][k] is None or dp[x][y][k] < val:
                dp[x][y][k] = val

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] is None:
                        continue

                for nx, ny in ((i + 1, j), (i, j + 1)):
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    val = coins[nx][ny]

                    # không dùng quyền bỏ qua
                    for k in range(3):
                        if dp[i][j][k] is not None:
                            relax(nx, ny, k, dp[i][j][k] + val)

                    # nếu là ô âm, có thể dùng quyền bỏ qua
                    if val < 0:
                        if dp[i][j][0] is not None:
                            relax(nx, ny, 1, dp[i][j][0])
                        if dp[i][j][1] is not None:
                            relax(nx, ny, 2, dp[i][j][1])

        return max(x for x in dp[m - 1][n - 1] if x is not None)
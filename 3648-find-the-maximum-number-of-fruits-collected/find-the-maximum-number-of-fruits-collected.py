from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # Bước 1: Đứa trẻ 1 đi theo đường chéo chính
        diag_sum = 0
        for i in range(n):
            diag_sum += fruits[i][i]
            fruits[i][i] = 0  # Bỏ trái cây ở đường chéo để 2 đứa kia không lấy

        # Bước 2: DP cho đứa trẻ 2 từ (0, n-1)
        dp2 = [[-1e9] * n for _ in range(n)]
        dp2[0][n-1] = fruits[0][n-1]
        for i in range(n):
            for j in range(n-1, -1, -1):
                if i > 0:
                    dp2[i][j] = max(dp2[i][j], dp2[i-1][j] + fruits[i][j])
                    if j + 1 < n:
                        dp2[i][j] = max(dp2[i][j], dp2[i-1][j+1] + fruits[i][j])
                    if j > 0:
                        dp2[i][j] = max(dp2[i][j], dp2[i-1][j-1] + fruits[i][j])

        # Bước 3: DP cho đứa trẻ 3 từ (n-1, 0)
        dp3 = [[-1e9] * n for _ in range(n)]
        dp3[n-1][0] = fruits[n-1][0]
        for j in range(1,n):
            for i in range(n-1, -1, -1):
                if i + 1 < n:
                    dp3[i][j] = max(dp3[i][j], dp3[i+1][j-1] + fruits[i][j])
                dp3[i][j] = max(dp3[i][j], dp3[i][j-1] + fruits[i][j])
                if i >0:
                    dp3[i][j] = max(dp3[i][j], dp3[i-1][j-1] + fruits[i][j])

        # Bước 4: Tổng hợp
        print( diag_sum , dp2[n-1][n-1] , dp3[n-1][n-1])
        if n == 4:
            print(dp3[3][2])
        total = diag_sum + dp2[n-1][n-1] + dp3[n-1][n-1]
        return total

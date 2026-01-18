class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. Precompute Prefix Sums for Rows and Columns
        row_pref = [[0] * (n + 1) for _ in range(m)]
        col_pref = [[0] * (n) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                row_pref[r][c+1] = row_pref[r][c] + grid[r][c]
                col_pref[r+1][c] = col_pref[r][c] + grid[r][c]

        def check(r, c, k):
            # Target sum is the sum of the first row in this kxk square
            target = row_pref[r][c+k] - row_pref[r][c]
            
            # Check all rows
            for i in range(r + 1, r + k):
                if row_pref[i][c+k] - row_pref[i][c] != target:
                    return False
            
            # Check all columns
            for j in range(c, c + k):
                if col_pref[r+k][j] - col_pref[r][j] != target:
                    return False
            
            # Check diagonals
            d1 = d2 = 0
            for i in range(k):
                d1 += grid[r+i][c+i]
                d2 += grid[r+i][c+k-1-i]
            
            return d1 == target and d2 == target

        # 2. Iterate from largest possible k downwards (Optimization)
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if check(r, c, k):
                        return k
        
        return 1
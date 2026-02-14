class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows, cols = 100, 100
        cups = [[0 for _ in range(cols)] for _ in range(rows)]
        cups[0][0] = poured
        for i in range(1,query_row+1):
            for j in range(i+1):
                cups[i][j] += max(0,(cups[i-1][j]-1)/2)
                if j > 0:
                    cups[i][j] += max(0,(cups[i-1][j-1]-1)/2)
        ans = min(1,max(0,cups[query_row][query_glass]))
        return ans
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        coll = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    coll.add(j)
        for r in row:
            for j in range(m):
                matrix[r][j] = 0
        for c in coll:
            for j in range(n):
                matrix[j][c] = 0
        
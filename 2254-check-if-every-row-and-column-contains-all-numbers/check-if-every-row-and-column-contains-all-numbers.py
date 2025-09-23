class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        n = len(matrix)
        for i in range(n):
            used1 = set()
            used2 = set()
            for j in range(n):
                used1.add(matrix[i][j])
                used2.add(matrix[j][i])
            if len(used1) != n or len(used2) != n:
                return False
        return True
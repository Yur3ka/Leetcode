class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        minus = []
        positive = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0:
                    positive.append(matrix[i][j])
                else:
                    minus.append(matrix[i][j])
        minus.sort()
        positive.sort()
        if len(minus) %2 == 0:
            return -sum(minus) + sum(positive)
        else:
            if len(positive) > 0:
                return -sum(minus[:-1]) + sum(positive[1:]) + abs(minus[-1]+positive[0])        
            else:
                return -sum(minus[:-1]) + minus[-1]
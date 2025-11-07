class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            temp = float('inf')
            index = -1
            status = True
            for j in range(len(matrix[0])):
                if matrix[i][j] < temp:
                    index = j
                    temp = matrix[i][j]
            for k in range(len(matrix)):
                if matrix[k][index] > matrix[i][index]:
                    status = False
                    break
            if status:
                ans.append(matrix[i][index]) 
        return ans
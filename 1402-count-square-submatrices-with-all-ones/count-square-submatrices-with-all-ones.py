class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    ans += 1
                    for k in range(2,min(m-i+1,n-j+1)):
                        curr = 0
                        for p in range(k):
                            curr += sum(matrix[i+p][j:j+k])
                        # print(k, curr, i, j)
                        if curr == k*k:
                            ans += 1
                        else:
                            break
        return ans
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ans = []
        count = 0
        for i in range(m):
            temp = []
            for j in range(min(i+1,n)):
                temp.append(mat[0+j][i-j])
            if count %2 == 0:
                ans += temp[::-1]
            else:
                ans += temp
            count += 1
        for k in range(1,n):
            temp = []
            for v in range(min(m,(n-k))):
                temp.append(mat[k+v][m-1-v])
            if count %2 == 0:
                ans += temp[::-1]
            else:
                ans += temp
            count += 1
        return ans
                
            
                
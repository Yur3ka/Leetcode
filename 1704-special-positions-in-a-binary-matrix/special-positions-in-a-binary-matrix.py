class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = set()
        columm = set()
        ans = 0
        m ,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i in row or j in columm:
                    continue
                if mat[i][j] == 1:
                    status = True
                    for r in range(m):
                        if r == i:
                            continue
                        if mat[r][j] == 1:
                            status = False
                            break
                    for c in range(n):
                        if c == j:
                            continue
                        if mat[i][c] == 1:
                            status = False
                            break
                    if status:
                        ans += 1
                    row.add(i)
                    columm.add(j)
        return ans

            
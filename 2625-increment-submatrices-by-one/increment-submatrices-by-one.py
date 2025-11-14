class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        a = [[0 for _ in range(n)] for _ in range(n)]
        m = [[0 for _ in range(n)] for _ in range(n)]
        for r1,c1,r2,c2 in queries:
            for i in range(r1,r2+1):
                a[i][c1] += 1
                m[i][c2] -= 1
        e = 0
        for i in range(n):
            for j in range(n):
                e += a[i][j]
                ans[i][j] = e
                e += m[i][j]
        return ans
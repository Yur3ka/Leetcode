class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        r = defaultdict(int)
        c = defaultdict(int)
        for row in grid:
            r[tuple(row)] += 1
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            c[tuple(temp)] += 1
        for k,v in r.items():
            ans += v*c[k]
        return ans
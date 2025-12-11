class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row = [[1000000,-1] for _ in range(n+1)]
        col = [[1000000,-1] for _ in range(n+1)]
        for x,y in buildings:
            row[x][0] = min(row[x][0],y)
            row[x][1] = max(row[x][1],y)
            col[y][0] = min(col[y][0],x)
            col[y][1] = max(col[y][1],x)
        ans = 0
        for x, y in buildings:
            if col[y][0] < x < col[y][1] and row[x][0] < y < row[x][1]:
                ans += 1
        return ans
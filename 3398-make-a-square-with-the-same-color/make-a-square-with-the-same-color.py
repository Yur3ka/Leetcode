class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        sq = [[0,0],[0,1],[1,0],[1,1]]
        for i in range(2):
            for j in range(2):
                b = 0
                w = 0
                for dx, dy in sq:
                    if grid[i+dx][j+dy] == 'B':
                        b += 1
                    else:
                        w += 1
                if max(b,w) >= 3:
                    return True
        return False
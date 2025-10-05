






class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        n, m = len(heights), len(heights[0])
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n and 0 <= ny < m
                    and not visited[nx][ny]
                    and heights[nx][ny] >= heights[x][y]
                ):
                    dfs(nx, ny, visited)

        # Pacific Ocean (top + left)
        for i in range(n):
            dfs(i, 0, pacific)
        for j in range(m):
            dfs(0, j, pacific)

        # Atlantic Ocean (bottom + right)
        for i in range(n):
            dfs(i, m - 1, atlantic)
        for j in range(m):
            dfs(n - 1, j, atlantic)

        # Cells that can reach both oceans
        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res

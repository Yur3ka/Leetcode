class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        total = 0
        visited = set()
        queue = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = 0
                    visited.add((i,j))
                    queue.append((i, j))
                    while queue:
                        curr = queue.pop()
                        count += 1
                        for k in range(row):
                            if grid[k][curr[1]] == 1 and (k, curr[1]) not in visited:
                                queue.append((k, curr[1]))
                                visited.add((k, curr[1]))
                        for m in range(col):
                            if grid[curr[0]][m] == 1 and (curr[0], m) not in visited:
                                queue.append((curr[0], m))
                                visited.add((curr[0], m))
                    if count >= 2:
                        total += count
        return total

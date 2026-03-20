class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n-k+1)]for _ in range(m-k+1)]
        for i in range(m):
            for j in range(n):
                if i+k-1 >= m or j+k-1 >= n:
                    continue
                temp = float('inf')
                arr = []
                seen = set()
                for x in range(k):
                    for y in range(k):
                        
                        if grid[i+x][j+y] not in seen:
                            arr.append(grid[i+x][j+y])
                            seen.add(grid[i+x][j+y])
                        arr.sort()
                        for idx in range(len(arr)-1):
                            temp = min(temp,arr[idx+1]-arr[idx])
                if len(arr) == 1:
                    temp = 0
                ans[i][j] = temp
        return ans
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        temp = [[float('inf') for i in range(n)] for j in range(n)]
        temp[0][0] = triangle[0][0]
        direction = ([1,0],[1,1])
        for i in range(n-1):
            for j in range(i+1):
                for dx, dy in direction:
                    newX, newY = i+dx,j+dy
                    if 0<= newX <=i+1 and 0<=newY<=i+1:
                        temp[newX][newY] = min(temp[newX][newY],temp[i][j]+triangle[newX][newY])
        return min(temp[n-1])
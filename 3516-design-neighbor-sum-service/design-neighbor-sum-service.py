class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.mat = grid
        self.n = len(grid)
        self.adj = [(1,0),(-1,0),(0,1),(0,-1)]
        self.diag = [(-1,-1),(1,1),(1,-1),(-1,1)]
    def location(self,value):
        for i in range(self.n):
            for j in range(self.n):
                if self.mat[i][j] == value:
                    return i,j
    def adjacentSum(self, value: int) -> int:
        ans = 0
        # print('case')
        row, col = self.location(value)
        # print(row,col)
        for dx, dy in self.adj:
            newx = row + dx
            newy = col + dy
            print(newx,newy)
            if 0 <= newx < self.n and 0 <= newy < self.n:
                ans += self.mat[newx][newy]
                # print(self.mat[newx][newy])
        return ans
    def diagonalSum(self, value: int) -> int:
        ans = 0
        row, col = self.location(value)
        for dx, dy in self.diag:
            newx = row + dx
            newy = col + dy
            if 0 <= newx < self.n and 0 <= newy < self.n:
                ans += self.mat[newx][newy]
        return ans
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
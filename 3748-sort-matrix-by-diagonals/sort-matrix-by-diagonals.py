class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(-n+1,n):
            if i <= 0:
                acs = True
            else:
                acs = False
            stack = []
            value = []
            y = max(0,i)
            x = y-i
            stack.append([x,y])
            value.append(grid[x][y])
            # print(x,y)
            while  x+1 < n and y+1 <n:
                x = x+1
                y = y+1
                stack.append([x,y])
                value.append(grid[x][y])
            value.sort(reverse=acs)
            # print(value)
            for j in range(len(stack)):
                grid[stack[j][0]][stack[j][1]] = value[j]
        return grid
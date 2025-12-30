class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def valid(x,y):
            seen = set()
            r1, r2, r3 = [], [], []
            for i in range(3):
                a,b,c = grid[x][y+i],grid[x+1][y+i],grid[x+2][y+i]
                if  a < 1 or a > 9 or b > 9 or c > 9 or b < 1 or c < 1:
                    return False
                if a not in seen:
                    r1.append(a)
                    seen.add(a)
                else:
                    return False
                if b not in seen:
                    r2.append(b)
                    seen.add(b)
                else:
                    return False
                if c not in seen:
                    r3.append(c)
                    seen.add(c)
                else:
                    return False
            sr1,sr2,sr3 = sum(r1), sum(r2), sum(r3)
            if sr1 != sr2 or sr1 != sr3:
                return False
            sc1 = r1[0] + r2[0] + r3[0]
            sc2 = r1[1] + r2[1] + r3[1]
            sc3 = r1[2] + r2[2] + r3[2]

            if sc1 != sc2 or sc1 != sc3:
                return False
            if r1[0] + r3[2] != r1[2] + r3[0]:
                return False
            return True
        
        ans = 0
        m,n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        for i in range(m-2):
            for j in range(n-2):
                if valid(i,j):
                    ans += 1
        # print(valid(0,0))
        return ans
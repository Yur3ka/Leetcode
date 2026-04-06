class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = 0
        face = ['N', 'E', "S", 'W']
        d = {}
        d['N'] = (0,1)
        d['E'] = (1,0)
        d['S'] = (0,-1)
        d['W'] = (-1,0)
        x,y = 0,0
        o = set()
        ans = 0
        for a,b in obstacles:
            o.add((a,b))
        for cm in commands:
            if cm == -1:
                pos = (pos+1)%4
            elif cm == -2:
                pos = (pos-1)%4
            else:
                for i in range(cm):
                    newx = x + d[face[pos]][0]
                    newy = y + d[face[pos]][1]
                    if (newx, newy) in o:
                        break
                    x,y = newx, newy
                    # print(x,y)
                ans = max(ans, x*x + y*y)
        return ans
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0
        line = defaultdict(lambda: defaultdict(set))
        center = defaultdict(lambda: defaultdict(set))
        def line_from_points(x1, y1, x2, y2):
            a = y1 - y2
            b = x2 - x1
            c = x1*y2 - x2*y1

            g = gcd(gcd(abs(a), abs(b)), abs(c))
            if g != 0:
                a //= g
                b //= g
                c //= g

            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c

            return a, b, c
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a,b,c = line_from_points(points[i][0],points[i][1],points[j][0],points[j][1])
                line[(a,b)][c].add(i)
                line[(a,b)][c].add(j)
                cx = points[i][0]+points[j][0]
                cy = points[i][1]+points[j][1]
                center[(cx,cy)][(a,b,c)].add((i,j))
        for k,v in line.items():
            if len(v) < 2:
                continue
            l = list(v.keys())
            for i in range(len(l)):
                base = len(v[l[i]])*(len(v[l[i]])-1)//2
                for j in range(i+1,len(l)):
                    addition = len(v[l[j]])*(len(v[l[j]])-1)//2
                    ans += base*addition
        for k,v in center.items():
            if len(v) < 2:
                continue
            l = list(v.keys())
            for i in range(len(l)):
                base = len(v[l[i]])
                for j in range(i+1,len(l)):
                    addition = len(v[l[j]])
                    ans -= base*addition
            
        # print(center)
        return ans
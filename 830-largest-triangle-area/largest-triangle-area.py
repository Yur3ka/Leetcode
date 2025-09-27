class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_dis(A,B):
            return sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
        ans = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    a = get_dis(points[i],points[j])
                    b = get_dis(points[i],points[k])
                    c = get_dis(points[k],points[j])
                    p = (a+b+c)/2
                    if p <= max(a,b,c):
                        continue
                    else:
                        ans = max(ans,p*(p-a)*(p-b)*(p-c))
        return sqrt(ans)
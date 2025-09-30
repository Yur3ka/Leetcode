class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],-x[1]))
        ans = 0
        for i in range(len(points)):
            usedX = set()
            lastY = -float('inf')
            for j in range(i+1,len(points)):
                if points[j][1] > points[i][1]:
                    continue
                if points[j][0] not in usedX:
                    if points[j][1]>lastY:
                        usedX.add(points[j][0])
                        ans += 1
                        lastY = points[j][1]
                
                
        return ans
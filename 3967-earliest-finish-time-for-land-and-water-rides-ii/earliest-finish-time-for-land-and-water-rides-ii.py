class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        water = []
        land = []
        for i in range(len(landStartTime)):
            land.append((landStartTime[i],landStartTime[i]+landDuration[i]))
        for j in range(len(waterStartTime)):
            water.append((waterStartTime[j],waterStartTime[j]+waterDuration[j]))
        ans = float('inf')
        land.sort(key=lambda x:x[1])
        water.sort(key= lambda x:x[1])
        for event in land:
            if event[0] >= water[0][1]:
                ans = min(ans,event[1])
            else: 
                ans = min(ans,event[1] + water[0][1]-event[0])
        for event in water:
            if event[0] >= land[0][1]:
                ans = min(ans,event[1])
            else:
                ans = min(event[1] + land[0][1]-event[0],ans)
        return ans
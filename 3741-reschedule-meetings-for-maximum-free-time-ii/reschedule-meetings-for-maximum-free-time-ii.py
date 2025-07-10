class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        ans = 0
        free = []
        for i in range(n):
            if i == 0:
                pre = 0
            else:
                pre = endTime[i-1]
            free.append([startTime[i]-pre,i])
        free.append([eventTime-endTime[-1],n])
        # print(free)
        free.sort(key=lambda x:x[0])
        # print(free)
        for i in range(n):
            if i == 0:
                pre = 0
            else:
                pre = endTime[i-1]
            if i == n-1:
                after = eventTime
            else:
                after = startTime[i+1]
            if after - pre < ans:
                continue
            space = 0
            time = endTime[i]-startTime[i]
            start_idx = bisect.bisect_left(free,time,key=lambda x:x[0])
            for j in range(start_idx,len(free)):
                if free[j][1] != i and free[j][1]!= i+1:
                    space = 1
                    break
            curr = startTime[i] - pre + after - endTime[i] + time*space
            ans = max(ans, curr)

        
        return ans
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        step = []
        last = 0
        for i in range(len(startTime)):
            step.append(startTime[i]-last)
            last = endTime[i]
        step.append(eventTime- endTime[-1])
        curr = 0
        for i in range(k+1):
            curr += step[i]
        ans = curr
        for i in range(k+1,len(step)):
            curr += step[i]
            curr -= step[i-k-1]
            ans = max(ans,curr)
        return ans
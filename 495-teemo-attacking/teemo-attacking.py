class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(1,len(timeSeries)):
            step = timeSeries[i] - timeSeries[i-1]
            if step > duration:
                ans += duration
            else:
                ans += step
        ans += duration
        return ans
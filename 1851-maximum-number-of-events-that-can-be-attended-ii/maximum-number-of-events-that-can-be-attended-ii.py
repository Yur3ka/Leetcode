class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)

        curr_max = 0
        memo = dict()
        def attend(remain,pos):
            if remain == 0 or pos == n:
                return 0
            if (remain,pos) in memo:
                return memo[(remain,pos)]

            pre = bisect.bisect_left(events,events[pos][1]+1,key=lambda x:x[0])

            pick = events[pos][2] + attend(remain-1,pre)
            not_pick = attend(remain,pos+1)
            memo[(remain,pos)] = max(pick,not_pick)
            return memo[(remain,pos)]
        return attend(k,0,)

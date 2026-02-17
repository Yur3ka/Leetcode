class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        hour = defaultdict(list)
        hour[0] = [0]
        hour[1] = [8,4,2,1]
        hour[2] = [3,5,9,10,6]
        hour[3] = [7,11]
        minute = defaultdict(list)
        for i in range(60):
            minute[bin(i).count('1')].append(i)
        ans = []
        for i in range(min(4,turnedOn+1)):
            for h in hour[i]:
                for m in minute[turnedOn-i]:
                    temp = str(h) + ':' + '0'*(2-len(str(m))) + str(m)
                    ans.append(temp)
        return ans
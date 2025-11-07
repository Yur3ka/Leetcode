class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        temp = []
        curr = sum(stations[:r+1])
        for i in range(len(stations)):
            temp.append(curr)
            if len(stations)> i-r >= 0:
                curr -= stations[i-r]
            if i+1+r < len(stations):
                curr += stations[i+1+r]
        ans = min(temp)
        left = ans
        right = ans + k
        # print(temp)
        while left <= right:
            needed = 0
            extra = [0]*len(temp)
            e = 0
            status = True
            m = (left+right)//2
            for i in range(len(temp)):
                if temp[i] + e < m:
                    missing = m - temp[i] - e
                    needed += missing
                    if r != 0:
                        # print('!!')
                        e += missing
                        if i + 2*r < len(temp):
                            extra[i+2*r] -= missing
                    if needed > k:
                        right = m -1
                        status = False
                        break
                # print(m,missing,needed,e)
                if r != 0:
                    e += extra[i]
            if status:
                ans = m
                left = m+1
        return ans
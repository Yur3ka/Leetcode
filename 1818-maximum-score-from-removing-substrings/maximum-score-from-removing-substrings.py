class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        prio = []
        if x >= y:
            prio = [('ab',x),('ba',y)]
        else:
            prio = [('ba',y),('ab',x)]
        temp = ''
        for i in range(2):
            pattern,value = prio[i]
            for char in s:
                temp += char
                if len(temp) >=2 and temp[-2:] == pattern:
                    # print(temp,end='-->')
                    ans += value
                    temp = temp[:-2]
                    # print(temp)
            s = temp
            temp = ''
        return ans
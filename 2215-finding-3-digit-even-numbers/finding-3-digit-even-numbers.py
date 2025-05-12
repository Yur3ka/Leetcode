class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = [0]*10
        ans = set()
        for digit in digits:
            count[digit] +=1
        print(count)
        for i in [0,2,4,6,8]:
            # print(i)
            if count[i] == 0:
                continue
            curr = defaultdict(int)
            curr[i] = 1
            for j in range(10):
                if curr[j] == count[j]:
                    continue
                curr[j] += 1
                for k in range(10):
                    if curr[k] == count[k]:
                        continue
                    curr[k] += 1
                    first = k*100+j*10+i
                    second = j*100 + k*10 + i

                    # print(first,second)
                    if first > 99:
                        ans.add(first)
                    if second > 99:
                        ans.add(second)
                    curr[k] -= 1
                curr[j] -= 1
        res = list(ans)
        res.sort()
        return res
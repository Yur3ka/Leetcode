class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Y = 0
        N = 0
        for c in customers:
            if c == 'Y':
                Y += 1
            else:
                N += 1
        min_pen = Y
        curr = Y
        ans = 0
        for i in range(1,len(customers)+1):
            if customers[i-1] == "Y":
                curr -= 1
            else:
                curr += 1
            if curr < min_pen:
                min_pen = curr
                ans = i
            print(i, curr, min_pen)
        if min_pen > N:
            return len(customers)
        else:
            return ans
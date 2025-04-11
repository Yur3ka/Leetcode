class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def equal(n):
            s = str(n)
            if len(s) %2 == 1:
                return False
            mid = len(s) //2
            left = 0
            right = 0
            for i in range(mid):
                left += int(s[i])
                right += int(s[mid+i])
            return left == right
        cnt = 0
        for n in range(low,high + 1):
            if equal(n):
                cnt += 1
        return cnt
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        temp = 0
        ans = 0
        i = 0
        if n == 0:
            return 1
        while temp < n:
            if 1 <<i & n != 0:
                temp += 2**i
            else:
                ans += 2**i
            i += 1
        return ans
        
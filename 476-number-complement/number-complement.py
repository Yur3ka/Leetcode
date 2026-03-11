class Solution:
    def findComplement(self, num: int) -> int:
        temp = 0
        ans = 0
        i = 0
        if num == 0:
            return 1
        while temp < num:
            if 1 <<i & num != 0:
                temp += 2**i
            else:
                ans += 2**i
            i += 1
        return ans
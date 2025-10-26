class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        level = 0
        while n > 0:
            digit = n%10
            if digit != 0:
                ans = ans + digit*(10**level)
                level+=1
            n//=10
        return ans
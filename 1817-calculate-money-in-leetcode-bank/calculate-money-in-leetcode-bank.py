class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n//7
        remain = n%7
        ans = full_weeks*(2*28+(full_weeks-1)*7)//2
        for i in range(remain):
            ans +=i+1+full_weeks
        return ans
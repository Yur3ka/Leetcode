class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(n):
            ans = 0
            while n > 0:
                ans += (n%10)
                n //=10
            return (ans%2) == 0
        ans = 0
        for n in range(1,num+1):
            if n <= num and digit_sum(n):
                ans += 1
        return ans
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        def power(k,n):
            if n == 0:
                return 1
            if n == 1:
                return k
            if n % 2 == 0:
                return power(k,n//2)**2 % MOD
            else:
                return k * power(k,n//2)**2 %MOD
        even = n //2
        if n %2 == 0:
            odd = n //2
        else:
            odd = n //2 + 1
        return power(5,odd)*power(4,even) %MOD
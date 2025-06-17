class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        MAX = n  

        fact = [1] * (MAX + 1)
        inv_fact = [1] * (MAX + 1)

        for i in range(1, MAX + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
        for i in range(MAX - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def combination(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        if m == 1:
            return 1 if k == n - 1 else 0
        pow_part = pow(m - 1, n - 1 - k, MOD)
        choose = combination(n - 1, k)
        ans = m * pow_part % MOD * choose % MOD
        return ans

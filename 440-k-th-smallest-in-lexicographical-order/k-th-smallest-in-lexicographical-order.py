class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_step(n, prefix):
            steps = 0
            start = prefix
            stop = prefix
            while start <= n:
                steps += min(n,stop) - start + 1
                start *= 10
                stop = stop * 10 + 9
            return steps
        current = 1
        k -= 1
        while k > 0:
            steps = count_step(n,current)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        return current
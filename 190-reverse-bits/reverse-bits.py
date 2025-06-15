class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans *= 2
            if n %2 == 1:
                ans += 1
            n //= 2
        return ans
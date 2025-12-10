class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        for num in complexity[1:]:
            if num <= complexity[0]:
                return 0

        ans = 1
        for i in range(1,len(complexity)):
            ans *= i
            ans %= MOD
        return ans
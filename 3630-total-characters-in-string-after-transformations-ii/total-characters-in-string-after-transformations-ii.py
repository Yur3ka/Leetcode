from typing import List
from collections import defaultdict

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def build_transform_matrix():
            T = [[0]*26 for _ in range(26)]
            for i in range(26):
                cnt = nums[i]
                for j in range(1, cnt + 1):
                    T[i][(i + j) % 26] += 1
            return T

        def mat_mult(A, B):
            n, m, p = len(A), len(B[0]), len(B)
            result = [[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    for k in range(p):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def mat_pow(mat, power):
            n = len(mat)
            result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while power > 0:
                if power % 2 == 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result

        # Step 1: Count initial character frequencies
        freq = [0]*26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        # Step 2: Build transformation matrix
        T = build_transform_matrix()

        # Step 3: Raise matrix to power t
        T_t = mat_pow(T, t)

        # Step 4: Multiply initial frequencies with the powered matrix
        # freq is 1x26, T_t is 26x26 → result is 1x26
        final = [0]*26
        for i in range(26):
            for j in range(26):
                final[j] = (final[j] + freq[i] * T_t[i][j]) % MOD

        # Step 5: Sum all frequencies
        return sum(final) % MOD

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ones = []
        p=0
        curr = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] == '0':
                curr *= 2
            else:
                curr = curr * 2 + 1
                ones.append(i)
            if curr > k:
                one_pop = ones.pop(0)
                curr -= 2**(i-one_pop)
                p+= 1
        return len(s) - p

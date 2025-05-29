class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        for i in range(len(s)):
            while curr < len(t) and t[curr] != s[i]:
                curr += 1
            if curr == len(t):
                return False
            curr += 1
        return True
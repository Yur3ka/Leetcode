class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in s and c.upper() in s:
                ans += 1
        return ans 
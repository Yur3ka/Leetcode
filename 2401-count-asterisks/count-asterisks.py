class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        vert = 0
        for i in range(len(s)):
            if s[i] == '|':
                vert += 1
            elif s[i] == '*' and vert %2==0:
                ans += 1
        return ans
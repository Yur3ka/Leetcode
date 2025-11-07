class Solution:
    def sortString(self, s: str) -> str:
        f = [0]*26
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {k:v for v,k in enumerate(alpha)}
        for char in s:
            f[d[char]] += 1
        ans = []
        while len(ans) < len(s):
            for i in range(26):
                if f[i] > 0:
                    ans.append(alpha[i])
                    f[i] -= 1
            for i in range(25,-1,-1):
                if f[i] > 0:
                    ans.append(alpha[i])
                    f[i] -= 1
        return ''.join(ans)
        
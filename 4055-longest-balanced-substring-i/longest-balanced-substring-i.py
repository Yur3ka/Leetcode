class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 1
        for i in range(len(s)):
            c = defaultdict(int)
            for j in range(i+1,len(s)+1):
                c[s[j-1]] += 1
                # print(c)
                if (j-i)%len(c) != 0:
                    continue
                balance = True
                for char in c:
                    if c[char] != (j-i)//len(c):
                        balance = False
                if balance:
                    ans = max(ans,j-i)
        return ans

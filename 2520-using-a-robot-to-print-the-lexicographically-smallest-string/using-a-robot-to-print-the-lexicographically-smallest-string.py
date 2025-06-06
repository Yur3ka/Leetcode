class Solution:
    def robotWithString(self, s: str) -> str:
        suf_min = ['']*len(s)
        ans = ''
        curr_min = 'z'
        for i in reversed(range(len(s))):
            curr_min = min(curr_min,s[i])
            suf_min[i] = (curr_min)
        t = []
        # print(suf_min)
        for i in range(len(s)):
            if not t or t[-1] > suf_min[i]:
                t.append(s[i])
            else:
                while t and t[-1] <= suf_min[i]:
                    ans += t.pop()
                t.append(s[i])
                # print(ans)
        while t:
            ans += t.pop()
        return ans
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        pos = defaultdict(list)
        count = []
        temp = [0]*26
        a = 'abcdefghijklmnopqrstuvwxyz'
        alpha = {k:v for v,k in enumerate('abcdefghijklmnopqrstuvwxyz')}
        # print(alpha)
        for i in range(len(s)):
            pos[s[i]].append(i)
            temp[alpha[s[i]]] += 1
            count.append(temp[:])
        # print(count)
        for char in a:
            if len(pos[char]) < 2:
                continue
            else:
                if len(pos[char]) >=3:
                    ans += 1
                s,e = pos[char][0], pos[char][-1]
                for mid in a:
                    if mid == char:
                        continue
                    # print(char,mid)
                    if count[e][alpha[mid]] - count[s][alpha[mid]] > 0:
                        ans += 1
                        print(char, mid, char)

        return ans
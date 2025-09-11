class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u'])
        vw = []
        for char in s:
            if char.lower() in vowels:
                vw.append(char)

        vw.sort()
        ans = []
        l = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                ans.append(vw[l])
                l+= 1
            else:
                ans.append(s[i])
        return ''.join(ans)
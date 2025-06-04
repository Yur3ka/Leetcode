class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_v = 0
        vowels = {'a','e','i','o','u'}
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        max_v = max(max_v, curr)
        for i in range(k,len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i-k] in vowels:
                curr -= 1
            max_v = max(max_v,curr)
        return max_v
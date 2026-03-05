class Solution:
    def minOperations(self, s: str) -> int:
        ans = float('inf')
        first = 0
        second = 1
        curr1 = 0
        curr2 = 0
        for i in range(len(s)):
            if s[i] != str(first):
                curr1 += 1
            if s[i] != str(second):
                curr2 += 1
            first = 1 - first
            second = 1 - second
        ans = min(ans,curr1,curr2)
        return ans
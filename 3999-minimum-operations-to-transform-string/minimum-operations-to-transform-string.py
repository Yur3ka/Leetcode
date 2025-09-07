class Solution:
    def minOperations(self, s: str) -> int:
        c = Counter(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(1,26):
            if alphabet[i] in c:
                return 26-i
        return 0
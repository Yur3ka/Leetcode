class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code = set()
        for i in range(len(s)-k+1):
            code.add(s[i:i+k])
        return len(code) == 2**k
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if num[i] != '0':
                return num[:i+1]
        return ''
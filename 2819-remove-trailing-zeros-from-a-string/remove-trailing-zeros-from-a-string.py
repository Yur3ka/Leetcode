class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans = ""
        temp = ''
        for char in num:
            if char == '0':
                temp += char
            else:
                ans += temp
                ans += char
                temp = ''
        return ans
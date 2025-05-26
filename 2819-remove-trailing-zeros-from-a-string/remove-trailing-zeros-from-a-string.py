class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans = []
        temp = []
        for char in num:
            if char == '0':
                temp.append(char)
            else:
                ans.extend(temp)
                ans.append(char)
                temp = []
        return ''.join(ans)
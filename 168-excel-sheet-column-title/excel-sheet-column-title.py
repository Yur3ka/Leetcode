class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        row = 1
        # columnNumber -= 1
        while columnNumber > 0:
            curr = columnNumber % 26
            ans.append(curr)
            columnNumber //=(26)
            if curr == 0:
                columnNumber -= 1
            row += 1
        # ans.append(columnNumber)
        res = ''
        # print(ans)
        for num in reversed(ans):
            if num == 0:
                res += "Z"
            else:
                res += chr(64+num)
        return res
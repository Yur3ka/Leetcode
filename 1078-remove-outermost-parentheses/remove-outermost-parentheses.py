class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        temp = []
        op = 0
        cl = 0
        for char in s:
            temp.append(char)
            if char == '(':
                op += 1
            else:
                cl += 1
            if op == cl:
                ans.extend(temp[1:-1])
                temp = []
                op = 0
                cl = 0
        return ''.join(ans)
                
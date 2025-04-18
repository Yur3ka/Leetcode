class Solution:
    def countAndSay(self, n: int) -> str:
        def toRLE(s):
            stack = []
            ans = ""
            for char in s:
                if not stack:
                    stack.append(char)
                elif char != stack[-1]:
                    ans += str(len(stack))
                    ans += stack[-1]
                    stack = [char]
                else:
                    stack.append(char)
            if stack:
                ans += (str(len(stack)))
                ans += stack[-1]
            return ans
        ans = "1"
        for i in range(1,n):
            ans = toRLE(ans)
        return ans
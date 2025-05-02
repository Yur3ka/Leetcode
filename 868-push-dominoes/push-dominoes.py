class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [-1] * n
        right = [-1] * n
        state = False
        curr = 0
        for i in range(n):
            if dominoes[i] == "R":
                state = True
                curr = 0
            elif dominoes[i] == "L":
                state = False
            if state:
                right[i] = curr
                curr += 1
        state = False
        for i in reversed(range(n)):
            if dominoes[i] == "L":
                state = True
                curr = 0
            elif dominoes[i] == "R":
                state = False
            if state:
                left[i] = curr
                curr += 1
        ans = ["."] * n
        for i in range(n):
            if left[i] == right[i]:
                continue
            elif left[i] > right[i]:
                if right[i] > -1:
                    ans[i] = "R"
                else:
                    ans[i] = "L"
            else:
                if left[i] > -1:
                    ans[i] = "L"
                else:
                    ans[i] = "R"
             
        res = "".join(ans)
        
        return res
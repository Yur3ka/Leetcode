class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        last_I = -1
        ans = ["1"]
        curr = 1
        for i in range(n):
            if pattern[i] == 'I':
                ans.append(str(curr+1))
                last_I = i+1
            elif pattern[i] == 'D':
                ans.insert(max(0,last_I),str(curr+1))
                
            curr += 1
        return "".join(ans)
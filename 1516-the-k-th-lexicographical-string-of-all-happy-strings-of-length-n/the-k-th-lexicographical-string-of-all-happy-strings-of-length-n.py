class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        chars = ["a", "b", "c"]
        def helper(word,n):
            if n == 0:
                ans.append(word)
                return
            else:
                for char in chars:
                    if not word or char != word[-1]:
                        helper(word+char,n-1)
        helper("", n)
        
        if len(ans) < k:
            return ""
        else:
            return ans[k-1]
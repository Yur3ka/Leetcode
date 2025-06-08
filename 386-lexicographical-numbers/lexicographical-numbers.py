class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(curr, n):
            for i in range(10):
                next_num = curr *10 + i
                if next_num <= n and next_num != 0:
                    res.append(next_num)
                    dfs(next_num,n)
        dfs(0,n)
        return res
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        b = []
        MOD = 10**9+7
        for i in range(31):
            if n & (1<<i) != 0:
                b.append(i)
        pre = [0]
        for i in b:
            pre.append(i + pre[-1])
        ans = []
        for start,end in queries:
            ans.append(pow(2,pre[end+1]-pre[start],MOD))
        return ans
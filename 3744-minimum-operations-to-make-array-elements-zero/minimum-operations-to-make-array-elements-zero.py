class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        def op(l,r):
            
            start = floor(log(l,4))
            end = floor(log(r,4))
            curr = start*(r-l+1)
            for i in range(start,end+1):
                curr += (r-max(4**i,l)+1)
            return ceil(curr/2)
        for l,r in queries:
            ans += op(l,r)
        return ans
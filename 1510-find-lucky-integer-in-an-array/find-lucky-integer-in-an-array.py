class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        c = Counter(arr)
        for k,v in c.items():
            if k == v:
                ans = max(ans,k)
        return ans